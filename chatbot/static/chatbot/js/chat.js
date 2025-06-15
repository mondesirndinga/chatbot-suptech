document.addEventListener('DOMContentLoaded', function () {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const voiceBtn = document.getElementById('voice-btn');
    const voiceStatus = document.getElementById('voice-status');
    const resourcesContainer = document.getElementById('resources-container');

    let recognition;
    let isSending = false; // 🚫 Empêche l’envoi multiple

    try {
        recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'fr-FR';

        recognition.onstart = function () {
            voiceBtn.classList.add('listening');
            voiceStatus.textContent = "🎙️ Écoute en cours...";
        };

        recognition.onresult = function (event) {
            const transcript = event.results[0][0].transcript;
            userInput.value = transcript;
            voiceStatus.textContent = "📝 Question reçue : " + transcript;

            // ✅ Petit délai pour laisser le champ se remplir avant envoi
            setTimeout(() => {
                sendMessage();
            }, 300);
        };

        recognition.onend = function () {
            voiceBtn.classList.remove('listening');
        };

        recognition.onerror = function (event) {
            voiceStatus.textContent = "❌ Erreur : " + event.error;
            voiceBtn.classList.remove('listening');
        };
    } catch (e) {
        voiceBtn.style.display = 'none';
        console.warn("⚠️ Reconnaissance vocale non supportée.");
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (!message || isSending) return;

        isSending = true;
        addMessage(message, 'user');
        userInput.value = '';

        fetch('/chatbot/api/chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => {
            if (response.redirected) {
                window.location.href = response.url;
                return;
            }
            return response.json();
        })
        .then(data => {
            if (!data) return;

            if (data.status === 'success') {
                addMessage(data.response, 'bot');

                const lowerMessage = message.toLowerCase();
                if (lowerMessage.includes('ressource') || lowerMessage.includes('pédagogique')) {
                    resourcesContainer.style.display = 'block';
                    resourcesContainer.scrollIntoView({ behavior: 'smooth' });
                }
            } else {
                addMessage("Désolé, une erreur s'est produite.", 'bot');
            }
        })
        .catch(error => {
            console.error('Erreur lors de la requête :', error);
            addMessage("Désolé, le service est temporairement indisponible.", 'bot');
        })
        .finally(() => {
            isSending = false;
        });
    }

    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);
        messageDiv.innerHTML = text;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                return decodeURIComponent(cookie.substring(name.length + 1));
            }
        }
        return null;
    }

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    if (recognition) {
        voiceBtn.addEventListener('click', function () {
            try {
                recognition.start();
            } catch (e) {
                voiceStatus.textContent = "🔁 Micro déjà activé";
            }
        });
    }
});
