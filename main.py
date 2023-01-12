import curses
from curses import wrapper
import datetime
from time import sleep
import random


def pick_text():
    pass


def itereate():
    pass


def countcown(window):
    window.addstr(0, 0, "3..")
    window.refresh()
    sleep(1)
    window.addstr(0, 3, "2..")
    window.refresh()
    sleep(1)
    window.addstr(0, 6, "1..\n")
    window.refresh()
    sleep(1)


def print_typed_text(window, target_text, typed_text_list):
    target_text_list = [*target_text]
    i = 0
    while i <= len(target_text):

        for inx, char in enumerate(typed_text_list):
            if char == target_text_list[inx]:
                window.addstr(2, inx, char, curses.color_pair(1))
            else:
                window.addstr(2, inx, char, curses.color_pair(2))

        typed_char = window.getkey()

        if typed_char == 'KEY_BACKSPACE':
            if typed_text_list:
                typed_text_list.pop()
                i -= 1
                window.erase()
                window.addstr(1, 0, target_text)
                window.addstr('\n')
        else:
            typed_text_list.append(typed_char)
            i += 1


def main(window):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    window.clear()

    target_text = "To nie jest koncowy tekst"
    target_text_list = [*target_text]
    typed_text_list = []

    window.addstr(1, 0, target_text)
    window.addstr('\n')
    countcown(window)
    # window.refresh()


    print_typed_text(window, target_text, typed_text_list)

    window.getkey()


if __name__ == "__main__":
    wrapper(main)
