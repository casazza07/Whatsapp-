from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

# Chave da API do OpenAI vinda das variáveis de ambiente
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    user_msg = request.form.get("Body")

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_msg}]
    )

    chat_reply = resposta['choices'][0]['message']['content']

    twilio_resp = MessagingResponse()
    twilio_resp.message(chat_reply)
    return str(twilio_resp)

@app.route("/")
def home():
    return "Servidor do bot rodando!"

if __name__ == "__main__":
    app.run()
