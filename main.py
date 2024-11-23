import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

def translate_to_russian(text=None):
    result = translator.translate(text, dest="ru")
    return result.text


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        # получаем слово и его определение:
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # переводим слово и его определение на русский:
        russian_word = translate_to_russian(english_word)
        russian_definition = translate_to_russian(word_definition)

        # возвращаем словарь
        return {
            "english_word": english_word,
            "word_definition": word_definition,
            "russian_word": russian_word,
            "russian_definition": russian_definition
        }

    except:
        print("Произошла ошибка")
        return None

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()

        russian_word = word_dict.get("russian_word")
        russian_definition = word_dict.get("russian_definition")

        print(f"Значение слова - {russian_definition}")
        user = input(f"Какое это слово на русском?: ")

        if user.lower() == russian_word.lower():  # Игнорируем регистр
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано другое слово - {russian_word}")

        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != "y":  # Игнорируем регистр
            print("Спасибо за игру!")
            break


word_game()
