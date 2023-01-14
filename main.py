import curses
from curses import wrapper, color_pair, init_pair
from time import time, sleep
from random import choice
import json


def pick_text(word_number):
    with open("target_texts.json") as file:
        all_data = json.load(file)

    target_text = choice(all_data['{}_word_sentence'.format(word_number)])
    return target_text


def countcown(window):
    window.addstr(0, 0, "3..")
    window.move(2, 0)
    window.refresh()
    sleep(1)
    window.addstr(0, 3, "2..")
    window.move(2, 0)
    window.refresh()
    sleep(1)
    window.addstr(0, 6, "1..")
    window.move(2, 0)
    window.refresh()
    sleep(1)
    window.addstr(0, 10, "START")
    window.move(2, 0)
    window.refresh()


def print_typed_text(window, target_text):
    target_text_list = [*target_text]
    typed_text_list = []
    typed_text = ""
    wrong_chars = 0
    all_chars = len(target_text_list)
    i = 0
    while i <= len(target_text):

        for inx, char in enumerate(typed_text_list):
            if char == target_text_list[inx]:
                window.addstr(2, inx, char, color_pair(1))
            else:
                window.addstr(2, inx, char, color_pair(2))
                if i == len(target_text):
                    wrong_chars += 1

        typed_char = window.getkey()

        if typed_char == 'KEY_BACKSPACE':
            if typed_text_list:
                typed_text_list.pop()
                typed_text = typed_text[:-1]
                i -= 1
                window.erase()
                window.addstr(1, 0, target_text)
                window.addstr('\n')
        else:
            typed_text_list.append(typed_char)
            typed_text += typed_char
            i += 1
    return all_chars, wrong_chars

def main(window):
    init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    window.clear()


    window.addstr("TYPE NUMBER OF WORDS (4 - 12)\n")
    curses.echo()
    word_number = window.getstr().decode()

    while True:
        if word_number.isdigit() is False:
            window.erase()
            window.addstr("TYPE NUMBER OF WORDS (4 - 12)\n")
            window.addstr(word_number)
            window.addstr(1, 0, word_number + " is not an integer between 4 and 10\n")
            word_number = window.getstr().decode()
        elif int(word_number) < 4 or int(word_number) > 12:
            window.erase()
            window.addstr("TYPE NUMBER OF WORDS (4 - 12)\n")
            window.addstr(word_number)
            window.addstr(1, 0, word_number + " is not an integer between 4 and 10\n")
            word_number = window.getstr().decode()
        else:
            target_text = pick_text(int(word_number))
            break
    curses.noecho()

    # TUTAJ ZACZYNA SIĘ WYPISYWANIE TARGET TEKSTU I WPISYWANIE WŁASNEGO
    window.erase()
    window.addstr(1, 0, target_text)
    window.addstr('\n')

    countcown(window)
    window.move(2, 0)

    start_time = time()
    all_chars, wrong_chars = print_typed_text(window, target_text)
    typing_time = time() - start_time

    correct_chars = all_chars - wrong_chars
    all_chars = str(all_chars)
    wrong_chars = str(wrong_chars)
    correct_chars = str(correct_chars)

    seconds = "{:.3f}".format(typing_time)
    wpm = "{:.0f}".format(int(word_number) * 60 / typing_time)

    window.addstr(4, 0, f'Time: {seconds} seconds')
    window.addstr(5, 0, 'Keystrokes: {}'.format(all_chars))
    window.addstr(5, len('Keystrokes: {}'.format(all_chars)) + 3, correct_chars, color_pair(1))
    window.addstr(5, len('Keystrokes: {}'.format(all_chars) + correct_chars) + 3, "/")
    window.addstr(5, len('Keystrokes: {}'.format(all_chars) + correct_chars) + 4, wrong_chars, color_pair(2))
    window.addstr(6, 0, f'WPM: {wpm}')
    window.addstr(7, 0, "Enter any key to end the program...")
    window.getkey()


if __name__ == "__main__":
    wrapper(main)
