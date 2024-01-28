import random
import json
import os
import csv

def generate_random_number():
    return random.randint(1, 10)

def get_player_name():
    name = input("Введите ваше имя: ")
    return name

def print_greeting(name):
    print("Привет, " + name + "! Добро пожаловать в игру не на жизнь, а на смерть!!!!")
    print("Вы очутились в тёмной комнате и видите перед собой Страшное существо")
    print("Вы решаете позвать его")
    print("Тут он резко оборачивается и предлагает игру, в случае победы которой, он вас отпустит")
    print("Он решает задать вам три вопроса")

def play_game():
    player_name = get_player_name()
    print_greeting(player_name)

    questions = [
        "Как зовут самого лучшего преподавателя?)",
        "Сколько пар у нас с ней в неделю?",
        "Сколько бы пар вы хотели с ней?"
    ]

    answers = {
        "Как зовут самого лучшего преподавателя?)": "Татьяна Артамонова",
        "Сколько пар у нас с ней в неделю?": "одна, а хотелось бы больше)",
        "Сколько бы пар вы хотели с ней?": "десять"
    }

    correct_answers = set()

    for question in questions:
        print(question)
        user_answer = input("Введите ответ: ")

        if user_answer.lower() == answers[question].lower():
            print("Правильный ответ, да вы гений!")
            correct_answers.add(question)
        else:
            print("Неправильный ответ, учи уроки, неуч!")

    print("Вы ответили правильно на следующие вопросы:")
    for answer in correct_answers:
        print("- " + answer)

    save_data(player_name, correct_answers)
    save_to_csv()

def save_data(player_name, correct_answers):
    data = {"player_name": player_name, "correct_answers": list(correct_answers)}

    with open("data.json", "a", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False)
        json_file.write("\n")

def delete_data(player_name):
    with open("data.json", "r", encoding="utf-8") as json_file:
        lines = json_file.readlines()

    with open("data.json", "w", encoding="utf-8") as json_file:
        for line in lines:
            saved_data = json.loads(line)
            if saved_data["player_name"] != player_name:
                json.dump(saved_data, json_file, ensure_ascii=False)
                json_file.write("\n")

def save_to_csv():
    with open("data.json", "r", encoding="utf-8") as json_file:
        data = [json.loads(line) for line in json_file]

    with open("data.csv", "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Player Name", "Correct Answers"])

        for entry in data:
            csv_writer.writerow([entry["player_name"], ", ".join(entry["correct_answers"])])

if __name__ == "__main__":
    play_game()
