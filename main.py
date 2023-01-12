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

def itereate():
    pass


def countcown(window):
    # window.move(2, 0)
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
    errors = 0
    i = 0
    while i <= len(target_text):

        for inx, char in enumerate(typed_text_list):
            if char == target_text_list[inx]:
                window.addstr(2, inx, char, color_pair(1))
            else:
                window.addstr(2, inx, char, color_pair(2))
                if i == len(target_text):
                    errors += 1


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
    return errors

def main(window):
    init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    window.clear()


    window.addstr("TYPE NUMBER OF WORDS (4 - 10)\n")
    window.addstr(str(word_number := int(window.getstr())))
    if type(word_number) == int:
        target_text = pick_text(word_number)
    else:
        while type(word_number) != int or word_number < 4 or word_number > 10:
            window.addstr("Try one more time\n")
            word_number = window.getstr()
        target_text = pick_text(word_number)


    # TUTAJ ZACZYNA SIĘ WYPISYWANIE TARGET TEKSTU I WPISYWANIE WŁASNEGO
    window.erase()
    window.addstr(1, 0, target_text)
    window.addstr('\n')

    countcown(window)
    window.move(2, 0)
    # window.refresh()
    start_time = time()
    errors = print_typed_text(window, target_text)
    typing_time = time() - start_time
    seconds = "{:.3f}".format(typing_time)
    window.addstr(4, 0, f'Pisanie zajęło ci {seconds} seconds!')
    window.addstr(5, 0, f'You made {errors} mistakes!')
    window.addstr(7, 0, "Enter any key to end the program...")
    window.getkey()


if __name__ == "__main__":
    wrapper(main)
