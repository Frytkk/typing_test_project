import curses
import datetime
import time


def pick_text():
    pass


def itereate():
    pass


def print_typed_text(stdscr, target_text, typed_text_list):
    target_text_list = [*target_text]
    i = 0
    while i <= len(target_text):
        stdscr.refresh()
        # stdscr.addstr(target_text)
        # stdscr.addstr('\n')

        for inx, char in enumerate(typed_text_list):
            if char == target_text_list[inx]:
                stdscr.addstr(1, inx, char, curses.color_pair(1))
            else:
                stdscr.addstr(1, inx, char, curses.color_pair(2))

        typed_char = stdscr.getkey()

        if typed_char == 'KEY_BACKSPACE':
            if typed_text_list:
                typed_text_list.pop()
                i -= 1
                stdscr.clear()
                stdscr.addstr(target_text)
                stdscr.addstr('\n')
        else:
            typed_text_list.append(typed_char)
            i += 1


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.clear()
    target_text = "To nie jest koncowy tekst"
    target_text_list = [*target_text]
    typed_text_list = []

    stdscr.addstr(target_text)
    stdscr.addstr('\n')

    i = 0
    while i <= len(target_text):
        stdscr.refresh()
        # stdscr.addstr(target_text)
        # stdscr.addstr('\n')

        for inx, char in enumerate(typed_text_list):
            if char == target_text_list[inx]:
                stdscr.addstr(1, inx, char, curses.color_pair(1))
            else:
                stdscr.addstr(1, inx, char, curses.color_pair(2))

        typed_char = stdscr.getkey()

        if typed_char == 'KEY_BACKSPACE':
            if typed_text_list:
                typed_text_list.pop()
                i -= 1
                stdscr.clear()
                stdscr.addstr(target_text)
                stdscr.addstr('\n')
        else:
            typed_text_list.append(typed_char)
            i += 1

    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
