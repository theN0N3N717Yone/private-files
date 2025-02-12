#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = "<b>○ Creator : <a href='https://t.me/zedplusplus'>This Person</a>\n○ Language : <code>Python3</code>\n○ Index : <a href='https://t.me/mxpbox'>Click here</a>\n○ Channel : <a href='https://t.me/+KBpcBedzPaw2Mzg1'>Private</a>\n○ Support Group : @mxpbox_support </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
