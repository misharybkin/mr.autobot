def lalala(message):



    if message.text == 'Актуальні вакансії 👷🏻':

        vac = open('vacancy/pierwsza.txt').read()

        inline_markup = types.InlineKeyboardMarkup(row_width=3)
        item1 = types.InlineKeyboardButton(text="Наступна >>", callback_data='nastepna')
        item2 = types.InlineKeyboardButton(text="Подати заявку", callback_data='zayavka')
        inline_markup.add(item1, item2)
        bot.send_message(message.chat.id, vac, parse_mode='html', reply_markup=inline_markup )

        print(vac)

    elif message.text == 'Важливі новини 💼':
        nowinki = open('nowiny.txt').read()
        bot.send_message(message.chat.id, nowinki)
    elif message.text == 'Хочу залишити свої контактні дані ☎️':

        def kolo(message):

            name1 = str(message.text)
            sold = bot.send_message(message.chat.id, "Введіть будь-ласка своє прізвище", reply_markup=otmena)
            open('imie.txt', 'a').write(str(message.text))
            bot.register_next_step_handler(sold, koko)
        def koko(message):
            nb = str(message.text)
            solv = bot.send_message(message.chat.id, "Введіть будь-ласка свій номер телефону")
            open('nazwisko.txt', 'a').write(str(message.text))
            bot.register_next_step_handler(solv, finale)
        def finale(message):
            open('nr_telefonu.txt', 'a').write(str(message.text))

            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            f = open('imie.txt').read()
            k = open('nazwisko.txt').read()

            l = open('nr_telefonu.txt').read()

            c.execute('INSERT INTO Clients(Imie, Nazwisko, Nr_telefonu) VALUES(?, ?, ?)', [f, k, l])

            conn.commit()
            c.execute('SELECT * FROM Clients')
            result1 = c.fetchall()
            print(result1)
            f1 = open('imie.txt', 'w')

            k1 = open('nazwisko.txt', 'w')

            l1 = open('nr_telefonu.txt', 'w')

            conn.close()


            bot.send_message(message.chat.id, "Дякуємо, ми найближчим часом задзвонимо до Вас")

        bot.send_message(message.chat.id, "Введіть будь-ласка своє ім'я")
        bot.register_next_step_handler(message, kolo)
    elif message.text == 'Контакти 📲':
        bot.send_message(message.chat.id, "Наші контакти:\n +48530751503 Василина\n +48530209245 Марія\n +48535477662 Владислав\n +48535624311 Вікторія\n")

    elif message.text == 'Популярні питання 🔓':
        pytania = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton(text="Ваші вакансії безкоштовні?", callback_data='bezkos')
        item2 = types.InlineKeyboardButton(text="Хто звільнений від обсервації?", callback_data='obserwacja')
        item3 = types.InlineKeyboardButton(text="Ви надаєте житло для проходження обсервації?", callback_data='zhytlo')
        item4 = types.InlineKeyboardButton(text="Чи робите ви запрошення для оформлення візи?", callback_data='visa')
        item5 = types.InlineKeyboardButton(text="Cімейні пари живуть окремо?", callback_data='simejni')
        item6 = types.InlineKeyboardButton(text="Чи можу я зробити карту побуту, працюючи на ваших вакансіях?", callback_data='kp')
        item7 = types.InlineKeyboardButton(text="Хочу задати своє питання", callback_data='swoje')
        pytania.add(item1, item2, item3, item4, item5, item6, item7)

        bot.send_message(message.chat.id, "Список популярних питань",  parse_mode='html', reply_markup=pytania)

    elif message.text == 'Охорона персональних даних(RODO) 📐':

        klauzula = open('klauzula.txt').read()
        bot.send_message(message.chat.id, klauzula)
    else:
        bot.send_message(message.chat.id, "Будь-ласка, користуйтесь клавішами:)")

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'otmenit':
                welcome(call.message)

            elif call.data == 'bezkos':
                bot.send_message(call.message.chat.id, "Так, наші вакансії безкоштовні.")
            elif call.data == 'obserwacja':
                kwar = open('kwarantanna.txt').read()
                bot.send_message(call.message.chat.id, kwar )
            elif call.data == 'zhytlo':
                bot.send_message(call.message.chat.id, "Так, надаємо. Ціна - 20 зл/доба. 2 тижнева обсервація коштуватиме близько 300зл. ")

            elif call.data == 'visa':
                bot.send_message(call.message.chat.id, "Так. Ми висилаємо запрошення в будь-яке місто України.")
            elif call.data == 'simejni':
                bot.send_message(call.message.chat.id, "Сімейні пари живуть разом в кімнаті. В кімнаті одночасно живуть дві сімейні пари. ")
            elif call.data == 'kp':
                bot.send_message(call.message.chat.id, "Так, звичайно.")
            elif call.data == 'swoje':
                def pytanko(message):
                    zlyszte = bot.send_message(message.chat.id, "Введіть будь-ласка свій email або номер телефону Telegram.")
                    open('pytanko.txt', 'a').write(str('\n' + message.text))
                    bot.register_next_step_handler(zlyszte, odp)
                def odp(message):
                    bot.send_message(message.chat.id, "Дякуємо! Найближчим часом ми дамо відповідь на Ваше запитання. ")
                    open('pytanko.txt', 'a').write(str('==' + message.text))
                bot.send_message(call.message.chat.id, "Будь-ласка, залиште своє запитання. Наша команда відправить Вам відповідь на email або в приватну бесіду Telegram")
                bot.register_next_step_handler(call.message, pytanko)
            elif call.data == 'nastepna':
                vac1 = open('vacancy/druga.txt').read()

                inlinemarkup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton(text="Наступна >>", callback_data='nastepna')
                item2 = types.InlineKeyboardButton(text="Подати заявку", callback_data='zayavka')
                inlinemarkup.add(item1, item2)
                bot.send_message(call.message.chat.id, vac1, parse_mode='html', reply_markup=inlinemarkup)
            elif call.data == 'zayavka':
                def imia(message):
                    otmena = types.InlineKeyboardMarkup(row_width=4)
                    otmena1 = types.InlineKeyboardButton(text='Відмінити', callback_data='otmenit')
                    otmena.add(otmena1)
                    sold = bot.send_message(message.chat.id, "Введіть будь-ласка своє прізвище", reply_markup=otmena)
                    open('temporary/imie.txt', 'a').write(str('\n' + message.text))


                    bot.register_next_step_handler(sold, familija)
                def familija(message):
                    otmena = types.InlineKeyboardMarkup(row_width=4)
                    otmena1 = types.InlineKeyboardButton(text='Відмінити', callback_data='otmenit')
                    otmena.add(otmena1)
                    bolt = bot.send_message(message.chat.id, "Скільки Вам повних років?", reply_markup=otmena)
                    open('temporary/sirname.txt', 'a').write(str('\n' + message.text))
                    f_read = open('temporary/imie.txt')
                    #last_line = f_read.readlines()[-1]
                    #print(last_line)
                    bot.register_next_step_handler(bolt, age)
                def age(message):
                    otmena = types.InlineKeyboardMarkup(row_width=4)
                    otmena1 = types.InlineKeyboardButton(text='Відмінити', callback_data='otmenit')
                    otmena.add(otmena1)
                    golt = bot.send_message(message.chat.id, "Чи Ви зараз знаходитесь в Польщі?", reply_markup=otmena)
                    open('temporary/lat.txt', 'a').write(str('\n' + message.text))
                    bot.register_next_step_handler(golt, dok)
                def dok(message):
                    variables = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                    karta = types.KeyboardButton("Karta pobytu")
                    wiza = types.KeyboardButton("Wiza sezonowa(6 місяців)")
                    dlug = types.KeyboardButton("Wiza wojewódzka(12 місяців)")
                    bezwiz = types.KeyboardButton("Ruch bezwizowy")
                    variables.add(karta, wiza, dlug, bezwiz)
                    doku = bot.send_message(message.chat.id, "Які у Вас документи?", parse_mode='html', reply_markup=variables)
                    open('temporary/czypolska.txt', 'a').write(str('\n' + message.text))
                    bot.register_next_step_handler(doku, prac)
                def prac(message):

                    zeszla = bot.send_message(message.chat.id, "Скільки часу Ви офіційно працювали у минулого роботодавця(днів)?")
                    open('temporary/dokumenty.txt', 'a').write('\n' + str(message.text))
                    bot.register_next_step_handler(zeszla, tel)
                def tel(message):
                    telef = bot.send_message(message.chat.id, "Залиште будь-ласка свій номер телефону. \n Ми скоро сконтактуємось з Вами для уточнення деталей:) ")
                    open('temporary/zeszla_praca.txt', 'a').write('\n' + str(message.text))
                    bot.register_next_step_handler(telef, finalic)
                def finalic(message):
                    bot.send_message(message.chat.id, "Дякуємо за Ваш інтерес! Ми проаналізуємо Ваші дані і скоро звяжемось з Вами!")
                    open('temporary/numer_telefon.txt', 'a').write('\n' + str(message.text))
                    connection = sqlite3.connect('database.db')
                    c = connection.cursor()
                    open('date.txt', 'a').write('\n' + str(message.date))
                    a1 = open('temporary/imie.txt')
                    a1_last = a1.readlines()[-1]
                    b1 = open('temporary/sirname.txt')
                    b1_last = b1.readlines()[-1]
                    c1 = open('temporary/lat.txt')
                    c1_last = c1.readlines()[-1]
                    d1 = open('temporary/czypolska.txt')
                    d1_last = d1.readlines()[-1]
                    f1 = open('temporary/dokumenty.txt')
                    f1_last = f1.readlines()[-1]
                    g1 = open('temporary/zeszla_praca.txt')
                    g1_last = g1.readlines()[-1]
                    h1 = open('temporary/numer_telefon.txt')
                    h1_last = h1.readlines()[-1]
                    c.execute('INSERT INTO Analiza(Imie, Nazwisko, Ile_lat, Czy_w_polsce, Dokumenty, Zeszla_praca, Nr_telefonu) VALUES(?, ?, ?, ?, ?, ?, ?)', [a1_last, b1_last, c1_last, d1_last, f1_last, g1_last, h1_last])

                    connection.commit()
                    connection.close()


                bot.send_message(call.message.chat.id, "Введіть будь-ласка своє ім'я")
                bot.register_next_step_handler(call.message, imia)
    except Exception as e:
            print(repr(e))

