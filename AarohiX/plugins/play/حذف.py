from AarohiX.utils.database import is_music_playing, music_off
from strings import get_command
import asyncio
from strings.filters import command
from AarohiX import app
from AarohiX.core.call import Yukki
from AarohiX.utils.database import set_loop
from AarohiX.utils.decorators import AdminRightsCheck
from AarohiX.utils.database import is_muted, mute_on
from AarohiX.utils.database import is_muted, mute_off
from AarohiX.utils.database import is_music_playing, music_on
from datetime import datetime
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from AarohiX.utils import bot_sys_stats
from AarohiX.utils.decorators.language import language
import random
import config
import re
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import Client, filters
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

START_IMG_URL = getenv("START_IMG_URL")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
MUTE_COMMAND = get_command("MUTE_COMMAND")
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
PING_COMMAND = get_command("PING_COMMAND")
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

api_key = "Vd9FvPMOKWfsKJNG9RbZnItaTNIRFzVyyXFdrGHONVsGqHcHBoj3AI3sIlNuqzuf0ZNG8uLcF9wAd5DXBBnUzA"
y = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
y.verbose = False

  

@app.on_message(
     command(["بوت حذف","رابط حذف","حذف حساب","عاوز احذف","حذف"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/50228546bd85a32fecd6e.jpg",
        caption=f"""**عاوز تحذف يا عـمري هتوحشني**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("رابط الحذف🗑", url=f"https://t.me/LC6BOT"),
                ],[
                InlineKeyboardButton(
                        "𓌹 ↱ 𝘿ٓ𝙀ٓ𝙑ٰٰ 𝙆ٓ𝙎ٓ𝙃ٓ𝙏ٓ𝘼ّ𝙃ٰ 𝘽ٰٓ𝘼ٓ𝙎ٓ𝙃َٓ𝘼 ↲ 𓌺", url=f"https://t.me/DEV_KSHTAH"), 
                ],[
                InlineKeyboardButton(
                        "𝙎𝙊𝙐𝙍𝘾𝞝 ࿊ 𝙏𝙐𝙍𝘽𝙊", url=f"http://t.me/SOURCE_Turbo"), 
                ]
            ]
        ),
    )
