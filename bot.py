import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import BoundFilter, CommandStart
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ChatJoinRequest

# Manba @MistrUZ | @MrGayratov
# Manbaga Tegilmasin !
# Kanalga obuna bolish so'ro'vnomasini avto qabul qiladigon bot kodi
# Token va ID ingizni qo`yib run qiling
# 1-Ish pip install aiogram
# 2-Ish  run qilish

TOKEN = "5729562816:AAGFT_r5zklmg8d3Ki2sInroydvtPPWknV8"
ADMINS = 1625900856

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

add_channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="➕ Add channel",url="https://t.me/ReaLJoin_Robot?startchannel="),InlineKeyboardButton(text="➕ Add group", url="https://t.me/ReaLJoin_Robot?startgroup=start")],])


class Shaxsiy(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE

@dp.message_handler(Shaxsiy(), CommandStart())
async def bot_start(message: types.Message):
    await message.reply(f"Assalomu alekum {message.from_user.full_name} \n\nKanallar va Guruxlarga qo'shilish so'rovini avtomatik tasdiqlaydigan botga hush kelibsiz\n\nAvvalo botni kanallingiz yoki guruxingizga admin qiling 💡", reply_markup=add_channel)



class Kanal(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.CHANNEL

TEXT=os.environ.get("TASDIQLANGAN_XABARI", "Yangi Obunachi {mention}\n\n{title} kanaliga qo'shildi\n\n")

@dp.chat_join_request_handler(Kanal())
async def Tasdiqlash (message: ChatJoinRequest):
    chat=message.chat
    user=message.from_user
    print(f"{user.first_name} Obuna Boldi")
    await bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    await bot.send_message(chat_id=user.id, text="Xush Kelibsiz")
    await bot.send_message(chat_id=ADMINS, text=TEXT.format(mention=user.mention, title=chat.title))

class Guruh(BoundFilter):
    async def check(self,message: types.Message):
        return message.chat.type == types.ChatType.SUPERGROUP

@dp.chat_join_request_handler(Guruh())
async def Tasdiqlash (message: ChatJoinRequest):
    chat=message.chat
    user=message.from_user
    print(f"{user.first_name} Obuna Boldi")
    await bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    await bot.send_message(chat_id=user.id, text="Xush Kelibsiz")


if __name__ == '__main__':
    executor.start_polling(dp)