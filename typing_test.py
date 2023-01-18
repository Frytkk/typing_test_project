import curses
from curses import wrapper, color_pair, init_pair
from time import time
from random import choice
import json
from typing_test_class import TypingTest


def pick_text(word_number):
    with open("target_texts.json") as file:
        all_data = json.load(file)

    target_text = choice(all_data['{}_word_sentence'.format(word_number)])
    return target_text


def home_window(window, tests):
    window.erase()
    window.addstr(0, 0, "WELCOME TO THE SPEED TYPING TEST!")
    window.addstr(2, 0, "Please select an option...\n\
1 - start the test\n\
2 - see instructions\n\
3 - check results from the current session\n\
Q - exit\n\
")
    while True:
        key = window.getkey()
        # key = input()
        if key == '1':
            actual_game(window, tests)
        elif key == '2':
            instructions(window, tests)
        elif key == '3':
            session_results(window, tests)
        elif key in ['Q', 'q']:
            quit()


def instructions(window, tests):
    window.erase()
    window.addstr(0, 0, "RULES AND FUNCTIONS\n")
    window.addstr(2, 0, "\
After entering the test you decide how many words you want to type\n\
Confirm your choice by clicking Enter\n\
Time starts counting as soon as you start typing\n\
You can end the test anytime by clicking Enter\n\
After the test, results will be displayed\n\
")
    window.getkey()
    home_window(window, tests)


def choose_words_number(window):
    window.erase()
    window.addstr("TYPE NUMBER OF WORDS (4 - 12)\n")
    curses.echo()

    while True:
        word_number = window.getstr().decode()
        if not word_number.isdigit() or int(word_number) < 4 or int(word_number) > 12:
            window.erase()
            window.addstr("TYPE NUMBER OF WORDS (4 - 12)\n")
            window.addstr(word_number)
            window.addstr(1, 0, word_number + " is not an integer between 4 and 12\n")
        else:
            target_text = pick_text(int(word_number))
            break
    curses.noecho()

    return word_number, target_text


def print_typed_text(window, target_text):

    i = 0
    test = TypingTest(target_text)

    window.addstr(0, 0, "Start typing when you are ready!")
    window.move(3, 0)
    typing_started = False

    while i <= len(target_text):
        typed_char = window.getkey()

        if not typing_started:
            typing_started = True
            start_time = time()

        # end typing when Enter clicked
        if typed_char == '\n':
            break

        # visual part - displays target text
        if typed_char == 'KEY_BACKSPACE':
            if test.typed_text_list:
                i -= 1
                window.erase()
                window.addstr(0, 0, "Start typing when you are ready!")
                window.addstr(2, 0, target_text)
                window.addstr('\n')
        elif typed_char.isalpha() or typed_char.isdigit() or typed_char in " !@#$%^&*()-_=+;:'\"<>?.,\\`~":
            i += 1
            if i > len(target_text):
                break

        # logic part
        test.add_remove_char(typed_char)

        # visual part - displays typed text
        for inx, char in enumerate(test.typed_text_list):
            if test.compatibility_list[inx]:
                window.addstr(3, inx, char, color_pair(1))
            else:
                window.addstr(3, inx, char, color_pair(2))

    return start_time, test


def actual_game(window, tests):
    word_number, target_text = choose_words_number(window)

    window.erase()
    window.addstr(0, 0, "Start typing when you are ready!\n")
    window.addstr(2, 0, target_text + "\n")

    start_time, test = print_typed_text(window, target_text)

    test.time = float(time() - start_time)

    correct_chars = test.correct_chars
    all_chars = str(test.correct_chars + test.wrong_chars)
    correct_chars = str(correct_chars)
    wrong_chars = str(test.wrong_chars)

    seconds = "{:.3f}".format(test.time)
    test.wpm = int(int(word_number) * 60 / test.time)
    wpm = str(test.wpm)


    window.addstr(5, 0, f'Time: {seconds} seconds')
    window.addstr(6, 0, 'Keystrokes: {}'.format(all_chars))
    window.addstr(6, len('Keystrokes: {}'.format(all_chars)) + 3, correct_chars, color_pair(1))
    window.addstr(6, len('Keystrokes: {}'.format(all_chars) + correct_chars) + 3, "/")
    window.addstr(6, len('Keystrokes: {}'.format(all_chars) + correct_chars) + 4, wrong_chars, color_pair(2))
    window.addstr(7, 0, f'WPM: {wpm}')
    window.addstr(8, 0, "Press M to go to main menu or R to repeat the test...")

    tests.append(test)
    key = None

    while key not in ['R', 'r', 'M', 'm']:
        key = window.getkey()
        if key in ['R', 'r']:
            return actual_game(window, tests)
        elif key in ['M', 'm']:
            return home_window(window, tests)


def session_results(window, tests):
    window.erase()
    window.addstr("SESSION RESULTS:\n")
    if not tests:
        window.addstr(2, 0, "You have played no games yet\n")
    else:
        average_wpm = 0
        correct_chars_sum = sum(int(test.correct_chars) for test in tests)
        wrong_chars_sum = sum(int(test.wrong_chars) for test in tests)
        all_chars_sum = correct_chars_sum + wrong_chars_sum
        average_accuracy = correct_chars_sum * 100 // all_chars_sum

        for inx, test in enumerate(tests):
            time = "{:.3f}".format(test.time)
            wpm = "{:.0f}".format(test.wpm)
            window.addstr(inx + 2, 0, f"{inx + 1}. Time: {time}\t")
            window.addstr(f"{test.correct_chars}", color_pair(1))
            window.addstr("/")
            window.addstr(f"{test.wrong_chars}\t", color_pair(2))
            window.addstr(f"WPM: {wpm}\n")
            average_wpm += test.wpm
        average_wpm //= len(tests)
        window.addstr(len(tests) + 2, 0, f"Average WPM: {average_wpm}\n")
        window.addstr(f"Average accuracy: {average_accuracy}%\n")
    window.getkey()
    home_window(window, tests)

def main(window):
    init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    home_window(window, tests=[])


if __name__ == "__main__":
    wrapper(main)
