from typing_test_class import TypingTest


def test_add_char():
    test1 = TypingTest("Ala ma kota")

    test1.add_remove_char('A')
    assert test1.typed_text_list == ['A']
    assert test1.correct_chars == 1
    assert test1.wrong_chars == 10


def test_add_multiple_chars():
    test1 = TypingTest("Ala ma kota")

    test1.add_remove_char('A')
    test1.add_remove_char('l')
    test1.add_remove_char('a')
    test1.add_remove_char(' ')
    assert test1.typed_text_list == ['A', 'l', 'a', ' ']
    assert test1.correct_chars == 4
    assert test1.wrong_chars == 7


def test_add_correct_text():
    test1 = TypingTest("Ala ma kota")
    typed_text = ""

    test1.add_remove_char('A')
    test1.add_remove_char('l')
    test1.add_remove_char('a')
    test1.add_remove_char(' ')
    test1.add_remove_char('m')
    test1.add_remove_char('a')
    test1.add_remove_char(' ')
    test1.add_remove_char('k')
    test1.add_remove_char('o')
    test1.add_remove_char('t')
    test1.add_remove_char('a')
    assert test1.typed_text_list == ['A', 'l', 'a', ' ', 'm', 'a', ' ', 'k', 'o', 't', 'a']
    typed_text = typed_text.join(test1.typed_text_list)
    assert typed_text == "Ala ma kota"
    assert test1.correct_chars == 11
    assert test1.wrong_chars == 0


def test_remove_char():
    test1 = TypingTest("Ala ma kota")
    test1.add_remove_char('A')
    test1.add_remove_char('l')
    test1.add_remove_char('a')
    test1.add_remove_char('\b')
    assert test1.typed_text_list == ['A', 'l']
    test1.add_remove_char('KEY_BACKSPACE')
    assert test1.typed_text_list == ['A']


def test_add_not_allowed_char():
    test1 = TypingTest("Ala ma kota")

    test1.add_remove_char('A')
    test1.add_remove_char('l')
    test1.add_remove_char('a')
    test1.add_remove_char('}')
    test1.add_remove_char('{')
    assert test1.typed_text_list == ['A', 'l', 'a']
    assert test1.correct_chars == 3
    assert test1.wrong_chars == 8


def test_add_over_target():
    test1 = TypingTest("al a")
    test1.add_remove_char('A')
    test1.add_remove_char('l')
    test1.add_remove_char(' ')
    test1.add_remove_char('l')
    test1.add_remove_char('a')
    assert len(test1.typed_text_list) == 4
    assert test1.typed_text_list == ['A', 'l', ' ', 'l']
    assert test1.correct_chars == 2
    assert test1.wrong_chars == 2


def test_compatibility_1():
    test1 = TypingTest("kot")
    test1.add_remove_char('K')
    test1.add_remove_char('o')
    test1.add_remove_char(' ')
    assert test1.compatibility_list == [False, True, False]


def test_compatibility_2():
    test1 = TypingTest("Ala ma kota")

    test1.add_remove_char('A')
    test1.add_remove_char('l')
    test1.add_remove_char('a')
    test1.add_remove_char('}')
    test1.add_remove_char('{')
    assert test1.typed_text_list == ['A', 'l', 'a']
    assert test1.compatibility_list == [True, True, True]


def test_compatibility_3():
    test1 = TypingTest("Ala ma kota")
    test1.add_remove_char('A')
    test1.add_remove_char('l')
    test1.add_remove_char('a')
    test1.add_remove_char(' ')
    test1.add_remove_char('\b')
    test1.add_remove_char('\b')
    test1.add_remove_char(' ')
    test1.add_remove_char('k')
    test1.add_remove_char('\b')
    test1.add_remove_char('t')
    test1.add_remove_char('\b')
    assert test1.typed_text_list == ['A', 'l', ' ']
    assert test1.compatibility_list == [True, True, False]
