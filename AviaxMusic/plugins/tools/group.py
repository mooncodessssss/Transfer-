from pyrogram import Client, filters
from pyrogram.types import Message
from AviaxMusic import app
from config import OWNER_ID

# Dictionary to track user join messages
join_messages = {}

@app.on_chat_member_updated()
async def voice_chat_notifier(client: Client, update: ChatMemberUpdated):
    if update.new_chat_member.is_member and update.new_chat_member.voice_chat:
        user = update.new_chat_member.user
        group = update.chat
        message = await client.send_message(
            group.id,
            f"🎙️ {user.first_name} has joined the voice chat."
        )
        join_messages[user.id] = message.message_id
    elif not update.new_chat_member.is_member and update.old_chat_member.voice_chat:
        user = update.old_chat_member.user
        group = update.chat
        if user.id in join_messages:
            await client.delete_messages(group.id, join_messages[user.id])
            del join_messages[user.id]
