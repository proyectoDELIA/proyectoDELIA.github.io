from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator
import requests
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
translator = Translator()

# Middleware para permitir que el frontend acceda a este backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Se puede restringir a un dominio específico
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# URL donde está corriendo el webhook REST de Rasa
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

# Modelo de datos que espera recibir el backend desde el frontend (solo un campo: "mensaje")
class MensajeUsuario(BaseModel):
    mensaje: str

# Endpoint que recibe el mensaje, lo traduce al español, lo envía a Rasa y devuelve la respuesta traducida
@app.post("/procesar-y-enviar/")
async def procesar_y_enviar(mensaje_usuario: MensajeUsuario):
    mensaje = mensaje_usuario.mensaje
    print(f"Mensaje recibido: {mensaje}")

    try:
        # Detectar el idioma original del mensaje
        idioma = translator.detect(mensaje).lang
        print(f"Idioma detectado: {idioma}")

        # Traducir al español si no es español
        mensaje_es = mensaje
        if idioma != "es":
            mensaje_es = translator.translate(mensaje, dest="es").text
            print(f"Mensaje traducido al español: {mensaje_es}")

        # Enviar el mensaje traducido a Rasa
        response = requests.post(
            RASA_URL,
            json={"sender": "usuario", "message": mensaje_es}
        )

        # Procesar respuesta de Rasa
        rasa_respuesta = response.json()
        if not rasa_respuesta:
            return {"error": "Rasa no devolvió ninguna respuesta"}

        # Extraer el primer mensaje de texto de la respuesta (puede haber más)
        respuesta_texto = None
        for mensaje in rasa_respuesta:
            if "text" in mensaje:
                respuesta_texto = mensaje["text"]
                break

        if not respuesta_texto:
            return {"error": "La respuesta de Rasa no contiene texto"}

        # Traducir la respuesta del bot al idioma del usuario (si era distinto del español)
        respuesta_traducida = respuesta_texto
        if idioma != "es":
            respuesta_traducida = translator.translate(respuesta_texto, dest=idioma).text
            print(f"Respuesta traducida al idioma original ({idioma}): {respuesta_traducida}")

        # Devolver al frontend todos los datos útiles
        return {
            "idioma_original": idioma,
            "mensaje_traducido": mensaje_es,
            "respuesta_rasa": respuesta_texto,
            "respuesta_traducida": respuesta_traducida
        }

    except Exception as e:
        # Si algo sale mal, devolver error
        return {"error": str(e)}
