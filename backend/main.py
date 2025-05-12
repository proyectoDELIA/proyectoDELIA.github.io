from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator
import requests
from fastapi.middleware.cors import CORSMiddleware
# Imports específicos para enviar audios y transcribirlos
from fastapi import UploadFile, File, Request
import whisper
import tempfile

# ───────────────── CONFIGURACIÓN ─────────────────
app = FastAPI()
translator = Translator()
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"
IDIOMA_USUARIO = "es"  # español por defecto
model = whisper.load_model("medium")

# Middleware CORS para permitir conexión con frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ───────────────── MODELOS DE DATOS ─────────────────
class MensajeUsuario(BaseModel):
    mensaje: str


class IdiomaSeleccionado(BaseModel):
    idioma: str


# ───────────────── FUNCIONES ─────────────────

def traducir(texto: str, destino: str) -> str:
    '''
    Traduce un texto si el idioma original no es español
    '''
    if destino == "es":
        return texto
    try:
        return translator.translate(texto, dest=destino).text
    except Exception as e:
        print(f"[ERROR] Fallo en traducción: {e}")
        return texto


def enviar_a_rasa(mensaje: str) -> list:
    '''
    Envía un mensaje a Rasa y devuelve su respuesta como lista
    '''
    payload = {"sender": "usuario", "message": mensaje}
    print(f"[DEBUG] Mensaje enviado a Rasa: {payload}")
    response = requests.post(RASA_URL, json=payload)
    response.raise_for_status()
    return response.json()


def extraer_respuesta_y_botones(rasa_respuesta: list, idioma: str) -> tuple:
    '''
    Extrae el texto y los botones de la respuesta de Rasa y los traduce si es necesario
    '''
    texto = next((m["text"] for m in rasa_respuesta if "text" in m), None)
    print(f"[DEBUG] Respuesta original: '{texto}'")
    respuesta_traducida = traducir(texto, idioma)
    print(f"[DEBUG] Respuesta traducida: '{respuesta_traducida}'")

    botones = next((m.get("buttons") for m in rasa_respuesta if "buttons" in m), [])
    # Traducir títulos de botones si el idioma no es español
    if idioma != "es":
        for boton in botones:
            try:
                original = boton["title"]
                boton["title"] = translator.translate(boton["title"], dest=idioma).text
                print(f"[DEBUG] Botón traducido: '{original}' → '{boton['title']}'")
            except Exception as e:
                print(f"[ERROR] No se pudo traducir el botón '{boton['title']}': {e}")

    return texto, respuesta_traducida, botones


# ───────────────── ENDPOINTS ─────────────────

# Establece el idioma del usuario y devuelve un mensaje de bienvenida
@app.post("/establecer-idioma-y-welcome/")
async def establecer_idioma_y_welcome(data: IdiomaSeleccionado):
    global IDIOMA_USUARIO
    IDIOMA_USUARIO = data.idioma
    print(f"[DEBUG] Idioma establecido: {IDIOMA_USUARIO}")

    try:
        respuesta_rasa = enviar_a_rasa("/iniciar_sesion")
        texto, respuesta_traducida, botones = extraer_respuesta_y_botones(respuesta_rasa, IDIOMA_USUARIO)

        return {
            "mensaje": f"Idioma establecido: {IDIOMA_USUARIO.upper()}",
            "respuesta_rasa": texto,
            "respuesta_traducida": respuesta_traducida,
            "botones": botones
        }
    except Exception as e:
        print(f"[ERROR] Fallo al establecer idioma: {e}")
        return {"error": str(e)}


# Procesa un mensaje del usuario, lo traduce y lo reenvía a Rasa
@app.post("/procesar-y-enviar/")
async def procesar_y_enviar(request: Request, audio: UploadFile = File(None)):
    try:
        if audio:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(await audio.read())
                tmp_path = tmp.name

            print(f"[DEBUG] Archivo de audio guardado temporalmente en {tmp_path}")
            resultado = model.transcribe(tmp_path, language='es')
            mensaje_transcrito = resultado.get("text", "").strip()
            print(f"[DEBUG] Audio transcrito: '{mensaje_transcrito}'")

            mensaje_es = mensaje_transcrito
        else:
            data = await request.json()
            mensaje_usuario = data.get("mensaje", "").strip()
            print(f"[DEBUG] Mensaje recibido: '{mensaje_usuario}' (idioma: {IDIOMA_USUARIO})")
            mensaje_es = traducir(mensaje_usuario, "es") if IDIOMA_USUARIO != "es" else mensaje_usuario
            print(f"[DEBUG] Mensaje traducido al español: '{mensaje_es}'")

        respuesta_rasa = enviar_a_rasa(mensaje_es)
        texto, respuesta_traducida, botones = extraer_respuesta_y_botones(respuesta_rasa, IDIOMA_USUARIO)

        return {
            "idioma_usuario": IDIOMA_USUARIO,
            "mensaje_traducido": mensaje_es,
            "respuesta_rasa": texto,
            "respuesta_traducida": respuesta_traducida,
            "botones": botones
        }

    except Exception as e:
        print(f"[ERROR] Fallo en procesar-y-enviar: {e}")
        return {"error": str(e)}
