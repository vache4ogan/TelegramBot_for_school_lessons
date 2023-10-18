import asyncio
import logging
import os

from aiogram import Dispatcher, types, Bot

import database
from config import token

database.init()
database.show()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    database.insert(message.from_user.id, message.from_user.username)
    database.commit()
    database.show()
    await message.answer(
        'Привет! Я телеграмм бот для Тлянче-Тамакской СОШ. Я буду каждое утро отправлять тебе измененное расписание')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    if message.from_user.id == 5447182412 or message.from_user.id == 2053394555:
        try:
            # Сохранение фото
            photo_id = message.photo[-1].file_id
            photo = await bot.get_file(photo_id)
            await photo.download(f'{photo_id}.jpg')
        except:
            await message.answer('Ошибка, я принимаю только фото расписания')

        all1 = database.id_for_ras()
        print('ok')
        for row in all1:
            print(row)
            print(row[0])
            try:
                await bot.send_photo(chat_id=row[0], photo=str(photo_id))
            except:
                print('error')
        try:
            os.remove(path=f'{photo_id}.jpg')
        except:
            pass
        await message.answer('Отправлено')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def message(message: types.Message):
    if message.from_user.id == '5447182412':
        try:
            all1 = database.id_for_ras()
            for row in all1:
                await bot.send_message(chat_id=row[0], text=message.text)

            await message.answer(f'Сообщение "{message.text}" было успешно отправлено, всем')
        except:
            pass
    else:
        database.insert(message.from_user.id, message.from_user.username)
        database.commit()
        database.show()
        await message.answer('Ученики мне писать не могут ((')


async def main():
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
