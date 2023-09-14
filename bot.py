#Zaimportowane biblioteki
import telebot
import config
from telebot import types
import sqlite3

from abc import ABC, abstractmethod

#Odnosnik do pliku z tokenem botu
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
#Metoda, definiująca powitanie użytkownika po kliknięciu przycisku /start
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(" Ogłoszenia ⚙️")
    item4 = types.KeyboardButton("Ważne wiadomości 💼")
    item5 = types.KeyboardButton("Ochrona danych osobowych(RODO) 📐")
    item2 = types.KeyboardButton("Kontakty 📲")
    item3 = types.KeyboardButton("Popularne pytania 🔓")
    markup.add(item1, item2, item3, item5, item4)

    bot.send_message(message.chat.id, "Witamy! Proszę wybrać interesującą usługę!", parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
#Metoda, definiująca wszystkie istniejące przyciski menu niekontekstowego
def lalala(message):
	if message.text == 'Ogłoszenia ⚙️':
		oglosenie = Ogloszenia()
		oglosenie.main(message)
	
	elif message.text == 'Audi🇩🇪':
		audi = Audi()
		audi.audi_action(message)

	elif message.text == 'Koła Audi🛞':
		audikol = Audi()
		audikol.audi_kolesa(message)

	elif message.text == 'Tarcze hamulcowe Audi🔩':
		auditorm = Audi()
		auditorm.audi_tormdyski(message)

	elif message.text == 'Części silnika Audi 🏎':
		audieng = Audi()
		audieng.audi_dvigatel(message)

	elif message.text == 'Inne części zamienne Audi 🚨':
		audiinne = Audi()
		audiinne.audi_inne(message)

	elif message.text == 'Volkswagen🇩🇪':
		volks = Volkswagen()
		volks.first_action(message)

	elif message.text == 'Koła Volkswagen🛞':
		volkskol = Volkswagen()
		volkskol.kolesa(message)

	elif message.text == 'Tarcze hamulcowe Volkswagen🔩':
		volkstorm = Volkswagen()
		volkstorm.torm_dyski(message)

	elif message.text == 'Części silnika Volkswagen 🏎':
		volkseng = Volkswagen()
		volkseng.dvigatel(message)

	elif message.text == 'Inne części zamienne Volkswagen 🚨':
		volksinne = Volkswagen()
		volksinne.inne(message)

	elif message.text == 'Seat🇪🇸':
		seat = Seat()
		seat.first_action(message)

	elif message.text == 'Koła Seat🛞':
		seatkol = Seat()
		seatkol.kolesa(message)

	elif message.text == 'Tarcze hamulcowe Seat🔩':
		seattorm = Seat()
		seattorm.torm_dyski(message)

	elif message.text == 'Części silnika Seat 🏎':
		seateng = Seat()
		seateng.dvigatel(message)

	elif message.text == 'Inne części zamienne Seat 🚨':
		seatinne = Seat()
		seatinne.inne(message)

	elif message.text == 'Ferrari🇮🇹':
		ferrari = Ferrari()
		ferrari.first_action(message)

	elif message.text == 'Koła Ferrari🛞':
		ferrarikol = Ferrari()
		ferrarikol.kolesa(message)

	elif message.text == 'Tarcze hamulcowe Ferrari🔩':
		ferraritorm = Ferrari()
		ferraritorm.torm_dyski(message)

	elif message.text == 'Części silnika Ferrari 🏎':
		ferrarieng = Ferrari()
		ferrarieng.dvigatel(message)

	elif message.text == 'Inne części zamienne Ferrari 🚨':
		ferrariinne = Ferrari()
		ferrariinne.inne(message)

	elif message.text == 'Skoda🇨🇿':
		skoda = Skoda()
		skoda.first_action(message)

	elif message.text == 'Koła Skoda🛞':
		skodakol = Skoda()
		skodakol.kolesa(message)

	elif message.text == 'Tarcze hamulcowe Skoda🔩':
		skodatorm = Skoda()
		skodatorm.torm_dyski(message)

	elif message.text == 'Części silnika Skoda 🏎':
		skodaeng = Skoda()
		skodaeng.dvigatel(message)

	elif message.text == 'Inne części zamienne Skoda 🚨':
		skodainne = Skoda()
		skodainne.skoda_inne(message)

	elif message.text == 'Kontakty 📲':
		cont = Contacts()
		cont.send(message)

	elif message.text == 'Popularne pytania 🔓':
		quest = Questions()
		quest.send(message)

	elif message.text == 'Ważne wiadomości 💼':
		newsletter = News()
		newsletter.send(message)

	elif message.text == 'Ochrona danych osobowych(RODO) 📐':
		rodo = Rodo()
		rodo.send(message)

	elif message.text == 'Wróć do ekranu początkowego':
		welcome(message)

	else:
		bot.send_message(message.chat.id, "Nie rozumiem tego polecenia lub ta sekcja jest wciąż w fazie rozwoju.")


class QuickSender(ABC):
	@abstractmethod
	@bot.message_handler(content_types=['text'])
	def send(self, message):
		pass


#Definicja klas, dedykowanych dla każdej kategorii
class Rodo(QuickSender):
	@bot.message_handler(content_types=['text'])
	def send(self, message):
		rodo = open('rodo/rodo.txt').read()
		bot.send_message(message.chat.id, rodo)	

class Questions(QuickSender):
	@bot.message_handler(content_types=['text'])
	def send(self, message):
		questions = open('questions/questions.txt').read()
		bot.send_message(message.chat.id, questions)

class News(QuickSender):
	@bot.message_handler(content_types=['text'])
	def send(self, message):
		newspaper = open('news/news.txt').read()
		bot.send_message(message.chat.id, newspaper)

class Contacts(QuickSender):
	@bot.message_handler(content_types=['text'])
	def send(self, message):
		bot.send_message(message.chat.id, "Nasze kontakty: Мykhailo, +48 796 732 788, ul. Wzorcowa 1, m. Warszawa")

class Ogloszenia:
	@bot.message_handler(content_types=['text'])
	def main(self, message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Audi🇩🇪")
		item2 = types.KeyboardButton("Volkswagen🇩🇪")
		item3 = types.KeyboardButton("Seat🇪🇸")
		item4 = types.KeyboardButton("Skoda🇨🇿")
		item5 = types.KeyboardButton("Ferrari🇮🇹")
		markup.add(item1, item2, item3, item5, item4)
		bot.send_message(message.chat.id, "Wybierz markę samochodu 🚘", parse_mode='html', reply_markup=markup)



#definicja klasy abstrakcyjnej dla każdego modelu auta
class Auto(ABC):
	@abstractmethod
	@bot.message_handler(content_types=['text'])
	#definicja metody która będzie tzw. ekranem powitalnym
	def first_action(self, message):
		pass
	#definicja metody która będzie zwracała listę sprzedawanych kół dla każdej marki samochodów
	def kolesa(self, message):
		pass
	#definicja metody która będzie zwracała listę sprzedawanych silników dla każdej marki samochodów
	def dvigatel(self, message):
		pass
	def torm_dyski(self, message):
		pass
	def inne(self, message):
		pass


#W pełni zaimplementowane
class Volkswagen(Auto):
	@bot.message_handler(content_types=['text'])
	def first_action(self, message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Koła Volkswagen🛞")
		item2 = types.KeyboardButton("Tarcze hamulcowe Volkswagen🔩")
		item3 = types.KeyboardButton("Części silnika Volkswagen 🏎")
		item4 = types.KeyboardButton("Inne części zamienne Volkswagen 🚨")
		item5 = types.KeyboardButton("Wróć do ekranu początkowego")
		markup.add(item1, item2, item3, item4, item5)
		bot.send_message(message.chat.id, "Wybierz kategorię części zamiennych:", parse_mode='html', reply_markup=markup)
		print ("Metoda wywoływana!")

	@bot.message_handler(content_types=['text'])
	def kolesa(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 5')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			inline_markup.add(item2, item1)
			message_w = f"ID: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		#list_volkswagen_kolesa = open('volkswagen/kolesa/kolesa.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_volkswagen_kolesa, parse_mode='html', reply_markup=inline_markup)	

	@bot.message_handler(content_types=['text'])
	def torm_dyski(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 6')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2, item1)
			message_w = f"ID: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()
		#list_volkswagen_tormdyski = open('volkswagen/torm_dyski.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_volkswagen_tormdyski, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def dvigatel(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 7')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			inline_markup.add(item2,item1)
			message_w = f"ID: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()
		#list_volkswagen_dvigatel = open('volkswagen/dvigatel.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_volkswagen_dvigatel, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def inne(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 8')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2,item1)
			message_w = f"ID: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()

		#list_volkswagen_inne = open('volkswagen/inne.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_volkswagen_inne, parse_mode='html', reply_markup=inline_markup )

class Skoda(Auto):
	@bot.message_handler(content_types=['text'])
	def first_action(self, message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Koła Skoda🛞")
		item2 = types.KeyboardButton("Tarcze hamulcowe Skoda🔩")
		item3 = types.KeyboardButton("Części silnika Skoda 🏎")
		item4 = types.KeyboardButton("Inne części zamienne Skoda 🚨")
		item5 = types.KeyboardButton("Wróć do ekranu początkowego")
		markup.add(item1, item2, item3, item4, item5)
		bot.send_message(message.chat.id, "Wybierz kategorię części zamiennych:", parse_mode='html', reply_markup=markup)
		print ("Metoda wywoływana!")

	@bot.message_handler(content_types=['text'])
	def kolesa(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 13')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2)
			message_w = f"ID: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()
		#bot.send_message(message.chat.id, list_skoda_kolesa, parse_mode='html', reply_markup=inline_markup )
		#list_skoda_kolesa = open('skoda/kolesa/kolesa.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_skoda_kolesa, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def torm_dyski(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 14')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2)
			message_w = f"ID: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()


		#list_skoda_tormdyski = open('skoda/torm_dyski.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_skoda_tormdyski, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def dvigatel(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 15')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2)
			message_w = f"ID: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()

		#list_skoda_dvigatel = open('skoda/dvigatel.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_skoda_dvigatel, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def inne(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 16')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()


		#list_skoda_inne = open('skoda/inne.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_skoda_inne, parse_mode='html', reply_markup=inline_markup )


class Ferrari(Auto):
	@bot.message_handler(content_types=['text'])
	def first_action(self, message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Koła Ferrari🛞")
		item2 = types.KeyboardButton("Tarcze hamulcowe Ferrari🔩")
		item3 = types.KeyboardButton("Części silnika Ferrari 🏎")
		item4 = types.KeyboardButton("Inne części zamienne Ferrari 🚨")
		item5 = types.KeyboardButton("Wróć do ekranu początkowego")
		markup.add(item1, item2, item3, item4, item5)
		bot.send_message(message.chat.id, "Wybierz kategorię części zamiennych:", parse_mode='html', reply_markup=markup)
		print ("Metoda wywoływana!")

	@bot.message_handler(content_types=['text'])
	def kolesa(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 17')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()

		#list_ferrari_kolesa = open('ferrari/kolesa/kolesa.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_ferrari_kolesa, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def torm_dyski(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 18')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()

		#list_ferrari_tormdyski = open('ferrari/torm_dyski.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_ferrari_tormdyski, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def dvigatel(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 19')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()

		#list_ferrari_dvigatel = open('ferrari/dvigatel.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_ferrari_dvigatel, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def inne(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 20')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()

		#list_ferrari_inne = open('ferrari/inne.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_ferrari_inne, parse_mode='html', reply_markup=inline_markup )

#W pełni zaimplementowany
class Seat(Auto):
	@bot.message_handler(content_types=['text'])
	def first_action(self, message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Koła Seat🛞")
		item2 = types.KeyboardButton("Tarcze hamulcowe Seat🔩")
		item3 = types.KeyboardButton("Części silnika Seat 🏎")
		item4 = types.KeyboardButton("Inne części zamienne Seat 🚨")
		item5 = types.KeyboardButton("Wróć do ekranu początkowego")
		markup.add(item1, item2, item3, item4, item5)
		bot.send_message(message.chat.id, "Wybierz kategorię części zamiennych:", parse_mode='html', reply_markup=markup)
		print ("Metoda wywoływana!")

	@bot.message_handler(content_types=['text'])
	def kolesa(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 10')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2, item1)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		#list_seat_kolesa = open('seat/kolesa/kolesa.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_seat_kolesa, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def torm_dyski(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 21')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2,item1)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()
		#list_volkswagen_tormdyski = open('seat/torm_dyski.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_seat_tormdyski, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def dvigatel(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 11')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2,item1)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()
		#list_seat_dvigatel = open('seat/dvigatel.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_seat_dvigatel, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def inne(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 12')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2,item1)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()
		#list_seat_inne = open('seat/inne.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_seat_inne, parse_mode='html', reply_markup=inline_markup )

#Klasa Audi w pełni zrealizowana
class Audi:
	@bot.message_handler(content_types=['text'])
	def audi_action(self, message):
		
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Koła Audi🛞")
		item2 = types.KeyboardButton("Tarcze hamulcowe Audi🔩")
		item3 = types.KeyboardButton("Części silnika Audi 🏎")
		item4 = types.KeyboardButton("Inne części zamienne Audi 🚨")
		item5 = types.KeyboardButton("Wróć do ekranu początkowego")
		markup.add(item1, item2, item3, item4, item5)
		bot.send_message(message.chat.id, "Wybierz kategorię części zamiennych:", parse_mode='html', reply_markup=markup)
		print ("Metoda wywoływana!")

	@bot.message_handler(content_types=['text'])
	def audi_kolesa(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 1')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2,item1)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		#list_audi_kolesa = open('audi/kolesa/kolesa.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=4)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)s
		#bot.send_message(message.chat.id, list_audi_kolesa, parse_mode='html', reply_markup=inline_markup )
		#bot.send_message(message.chat.id, list_audi_kolesa, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def audi_tormdyski(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 2')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2, item1)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)

		#Poniżej przedstawiona jest metoda, wykorzystana przed implementacją bazy danych
		#list_audi_tormdyski = open('audi/torm_dyski.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_audi_tormdyski, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def audi_dvigatel(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 3')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2,item1)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()
		#list_audi_dvigatel = open('audi/dvigatel.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_audi_dvigatel, parse_mode='html', reply_markup=inline_markup )

	@bot.message_handler(content_types=['text'])
	def audi_inne(self, message):
		conn = sqlite3.connect('autobot_pl.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM Artykuly WHERE PodkategoriaID = 4')
		rows = cursor.fetchall()
		for row in rows:
			inline_markup = types.InlineKeyboardMarkup(row_width=3)
			item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
			inline_markup.add(item2)
			message_w = f"Identyfikator: {row[0]}\nNazwa: {row[1]}\nIlosc: {row[2]}\nPodkategoriaID: {row[3]}\nCena: {row[4]}"
			bot.send_message(message.chat.id, message_w,  parse_mode='html', reply_markup=inline_markup)
		conn.close()
		#list_audi_inne = open('audi/inne.txt').read()
		#inline_markup = types.InlineKeyboardMarkup(row_width=3)
		#item1 = types.InlineKeyboardButton(text="Wróć do początku", callback_data='back_kolesa')
		#item2 = types.InlineKeyboardButton(text="Zawnioskuj", callback_data='zayavka')
		#inline_markup.add(item1, item2)
		#bot.send_message(message.chat.id, list_audi_inne, parse_mode='html', reply_markup=inline_markup )


#Niżej przedstawione są metody pobierania danych od użytkowników

def get_client_info(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Proszę podać imię:")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    chat_id = message.chat.id
    imie = message.text
    bot.send_message(chat_id, "Proszę podać nazwisko:")
    bot.register_next_step_handler(message, get_phone_number, imie=imie)

def get_phone_number(message, imie):
    chat_id = message.chat.id
    nazwisko = message.text
    bot.send_message(chat_id, "Proszę podać numer telefonu:")
    bot.register_next_step_handler(message, get_email, imie=imie, nazwisko=nazwisko)

def get_email(message, imie, nazwisko):
    chat_id = message.chat.id
    nr_telefonu = message.text
    bot.send_message(chat_id, "Proszę podać adres e-mail:")
    bot.register_next_step_handler(message, process_client_info, imie=imie, nazwisko=nazwisko, nr_telefonu=nr_telefonu)

def process_client_info(message, imie, nazwisko, nr_telefonu):
	chat_id = message.chat.id
	email = message.text
	conn = sqlite3.connect('autobot_pl.db')
	print("Connection established")
	c = conn.cursor()

    # Додаємо клієнта до бази даних
	c.execute("INSERT INTO Klienci (Imie, Nazwisko, Nr_telefonu, Email) VALUES (?, ?, ?, ?)",
              (imie, nazwisko, nr_telefonu, email))
	KlientID = c.lastrowid


    # Зберігаємо зміни у базі даних
	conn.commit()
	conn.close()
	bot.send_message(chat_id, "Użytkownik zarejestrowany!")
	get_order_info(message)


def get_order_info(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Proszę podać identyfikator ogłoszenia:")
    bot.register_next_step_handler(message, get_klientid)

def get_klientid(message):
    chat_id = message.chat.id
    zamowienie_id = message.text
    bot.send_message(chat_id, "Proszę podać ilosc żądanych sztuk produktu:")
    bot.register_next_step_handler(message, get_ilosc, zamowienie_id=zamowienie_id)

def get_ilosc(message, zamowienie_id):
	chat_id = message.chat.id
	conn = sqlite3.connect('autobot_pl.db')
	print("Connection established")
	c = conn.cursor()
	c.execute("SELECT KlientID FROM Klienci ORDER BY KlientID DESC LIMIT 1")
	klient_id = c.fetchall()[0][0]
	print(klient_id)
	bot.send_message(chat_id, "Twoje zamówienie zarejestrowane! Wkrótce do Ciebie oddzwonimy")
	bot.register_next_step_handler(message, process_order, zamowienie_id=zamowienie_id, klient_id=klient_id)



def process_order(message, zamowienie_id, klient_id):
	chat_id = message.chat.id
	ilosc = message.text
	conn = sqlite3.connect('autobot_pl.db')
	#print("Connection established")
	c = conn.cursor()

    # 
	#c.execute("INSERT INTO Klienci (Imie, Nazwisko, Nr_telefonu, Email) VALUES (?, ?, ?, ?)",
     #         (imie, nazwisko, nr_telefonu, email))
	#KlientID = c.lastrowid

	c.execute("INSERT INTO Zamowienia(ArtykulID, KlientID, Ilosc) VALUES(?, ?, ?)",
			(zamowienie_id, klient_id, ilosc))
	ZamowienieID = c.lastrowid


    # Зберігаємо зміни у базі даних
	conn.commit()
	conn.close()
	bot.send_message(chat_id, "Zamowienie złożone! Wkrótce do Ciebie oddzwonimy")

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'zayavka':
				get_client_info(call.message)
				
			if call.data == 'back_kolesa':
				welcome(call.message)
	except Exception as e:
            print(repr(e))




		
		




	







bot.polling(none_stop = True)
