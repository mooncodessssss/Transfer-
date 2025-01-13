from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from AviaxMusic import app
from config import OWNER_ID

@app.on_chat_member_updated(filters.group)
async def greet_new_member(_, member: ChatMemberUpdated):
    # Check if the user has joined the voice chat
    if member.new_chat_member and not member.old_chat_member:
        if member.new_chat_member.status == "member":  # Check if they are a member
            user = member.new_chat_member.user
            chat_id = member.chat.id
            
            # Send a message mentioning the user
            await app.send_message(
                chat_id,
                f"🎉 Welcome {user.mention} to the voice chat! 🎤"
            )

app.run()
