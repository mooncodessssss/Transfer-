from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
import os
from AviaxMusic import app
from config import OWNER_ID

@app.on_chat_member_updated(filters.group)
async def greet_new_member(_, member: ChatMemberUpdated):
    # Check if the user has joined the voice chat
    if member.new_chat_member and not member.old_chat_member:
        if member.new_chat_member.status == "member":  # Check if they are a member
            user = member.new_chat_member.user
            chat_id = member.chat.id
            
            # Create the voice chat link (replace with your actual voice chat link)
            voice_chat_link = f"tg://joinvoicechat/{member.chat.username}"  # Ensure the chat has a username
            
            # Send a message mentioning the user and include the QR code
            await app.send_photo(
                chat_id,
                caption=f"🎉 Welcome {user.mention} to the voice chat! 🎤\nScan the QR code to join the voice chat."
            )
