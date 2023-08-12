from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

load_dotenv()

app = Client(
    'rpabot_helper_bot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
)

@app.on_callback_query()
async def callback(client, callback_query):
    pages = {
        'data': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_2'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='data'),
            'texto': 'Você está na página 1'
        },
        'page_2': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_3'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='data'),
            'texto': 'Você está na página 2'
        },
        'page_3': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='data'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='page_2'),
            'texto': 'Você está na página 3'
        }
    }
    page = pages[callback_query.data]
    await callback_query.edit_message_text(
        page['texto'],
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    page['anterior'], page['proximo']
                ]
            ]
        )
    )


@app.on_message(filters.command('inline'))
async def start_botoes(client, message):
    botoes = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Callback', callback_data='data'),
                InlineKeyboardButton(
                    'Link',
                    url='https://docs.roboteasy.tech/studio/'
                )
            ]
        ]
    )
    await message.reply(
        'Escolha uma opção!',
        reply_markup=botoes,
    )


@app.on_message(filters.command('teclado'))
async def start_teclado(client, message):

    teclado = ReplyKeyboardMarkup(
        [
            ['/ajuda', '/xpto'],
            ['a', 'b', 'c']
        ],
        resize_keyboard=True
    )
    await message.reply(
        'Aperta aí no teclado',
        reply_markup=teclado,
    )

@app.on_message(filters.sticker)
async def help_stickers(client, message):
    await app.send_sticker(
        message.chat.id,
        message.sticker.file_id
    )

@app.on_message(filters.command('photo'))
async def photos(client, message):
    await app.send_photo(
        message.chat.id,
        'https://www.pexels.com/pt-br/foto/inteligencia-artificial-preto-e-branco-p-b-contemporaneo-8294554/'
    )

@app.on_message(~filters.text)
async def help_filters(client, message):
    await message.reply('Desculpe, só consigo interpretar textos 😞.')
@app.on_message(filters.voice | filters.audio)
async def help_voices(client, message):
    await message.reply('Desculpe, não consigo interpretar áudios.')

@app.on_message(filters.command('help'))
async def help(client, message):
    print(message.chat.username, message.text)
    await message.reply('Essa é uma mensagem de ajuda!')

@app.on_message()
async def messages(client, message):
    print(message.chat.username, message.text)
    await message.reply(message.text + '???')

app.run()
