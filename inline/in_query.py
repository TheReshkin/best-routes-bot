from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from routes import railway, avia
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram import InlineQueryResult



def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    print(query)
    results = list()
    reply_markup_1 = InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(text="Пример", url="rzd.ru"),
            ],
        ]
    )

    results.append(
        InlineQueryResultArticle(
            id="avia",
            title="Поиск ЖД билетов",
            input_message_content=InputTextMessageContent(message_text=railway.railway_search(query)),
        )
    )
    results.append(
        InlineQueryResultArticle(
            id="railway",
            title="Поиск авиа билетов",
            input_message_content=InputTextMessageContent(avia.avia_search(query))
        )
    )
    print(update.inline_query.id)
    context.bot.answer_inline_query(update.inline_query.id, results)


inline_caps_handler = InlineQueryHandler(inline_caps)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command.")
