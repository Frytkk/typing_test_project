class TypingTest:
    def __init__(self, target_text: str, typed_text=""):
        self.typed_text_list = [*typed_text]
        self.target_text_list = [*target_text]
        self.compatibility_list = []
        self.correct_chars = 0
        self.wrong_chars = len(target_text)
        self.time = 0
        self.wpm = 0


    def add_remove_char(self, typed_char):
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
        if self.typed_text_list[-1] == self.target_text_list[len(self.typed_text_list) - 1]:
            return True
        return False
