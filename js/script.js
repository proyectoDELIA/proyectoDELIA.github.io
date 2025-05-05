// -------------- DOM Elements --------------
const input = document.getElementById("input");
const chatWindow = document.getElementById("ventana-chat");

// -------------- Show Bot Response and Buttons --------------
function mostrarRespuestaDelBot(data) {
  const botmensaje = document.createElement("div");
  botmensaje.className = "mensaje bot";
  botmensaje.textContent = data.respuesta_traducida || data.respuesta_rasa || "Sin respuesta del bot.";
  chatWindow.appendChild(botmensaje);
  chatWindow.scrollTop = chatWindow.scrollHeight;
  
  if (data.botones && data.botones.length > 0) {
    const botonesContainer = document.createElement("div");
    botonesContainer.className = "botones-opciones";

    data.botones.forEach(boton => {
      const btn = document.createElement("button");
      btn.className = "boton-opcion";
      btn.textContent = boton.title;

      btn.onclick = () => {
        botonesContainer.remove(); // Remove buttons

        const usermensaje = document.createElement("div");
        usermensaje.className = "mensaje user";
        usermensaje.textContent = boton.title;
        chatWindow.appendChild(usermensaje);
        chatWindow.scrollTop = chatWindow.scrollHeight;

        // Send payload to backend
        fetch("http://127.0.0.1:8000/procesar-y-enviar/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ mensaje: boton.payload })
        })
        .then((response) => response.json())
        .then((data) => mostrarRespuestaDelBot(data))
        .catch((error) => {
          console.error("Error al enviar opción seleccionada:", error);
          const botError = document.createElement("div");
          botError.className = "mensaje bot";
          botError.textContent = "❌ Error al conectar con el servidor.";
          chatWindow.appendChild(botError);
          chatWindow.scrollTop = chatWindow.scrollHeight;
        });
      };

      botonesContainer.appendChild(btn);
    });

    chatWindow.appendChild(botonesContainer);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }
}

// -------------- Sending Message on Enter Key --------------
input.addEventListener("keypress", function (e) {
  if (e.key === "Enter" && input.value.trim() !== "") {
    const usermensaje = document.createElement("div");
    usermensaje.className = "mensaje user";
    usermensaje.textContent = input.value.trim();
    chatWindow.appendChild(usermensaje);

    const botmensaje = document.createElement("div");
    botmensaje.className = "mensaje bot";
    botmensaje.textContent = "( . . . )";
    chatWindow.appendChild(botmensaje);

    const mensaje = input.value.trim();
    input.value = "";
    chatWindow.scrollTop = chatWindow.scrollHeight;

    fetch("http://127.0.0.1:8000/procesar-y-enviar/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensaje })
    })
    .then((response) => response.json())
    .then((data) => {
      botmensaje.remove();  // Remove "typing..."
      mostrarRespuestaDelBot(data); // Show actual bot response
    })
    .catch((error) => {
      console.error("Error al enviar mensaje:", error);
      botmensaje.textContent = "❌ Error al conectar con el servidor.";
    });
  }
});

// -------------- Audio Recording Logic --------------
let isRecording = false;
let mediaRecorder;
let audioChunks = [];

async function toggleRecording() {
  if (isRecording) {
    mediaRecorder.stop();
    document.getElementById('recordButton').innerHTML = '<img id="recordIcon" src="images/mic.svg" style="width: 30px; height: 30px" />';
    isRecording = false;
  } else {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder = new MediaRecorder(stream);
      audioChunks = [];

      mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
      };

      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);

        const audiomensaje = document.createElement('div');
        audiomensaje.classList.add('mensaje', 'user');

        const audioElement = document.createElement('audio');
        audioElement.controls = true;
        audioElement.src = audioUrl;

        audiomensaje.appendChild(audioElement);
        chatWindow.appendChild(audiomensaje);
        chatWindow.scrollTop = chatWindow.scrollHeight;

        sendAudioToServer(audioBlob);
      };

      mediaRecorder.start();
      document.getElementById('recordButton').innerHTML = '<img id="recordIcon" src="images/arrow-right-short.svg" style="width: 30px; height: 30px" />';
      isRecording = true;
    } catch (err) {
      console.error('Error accessing the microphone:', err);
    }
  }
}

function sendAudioToServer(audioBlob) {
  const formData = new FormData();
  formData.append('audio', audioBlob, 'recorded_audio.wav');

  fetch('http://127.0.0.1:8000/procesar-y-enviar/', {
    method: 'POST',
    body: formData
  })
  .then((response) => response.json())
  .then((data) => mostrarRespuestaDelBot(data))
  .catch((error) => {
    console.error("Error al enviar audio:", error);
    const botmensaje = document.createElement("div");
    botmensaje.className = "mensaje bot";
    botmensaje.textContent = "❌ Error al conectar con el servidor.";
    chatWindow.appendChild(botmensaje);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  });
}

// -------------- Mic Button Event Listener --------------
document.getElementById('recordButton').addEventListener('click', toggleRecording);

// -------------- Dark Mode Toggle --------------
function toggleDarkMode() {
  document.body.classList.toggle("modo-oscuro");

  const isDark = document.body.classList.contains("modo-oscuro");
  document.querySelectorAll(".dark-toggle-icon").forEach(el => {
    el.style.filter = isDark ? "invert(1)" : "none";
  });
}

// -------------- Settings Panel Toggle --------------
function toggleSettings() {
  document.getElementById("panel-ajustes").classList.toggle("open");
}

// -------------- Textarea Auto Resize --------------
const textarea = document.getElementById("input");

textarea.addEventListener("input", () => {
  textarea.rows = 1;
  const lines = textarea.value.split("\n").length;
  textarea.rows = Math.min(lines, 10);
});

// -------------- Language Selection --------------
function setLanguageAndShowWelcome(lang, button) {
  fetch("http://127.0.0.1:8000/establecer-idioma-y-welcome/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ idioma: lang })
  })
  .then((response) => response.json())
  .then((data) => {
    mostrarRespuestaDelBot(data);
    const allButtons = document.querySelectorAll(".flag-button");
    allButtons.forEach(btn => {
      btn.classList.add("disabled");
      btn.classList.remove("selected");
    });
    button.classList.add("selected");
  })
  .catch((error) => {
    console.error("Error al establecer idioma:", error);
  });
}
