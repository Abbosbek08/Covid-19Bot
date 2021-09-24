import logging
import requests
from aiogram import Bot,Dispatcher,executor,types

url='https://ca-uz.herokuapp.com/'
API_TOKEN='BOT TOKENI'

logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(m: types.Message):
  await m.answer("Assalomu aleykum\nBuyruqlar: /uzbekistan /dunyo")

@dp.message_handler(commands=['dunyo'])
async def get_stat(m: types.Message):
  r=requests.get(url+'world')
  j=r.json()
  text="Kasallanganlar: {0}\nBugun kasallanganlar: {1}\nVafot etganlar: {2}\nBugun vafot etganlar: {3}\nSog'ayganlar: {4}\nBugun sog'ayganlar: {5}".format(
    j["Kasallanganlar"],j["Bugun kasallanganlar"],j["Vafot etganlar"],j["Bugun vafot etganlar"],j["Sog'ayganlar"],j["Bugun sog'ayganlar"]
  )
  await m.answer(text)
@dp.message_handler(commands=['uzbekistan'])
async def get_stat2(m: types.Message):
  r=requests.get(url+'uzbekistan')
  j=r.json()
  text="Kasallanganlar: {0}\nBugun kasallanganlar: {1}\nVafot etganlar: {2}\nBugun vafot etganlar: {3}\nSog'ayganlar: {4}\nBugun sog'ayganlar: {5}".format(
    j["Kasallanganlar"],j["Bugun kasallanganlar"],j["Vafot etganlar"],j["Bugun vafot etganlar"],j["Sog'ayganlar"],j["Bugun sog'ayganlar"]
  )
  await m.answer(text)
if __name__=='__main__':
  executor.start_polling(dp,skip_updates=True)
