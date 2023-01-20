# Speed typing test - project description

## Purpose and description of the project:

The purpose of the project is to implement a typing test. Users should be able to decide on how many words they want to type. While typing, characters should be colored, depending on the correctness of the entered text. After the test, there should be displayed basic stats, including the number of typed characters - correct and wrong ones, and typed words per minute - WPM.

## Program structure:
1. class_typing.py - file with the most relevant code of the whole project. It contains a TypingTest class that stores all information about the current test. It is able to add or remove characters, check the correctness of the typed text and count basic stats.

2. test_class_typing.py - file that checks every aspect of the class_typing.py file. It tests all logic functions and ensures that all functions and methods work properly.

3. typing_test.py - file containing interface of the project. It displays data in real time with no delay, letting users type a number of words they want to type, coloring typed text and showing test’s stats. The program also allows users to see the results of all tests performed in one session.

4. target_texts.json - file with over 2000 sentences that differ in length. Minimal length of a sentence is 4 words and maximum is 12 words. User chooses a specific length and a random sentence is drawn.

## Instruction:

The program works correctly on Unix-like systems (it contains a curses library that is only supported on that kind of system). The easiest way to open the program is to go to the directory consisting of program files in the Terminal and type:
>“python3 typing_test.py”

## Reflective part:

The above project is a diverse project that required different skills. The basic one was the knowledge of object-oriented programming, which allowed for uncomplicated testing, and at the same time ensured easy familiarization with the program. In addition, the program uses files of different formats, so this issue also had to be dealt with. However, the program wouldn't be complete without the visual aspects that were designed to look nice and be comfortable to use. Everything that was indicated in the program description was implemented, considering the project as complete.




