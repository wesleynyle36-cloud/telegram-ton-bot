import os
import json
import firebase_admin
from firebase_admin import credentials, db
from pyrogram import Client, filters

# ---------------- FIREBASE ----------------
firebase_key = json.loads(os.environ["FIREBASE_KEY"])

cred = credentials.Certificate(firebase_key)
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://telegram-bot-ae675-default-rtdb.asia-southeast1.firebasedatabase.app"
})

# Test write on startup
ref = db.reference("test")
ref.set({
    "status": "firebase connected",
    "working": True
})

# ---------------- TELEGRAM ----------------


app = Client(
    "tonalt_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    # Save user to Firebase
    db.reference(f"users/{user_id}").set({
        "joined": True
    })

    await message.reply_text("👋 Welcome! You are registered.")

print("Bot is running...")
app.run()




