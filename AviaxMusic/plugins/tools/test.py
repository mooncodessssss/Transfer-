import qrcode
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
import os

app = Client("my_bot")

# Function to generate QR code
def generate_qr_code(voice_chat_link, user_id):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(voice_chat_link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    qr_code_path = f"qr_code_{user_id}.png"
    img.save(qr_code_path)
    return qr_code_path

@app.on_chat_member_updated(filters.group)
async def greet_new_member(_, member: ChatMemberUpdated):
    # Check if the user has joined the voice chat
    if member.new_chat_member and not member.old_chat_member:
        if member.new_chat_member.status == "member":  # Check if they are a member
            user = member.new_chat_member.user
            chat_id = member.chat.id
            
            # Create the voice chat link (replace with your actual voice chat link)
            voice_chat_link = f"tg://joinvoicechat/{member.chat.username}"  # Ensure the chat has a username
            
            # Generate QR code for the voice chat link
            qr_code_path = generate_qr_code(voice_chat_link, user.id)
            
            # Send a message mentioning the user and include the QR code
            await app.send_photo(
                chat_id,
                photo=qr_code_path,
                caption=f"🎉 Welcome {user.mention} to the voice chat! 🎤\nScan the QR code to join the voice chat."
            )
            
            # Optionally, remove the QR code image after sending
            os.remove(qr_code_path)

app.run()
