# import logging
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# TOKEN = '7905134738:AAEE9KeyfAERLVHEqD1PssR4Rp1RjHHJQUc'

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# FAQ = {
#     'Как зарегистрироваться в системе?': '➡️ Перейти на страницу регистрации.\n➡️ Заполнить форму с указанием имени, email и других необходимых данных.\n➡️ Установить пароль.\n➡️ Нажать на кнопку "Зарегистрироваться".\n➡️ После этого на указанный email придет письмо с подтверждением.',
#     'Как войти в систему?': '➡️ Перейдите на страницу входа.\n➡️ Введите email и пароль.\n➡️ Если не помните пароль, воспользуйтесь функцией восстановления.',
#     'Какие функции доступны на сайте?': 'Основные функции:\n➡️ Просмотр и редактирование данных студентов.\n➡️ Генерация отчетов.\n➡️ Экспорт и импорт данных.\n➡️ Управление учетными записями администраторов.',
#     'Как добавить нового студента?': '➡️ Войдите в систему с учетной записью администратора.\n➡️ Перейдите в раздел "Добавить студента".\n➡️ Заполните необходимые поля (ФИО, дата рождения, контактные данные, и т. д.).\n➡️ Сохраните изменения.',
#     'Как редактировать данные студента?': '➡️ Найдите нужного студента через поиск.\n➡️ Нажмите "Редактировать" рядом с его записью.\n➡️ Внесите необходимые изменения и сохраните.',
#     'Как удалить запись?': '➡️ Найдите студента через поиск.\n➡️ Выберите опцию "Удалить".\n➡️ Подтвердите удаление.\n➡️ Обычно удаление доступно только администраторам.'
# }

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [
#         [InlineKeyboardButton("Часто задаваемые вопросы", callback_data='faq')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text('Привет! Я помощник-бот. Выберите действие:', reply_markup=reply_markup)

# async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()

#     if query.data == 'faq':
#         keyboard = [
#             [InlineKeyboardButton(q, callback_data=f'faq_{i}')] for i, q in enumerate(FAQ.keys())
#         ]
#         keyboard.append([InlineKeyboardButton("Назад", callback_data='start')])
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         await query.edit_message_text(text="Выберите вопрос:", reply_markup=reply_markup)
#     elif query.data.startswith('faq_'):
#         question_index = int(query.data.split('_')[1])
#         question = list(FAQ.keys())[question_index]
#         answer = FAQ[question]
#         keyboard = [[InlineKeyboardButton("Назад", callback_data='faq')]]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         await query.edit_message_text(text=f'{question}\n\n{answer}', reply_markup=reply_markup)
#     elif query.data == 'start':
#         await start(update, context)

# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     logger.warning(f'Update {update} caused error {context.error}')

# def main():
#     app = Application.builder().token(TOKEN).build()

#     app.add_handler(CommandHandler('start', start))
#     app.add_handler(CallbackQueryHandler(button))
#     app.add_error_handler(error)

#     app.run_polling()

# if __name__ == '__main__':
#     main()




import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes



TOKEN = '7905134738:AAEE9KeyfAERLVHEqD1PssR4Rp1RjHHJQUc'



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)



FAQ_RU = {
    'Как зарегистрироваться в системе?': '➡️ Перейти на страницу регистрации.\n➡️ Заполнить форму с указанием имени, email и других необходимых данных.\n➡️ Установить пароль.\n➡️ Нажать на кнопку "Зарегистрироваться".\n➡️ После этого на указанный email придет письмо с подтверждением.',
    'Как войти в систему?': '➡️ Перейдите на страницу входа.\n➡️ Введите email и пароль.\n➡️ Если не помните пароль, воспользуйтесь функцией восстановления.',
    'Какие функции доступны на сайте?': 'Основные функции:\n➡️ Просмотр и редактирование данных студентов.\n➡️ Генерация отчетов.\n➡️ Экспорт и импорт данных.\n➡️ Управление учетными записями администраторов.',
    'Как добавить нового студента?': '➡️ Войдите в систему с учетной записью администратора.\n➡️ Перейдите в раздел "Добавить студента".\n➡️ Заполните необходимые поля (ФИО, дата рождения, контактные данные, и т. д.).\n➡️ Сохраните изменения.',
    'Как редактировать данные студента?': '➡️ Найдите нужного студента через поиск.\n➡️ Нажмите "Редактировать" рядом с его записью.\n➡️ Внесите необходимые изменения и сохраните.',
    'Как удалить запись?': '➡️ Найдите студента через поиск.\n➡️ Выберите опцию "Удалить".\n➡️ Подтвердите удаление.\n➡️ Обычно удаление доступно только администраторам.'
}

FAQ_KZ = {
    'Жүйеде қалай тіркелуге болады?': '➡️ Тіркеу бетіне өту.\n➡️ Аты-жөнін, электрондық поштаны және басқа қажетті деректерді көрсете отырып, нысанды толтыру.\n➡️ Құпия сөзді орнату.\n➡️ "Тіркелу" түймесін басу.\n➡️ Осыдан кейін көрсетілген электрондық поштаға растау хаты келеді.',
    'Жүйеге қалай кіруге болады?': '➡️ Кіру бетіне өтіңіз.\n➡️ Электрондық поштаны және құпия сөзді енгізіңіз.\n➡️ Егер құпия сөзді есіңізде сақтамасаңыз, қалпына келтіру функциясын пайдаланыңыз.',
    'Сайтта қандай функциялар бар?': 'Негізгі функциялар:\n➡️ Студенттердің деректерін қарау және өңдеу.\n➡️ Есептер генерациясы.\n➡️ Деректерді экспорттау және импорттау.\n➡️ Әкімшілердің есептік жазбаларын басқару.',
    'Жаңа студентті қалай қосуға болады?': '➡️ Әкімші тіркелгісімен жүйеге кіріңіз.\n➡️ "Студент қосу" бөлімін ашыңыз.\n➡️ Қажетті өрістерді толтырыңыз (Аты-жөні, туған күні, байланыс деректері және т. б.).\n➡️ Өзгерістерді сақтаңыз.',
    'Студенттің деректерін қалай өңдеуге болады?': '➡️ Қажетті студентті іздеу арқылы табыңыз.\n➡️ Оның жазбасының жанындағы "Өңдеу" түймесін басыңыз.\n➡️ Қажетті өзгерістерді енгізіңіз және сақтаңыз.',
    'Жазбаны қалай жоюға болады?': '➡️ Студентті іздеу арқылы табыңыз.\n➡️ "Жою" опциясын таңдаңыз.\n➡️ Жоюды растаңыз.\n➡️ Әдетте, жою тек әкімшілерге қолжетімді.'
}



user_language = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data='lang_ru')],
        [InlineKeyboardButton("Қазақша", callback_data='lang_kz')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите язык / Тілді таңдаңыз:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if query.data == 'lang_ru':
        user_language[user_id] = 'ru'
        keyboard = [
            [InlineKeyboardButton("Часто задаваемые вопросы", callback_data='faq')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Выберите действие:", reply_markup=reply_markup)
    elif query.data == 'lang_kz':
        user_language[user_id] = 'kz'
        keyboard = [
            [InlineKeyboardButton("Жиі қойылатын сұрақтар", callback_data='faq')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Әрекетті таңдаңыз:", reply_markup=reply_markup)
    elif query.data == 'faq':
        lang = user_language.get(user_id, 'ru')
        faq = FAQ_RU if lang == 'ru' else FAQ_KZ
        keyboard = [
            [InlineKeyboardButton(q, callback_data=f'faq_{i}')] for i, q in enumerate(faq.keys())
        ]
        keyboard.append([InlineKeyboardButton("Назад", callback_data='start')])
        reply_markup = InlineKeyboardMarkup(keyboard)
        if lang == 'ru':
            await query.edit_message_text(text="Выберите вопрос:", reply_markup=reply_markup)
        else:
            await query.edit_message_text(text="Сұрақты таңдаңыз:", reply_markup=reply_markup)
    elif query.data.startswith('faq_'):
        lang = user_language.get(user_id, 'ru')
        faq = FAQ_RU if lang == 'ru' else FAQ_KZ
        question_index = int(query.data.split('_')[1])
        question = list(faq.keys())[question_index]
        answer = faq[question]
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
