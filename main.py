import curses
from curses import wrapper, color_pair, init_pair
from time import time
from random import choice
import json


class Result:
    def __init__(self, time, word_number, correct_chars, wrong_chars, wpm):
        self.time = time
        self.word_number = word_number
        self.correct_chars = correct_chars
        self.wrong_chars = wrong_chars
        self.wpm = wpm


def pick_text(word_number):
    with open("target_texts.json") as file:
        all_data = json.load(file)

    target_text = choice(all_data['{}_word_sentence'.format(word_number)])
    return target_text


def home_window(window, results):
    window.erase()
    window.addstr(0, 0, "WELCOME TO THE SPEED TYPING TEST!")
    window.addstr(2, 0, "Press 1 to start the test\n\
Press 2 to see instructions\n\
Press 3 to check your results from the current session\n\
Press 4 to check your all results\n\
Press Q to exit\n\
")
    while True:
        key = window.getkey()
        if key == '1':
            actual_game(window, results)
        elif key == '2':
            instructions(window, results)
        elif key == '3':
            session_results(window, results)
        elif key in ['Q', 'q']:
            quit()


def instructions(window, results):
    window.erase()
    window.addstr(0, 0, "RULES AND FUNCTIONS\n")
    window.addstr(2, 0, "\
After entering the test you can decide on how many words you want to write\n\
Confirm your choice by clicking Enter\n\
This will start a short countdown so that you can prepare for typing\n\
Type as quickly and accurately as possible\n\
You can end the test anytime by clicking Enter\n\
After the test, results will be displayed\n\
")
    window.getkey()
    home_window(window, results)


def choose_words_number(window):
    window.erase()
    window.addstr("TYPE NUMBER OF WORDS (4 - 12)\n")
    curses.echo()
    word_number = window.getstr().decode()

    while True:
        if not word_number.isdigit() or int(word_number) < 4 or int(word_number) > 12:
            window.erase()
            window.addstr("TYPE NUMBER OF WORDS (4 - 12)\n")
            window.addstr(word_number)
            window.addstr(1, 0, word_number + " is not an integer between 4 and 12\n")
            word_number = window.getstr().decode()
        else:
            target_text = pick_text(int(word_number))
            break
    curses.noecho()

    return word_number, target_text


def print_typed_text(window, typed_text_as_list, target_text):

    target_text_list = [*target_text]
    typed_text_list = typed_text_as_list
    typed_text = ""
    all_chars = len(target_text_list)
    wrong_chars = len(target_text_list)
    i = 0

    window.addstr(0, 0, "Start typing when you are ready!")
    window.move(2, 0)
    typing_started = False

    while i <= len(target_text):
        typed_char = window.getkey()
        if not typing_started:
            typing_started = True
            start_time = time()
        if typed_char == 'KEY_BACKSPACE':
            if typed_text_list:
                typed_text_list.pop()
                typed_text = typed_text[:-1]
                i -= 1
                window.erase()
                window.addstr(0, 0, "Start typing when you are ready!")
                window.addstr(1, 0, target_text)
                window.addstr('\n')
        elif typed_char == '\n':
            break
        elif typed_char.isalpha() or typed_char.isdigit() or typed_char in " !@#$%^&*()-_=+;:'\"<>?.,\\`~":
            i += 1
            if i > len(target_text):
                break
            typed_text_list.append(typed_char)
            typed_text += typed_char

        wrong_chars = len(target_text_list)
        for inx, char in enumerate(typed_text_list):
            if char == target_text_list[inx]:
                window.addstr(2, inx, char, color_pair(1))
                wrong_chars -= 1
            else:
                window.addstr(2, inx, char, color_pair(2))

    return all_chars, wrong_chars, start_time


def actual_game(window, results):
    word_number, target_text = choose_words_number(window)

    window.erase()
    window.addstr(0, 0, "Start typing when you are ready!\n")
    window.addstr(1, 0, target_text + "\n")

    all_chars, wrong_chars, start_time = print_typed_text(window, [], target_text)

    typing_time = time() - start_time

    correct_chars = all_chars - wrong_chars
    all_chars = str(all_chars)
    correct_chars = str(correct_chars)
    wrong_chars = str(wrong_chars)

    seconds = "{:.3f}".format(typing_time)
    wpm = "{:.0f}".format(int(word_number) * 60 / typing_time)

    window.addstr(4, 0, f'Time: {seconds} seconds')
    window.addstr(5, 0, 'Keystrokes: {}'.format(all_chars))
    window.addstr(5, len('Keystrokes: {}'.format(all_chars)) + 3, correct_chars, color_pair(1))
    window.addstr(5, len('Keystrokes: {}'.format(all_chars) + correct_chars) + 3, "/")
    window.addstr(5, len('Keystrokes: {}'.format(all_chars) + correct_chars) + 4, wrong_chars, color_pair(2))
    window.addstr(6, 0, f'WPM: {wpm}')
    window.addstr(7, 0, "Enter Esc to end the program or Enter to repeat the test...")

    results.append(Result(seconds, word_number, correct_chars, wrong_chars, wpm))

    key = None

    while key != '^[' or key != '\n' or ord(key) != 27:
        key = window.getkey()
        if key == '\n':
            return actual_game(window, results)
        elif key == '^[' or ord(key) == 27:
            home_window(window, results)


def session_results(window, results):
    window.erase()
    window.addstr("SESSION RESULTS:\n")
    if not results:
        window.addstr(2, 0, "You have played no games yet\n")
    else:
        average_wpm = 0
        correct_chars_sum = sum(int(result.correct_chars) for result in results)
        wrong_chars_sum = sum(int(result.wrong_chars) for result in results)
        all_chars_sum = correct_chars_sum + wrong_chars_sum
        average_accuracy = correct_chars_sum * 100 // all_chars_sum


        for inx, result in enumerate(results):
            window.addstr(inx + 2, 0, f"{inx + 1}. Time: {result.time}\t")
            window.addstr(f"{result.correct_chars}", color_pair(1))
            window.addstr("/")
            window.addstr(f"{result.wrong_chars}\t", color_pair(2))
            window.addstr(f"WPM: {result.wpm}\n")
            average_wpm += int(result.wpm)
        average_wpm //= len(results)
        window.addstr(len(results) + 2, 0, f"Average WPM: {average_wpm}\n")
        window.addstr(f"Average accuracy: {average_accuracy}%\n")
    window.getkey()
    home_window(window, results)

def main(window):
    init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    home_window(window, results=[])


if __name__ == "__main__":
    wrapper(main)
