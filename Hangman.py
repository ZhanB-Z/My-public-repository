import random
import re
import string

with open("words.txt", "r") as file:
    allwords = file.read()
    splitwords = allwords.split()
    print(splitwords)

w = random.choice(splitwords)
s = []
x = 10
f = 0
print(w)
print(len(w))

CORRECT = True

len_s = len(s)
len_w = len(w)

#print ****** for the start
while len(s) < len_w:
    s.append("*")
print(s)

alphabet_string = string.ascii_uppercase
alphabet = list(alphabet_string)
print(alphabet)

def main():
    a = input("Choose a letter: ").upper()
    if not a in alphabet:
        print(f"The letter {a} has already been used. Chose another one!")
    global x
    f = 0
    for i in w:
        if i == a:
            s[f] = a
            f += 1
        else:
            f += 1
            

    if list(w) == s:
        print(s)
        print("You survived! Good job!")
        exit()

    if a in w:
        print("Good job")
        print(s)
        print(f"You have {x} more chances")
        try:
            alphabet.remove(a)
        except:
            pass
    else:
        x -= 1
        print(f"Wrong! You have {x} more chances")
        print(s)
        try:
            alphabet.remove(a)
        except:
            pass


    while x > 0:
        print("Next round")
        main()

    if x == 0:
        print("GAME OVER")
        print(f"The word was {w}")
        exit()


if __name__ == '__main__':
    main()


