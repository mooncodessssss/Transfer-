from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from AviaxMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, User
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden, PeerIdInvalid, ChatAdminRequired
from pyrogram.enums import ChatAction, ChatType, MessageEntityType
from pyrogram import Client, filters, enums
from AviaxMusic.misc import SUDOERS

buttons = [
    [
        InlineKeyboardButton(
            text="➕ 𝐀𝐃𝐃 𝐌𝐄 𝐁𝐀𝐁𝐘", 
            url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users"
        ),
    ],
]

@app.on_message(filters.command(["untold"]) & SUDOERS)
async def promos(client, message: Message):
    AMBOT = f"""{app.mention},
🌙 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐌𝐔𝐒𝐈𝐂 𝐏𝐋𝐀𝐘𝐄𝐑 𝐁𝐎𝐓 𝐅𝐎𝐑 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐆𝐑𝐎𝐔𝐏 𝐕𝐈𝐃𝐄𝐎𝐂𝐇𝐀𝐓𝐒 🌙
😘 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒 😘
● 𝐈 𝐂𝐀𝐍 𝐏𝐋𝐀𝐘 𝐒𝐎𝐍𝐆 𝐈𝐍 𝐆𝐑𝐎𝐔𝐏 𝐕𝐂 ☺
● 𝐍𝐎 𝐋𝐀𝐆 ☺
● 𝐁𝐄𝐒𝐓 𝐒𝐎𝐔𝐍𝐃 𝐐𝐔𝐀𝐋𝐈𝐓𝐘 ☺
● 𝟐𝟒𝐱𝟕 𝐔𝐏𝐓𝐈𝐌𝐄 ☺
● 𝐋𝐀𝐆 𝐅𝐑𝐄𝐄 ☺
"""
    await message.reply(
        text=AMBOT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
