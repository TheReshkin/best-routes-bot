# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from handlers import currentHandlers

TOKEN = '5172456509:AAGsAV35r223KpjCgxOAhYyew9K9ljbLkD0'




def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)
    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher
    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, currentHandlers.echo)
    # Регистрируем обработчик в диспетчере.

    dp.add_handler(CommandHandler("start", currentHandlers.start))
    dp.add_handler(CommandHandler("help", currentHandlers.help))
    dp.add_handler(CommandHandler("address", currentHandlers.address))
    dp.add_handler(CommandHandler("phone", currentHandlers.phone))
    dp.add_handler(CommandHandler("site", currentHandlers.site))


    dp.add_handler(text_handler)
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()
    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()
    # Запускаем функцию main() в случае запуска скрипта.


if __name__ == '__main__':
    main()
