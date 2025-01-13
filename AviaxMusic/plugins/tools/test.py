from pyrogram import Client, filters
from pyrogram.types import Message
from ANNIEMUSIC import app
from config import OWNER_ID

# invite members on voice 
@app.on_message(filters.video_chat_members_invited)
async def brah3(app :app, message:Message):
           text = f"♻️ ❛{message.from_user.mention}❜ 💞™🌙 ɪɴᴠɪᴛᴇᴅ "
           x = 0
           for user in message.video_chat_members_invited.users:         
           await app.send_message(member.chat.id,  
            text += f"🖤[{user.first_name}](tg://user?id={user.id})🖤! "
               x += 1
             except Exception:
               pass
