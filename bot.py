import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase_key.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://telegram-bot-ae675-default-rtdb.asia-southeast1.firebasedatabase.app"
})


from pyrogram import Client

API_ID = 34582790
API_HASH = "cff1082d205c1de35297e084aac7e46b"
BOT_TOKEN = "8567930962:AAEAnY27LjeKMQwWiTjuPEb1Lm6bdc1T2eQ"

app = Client(
    "tonalt_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
def all_messages(client, message):
    print("Message received:", message.text)
    message.reply_text("👋 I received your message!")

print("Bot is running...")
app.run()
ref = db.reference("test")

ref.set({
    "status": "firebase connected",
    "working": True
})
