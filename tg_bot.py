import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7905134738:AAEE9KeyfAERLVHEqD1PssR4Rp1RjHHJQUc'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

FAQ = {
    'Как зарегистрироваться в системе?': '➡️ Перейти на страницу регистрации.\n➡️ Заполнить форму с указанием имени, email и других необходимых данных.\n➡️ Установить пароль.\n➡️ Нажать на кнопку "Зарегистрироваться".\n➡️ После этого на указанный email придет письмо с подтверждением.',
    'Как войти в систему?': '➡️ Перейдите на страницу входа.\n➡️ Введите email и пароль.\n➡️ Если не помните пароль, воспользуйтесь функцией восстановления.',
    'Какие функции доступны на сайте?': 'Основные функции:\n➡️ Просмотр и редактирование данных студентов.\n➡️ Генерация отчетов.\n➡️ Экспорт и импорт данных.\n➡️ Управление учетными записями администраторов.',
    'Как добавить нового студента?': '➡️ Войдите в систему с учетной записью администратора.\n➡️ Перейдите в раздел "Добавить студента".\n➡️ Заполните необходимые поля (ФИО, дата рождения, контактные данные, и т. д.).\n➡️ Сохраните изменения.',
    'Как редактировать данные студента?': '➡️ Найдите нужного студента через поиск.\n➡️ Нажмите "Редактировать" рядом с его записью.\n➡️ Внесите необходимые изменения и сохраните.',
    'Как удалить запись?': '➡️ Найдите студента через поиск.\n➡️ Выберите опцию "Удалить".\n➡️ Подтвердите удаление.\n➡️ Обычно удаление доступно только администраторам.'
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Часто задаваемые вопросы", callback_data='faq')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Я помощник-бот. Выберите действие:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'faq':
        keyboard = [
            [InlineKeyboardButton(q, callback_data=f'faq_{i}')] for i, q in enumerate(FAQ.keys())
        ]
        keyboard.append([InlineKeyboardButton("Назад", callback_data='start')])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Выберите вопрос:", reply_markup=reply_markup)
    elif query.data.startswith('faq_'):
        question_index = int(query.data.split('_')[1])
        question = list(FAQ.keys())[question_index]
        answer = FAQ[question]
        keyboard = [[InlineKeyboardButton("Назад", callback_data='faq')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f'{question}\n\n{answer}', reply_markup=reply_markup)
    elif query.data == 'start':
        await start(update, context)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.warning(f'Update {update} caused error {context.error}')

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_error_handler(error)

    app.run_polling()

if __name__ == '__main__':
    main()