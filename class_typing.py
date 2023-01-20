class TypingTest:
    """
    Class TypingTest. Contains test attributes:
    :typed_text_list: Typed text as a list
    :type typed_text_list: list

    :target_text_list: Target text as a list
    :type taret_text_list: list

    :compatibility_list: list[inx] is True if typed character is correct
    :type compatibility_list: list

    :correct_chars: Number of correctly typed chars
    :type correct_chars: int

    :correct_chars: Number of correctly typed chars
    :type correct_chars: int

    :wrong_chars: Number of wrongly typed chars
    :type wrong_chars: int

    :time: Duration of the test
    :type time: float

    :wpm: Number of typed words per minute
    :type wpm: int
    
    """
    def __init__(self, target_text: str, typed_text=""):
        self.typed_text_list = [*typed_text]
        self.target_text_list = [*target_text]
        self.compatibility_list = []
        self.correct_chars = 0
        self.wrong_chars = len(target_text)
        self.time = 0
        self.wpm = 0


    def add_remove_char(self, typed_char):
        """
        Method that appends char to typed_text_list or removes it,
        if char is Backspace
        """
        if typed_char == '\b' or typed_char == 'KEY_BACKSPACE':
            if self.typed_text_list:
                if self.check_compatibility():
                    self.correct_chars -= 1
                    self.wrong_chars += 1
                self.typed_text_list.pop()
                self.compatibility_list.pop()

        elif typed_char.isalpha() or typed_char.isdigit() or typed_char in " !@#$%^&*()-_=+;:'\"<>?.,\\`~":
            if len(self.typed_text_list) == len(self.target_text_list):
                pass
            else:
                self.typed_text_list.append(typed_char)
                if self.check_compatibility():
                    self.compatibility_list.append(True)
                    self.correct_chars += 1
                    self.wrong_chars -= 1
                else:
                    self.compatibility_list.append(False)


    def check_compatibility(self):
        """
        Method that checks if typed char is correct
        """
        if self.typed_text_list[-1] == self.target_text_list[len(self.typed_text_list) - 1]:
            return True
        return False
