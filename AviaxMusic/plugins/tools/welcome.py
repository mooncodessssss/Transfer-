from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from AviaxMusic import app

LOGGER = getLogger(__name__)

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id

    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return

    user = member.new_chat_member.user if member.new_chat_member else member.from_user

    # Simple text-based welcome message
    try:
        await app.send_message(
            chat_id,
            f"Hi {user.mention}, glad you’re here!"
        )
    except Exception as e:
        LOGGER.error(f"Failed to send welcome message: {e}")
