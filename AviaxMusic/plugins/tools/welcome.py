from AviaxMusic import app
from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from PIL import ImageChops

LOGGER = getLogger(__name__)

@app.on_message(filters.command("wel") & ~filters.private)
async def auto_state(_, message):
    if len(message.command) == 1:
        return await message.reply_text("Usage: /wel [on|off]")
    
    chat_id = message.chat.id
    state = message.text.split(None, 1)[1].strip().lower()
    
    if state == "off":
        # Disable welcome message logic
        await message.reply_text("Welcome message disabled.")
    elif state == "on":
        # Enable welcome message logic
        await message.reply_text("Welcome message enabled.")
    else:
        await message.reply_text("Usage: /wel [on|off]")

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):
    if member.new_chat_member and not member.old_chat_member:
        user = member.new_chat_member.user
        await app.send_message(
            member.chat.id,
            f"Hi {user.first_name}, Glad you’re here!!"
        )
