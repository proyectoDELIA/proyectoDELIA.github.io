# proyectoDELIA.github.io
Front-end de juguete para proyecto DELIA

Pese a que GitHub permite hostear aplicaciones front-end, no podemos conectarlas directamente a un back-end en GitHub. Sin embargo, podemos conectarlo a un back-end hosteado en otra parte a través de APIs (FastAPI) y viceversa.

------------------------
Paso 1: crear un entorno virtual para el backend e instalar en él el requirements.txt que está en la carpeta backend. (pip install -r backend/requirements.txt). Activar el entorno.

Paso 2: ejecutar backend (comando uvicorn main:app --reload desde carpeta "backend"). 📍 FastAPI estará corriendo en: http://127.0.0.1:8000 En la terminal verás: "INFO: Application startup complete." Dejar la terminal abierta así.

Paso 3: ejecutar rasa. Abrir una segunda ventana de la terminal. Activar un entorno virtual para Rasa (debe tener instalado el requirements.txt de la carpeta "chatbot"). Lanzar Rasa. Comando rasa run --enable-api desde carpeta "chatbot". 📍 Rasa escuchará en: http://localhost:5005/webhooks/rest/webhook En la termninal verás: "2025-04-21 22:23:33 INFO root - Rasa server is up and running." Dejar la terminal abierta así.

Paso 4: ejecutar servidor de acciones de Rasa (si se utiliza el actions.py). Abrir una tercera ventana de la terminal. Activar también el entorno virtual de rasa. Lanzar servidor de acciones de Rasa. Comando rasa run actions desde carpeta "chatbot". 📍 Servidor de acciones corriendo en http://localhost:5055 En la terminal verás: "Action endpoint is up and running on http://0.0.0.0:5055" Dejar la terminal abierta así.

Paso 5: Abrir index.html en el navegador. Hablar con el bot.
