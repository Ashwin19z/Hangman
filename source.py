import random
print("WELCOME TO HANGMAN !!".center(50))
R=(random.choice(open('words.txt','r').read().split("\n")))
b=[" _ " for i in R]
print("\nW O R D ==","".join(b))
life=[   """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    LIFE = 0""",
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    LIFE = 1""",
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    LIFE = 2""",
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    LIFE = 3""",
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    LIFE = 4""",
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    LIFE = 5""",
     """
     -----
     |   |
         |
         |
         |
         |
    --------
    LIFE = 6"""]
c=6
while c>0:
    g=input("%s \n Enter Your Guess:" % life[c]).upper()
    if g in R:
        print("\n %s is in the word" %g)
        b=[" _ " if i != g and i not in b else i for i in R]
        print("\nW O R D ==","".join(b))
        if " _ " not in b:
            print("\n\nYOU WON!! ".center(50),life[c])
            break
    else:
        c -= 1
        print("\n %s is not in the word" %g)
        print("\nW O R D ==","".join(b))
        if c == 0:
            print("\n\nYOU LOST!! ".center(50),life[c])
            print("\n The word was: %s \n\n" % R)
            break
print("\n\nTHANK YOU FOR PLAYING HANGMAN!!".center(50))   