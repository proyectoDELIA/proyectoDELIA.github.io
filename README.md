# proyectoDELIA.github.io
Front-end de juguete para proyecto DELIA

Pese a que GitHub permite hostear aplicaciones front-end, no podemos conectarlas directamente a un back-end en GitHub. Sin embargo, podemos conectarlo a un back-end hosteado en otra parte a través de APIs (FastAPI) y viceversa.

------------------------
🤔 Paso ?: Instalar FFMPEG para el reconocimiento de voz
Nuestro Chatbot tiene implementado un reconocedor de voz, pero para utilizarlo, debes instalar FFMPEG, un software de código abierto para el tratamiento de archivos de audio. Para instalarlo, debes:
1.   Ir a https://www.ffmpeg.org/download.html y descargar la versión que más se adecúe a tu sistema operativo.
2.   Extrae el archivo descargado.
3.   Coloca la carpeta extraída, junto a todos sus contenidos, en una ruta no muy profunda.
4.   Añade la ruta de la carpeta ffmpeg/bin a tu PATH.
5.   Asegúrate de que FFMPEG está instalando escribiendo en tu terminal de tu comandos la siguiente línea: ffmpeg -version (en Windows, en Mac será otro el comando)
   
🧪 Paso 1: Crear y activar entorno virtual del backend

1.	Abre una terminal y colócate en la raíz del proyecto.
2.	Crea un entorno virtual para el backend:
     python -m venv nombre_del_entorno
3.	Activa el entorno: nombre_del_entorno\Scripts\activate (para Windows) o source nombre_del_entorno/bin/activate (para macOS/Linux)
4.	Instala las dependencias: pip install -r backend/requirements.txt
5.	Paso extra: comprueba que el entorno virtual también tiene acceso a la ruta de FFMPEG. Si el backend no encuentra la ruta, no funcionará el reconocedor de voz.

🚀 Paso 2: Ejecutar el backend con FastAPI

1.	En la misma terminal (con el entorno virtual activado), entra en la carpeta del backend: cd backend
3.	Lanza el servidor FastAPI: uvicorn main:app --reload
4.	Si todo va bien, verás este mensaje: INFO:     Application startup complete.
📍 FastAPI estará disponible en: http://127.0.0.1:8000
➡️ Deja esta terminal abierta y funcionando.

🤖 Paso 3: Ejecutar Rasa 

1.	Abre una segunda terminal nueva.
2.	Activa el entorno virtual que tengas creado para Rasa. Previamente debes haber instalado en ese entorno el requirements.txt con las dependencias del chatbot. 
3.	Colócate en la carpeta donde esté guardado el chatbot.
4.	Lanza Rasa con el comando: rasa run --enable-api
5.	En la terminal verás: Rasa server is up and running. 
📍 Rasa escuchará en: http://localhost:5005/webhooks/rest/webhook
➡️ Deja esta segunda terminal abierta también.

🛠️ Paso 4: Ejecutar servidor de acciones de Rasa

1.	Abre una tercera terminal nueva.
2.	Activa el mismo entorno virtual de Rasa.
3.	Colócate en la carpeta donde esté guardado el chatbot.
4.	Ejecuta el servidor de acciones con el comando: rasa run actions
5.	En la terminal verás: Action endpoint is up and running on http://0.0.0.0:5055
📍 El servidor de acciones estará corriendo en: http://localhost:5055
➡️ También deja esta tercera terminal abierta.

🌐 Paso 5: Probar el bot en el navegador

1.	Abre en el navegador el archivo index.html que está en la carpeta frontend.
2.	Ya puedes hablar con el bot desde la interfaz web.







