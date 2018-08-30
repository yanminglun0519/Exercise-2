'''Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

lines = []
i = 0
while i <1:
    sentence = input("Please enter sentence here: ")
    if sentence == '':
        i = 1
    else:
        lines.append(sentence.upper())

for line in lines:
    print(line)

