while True:
    import random
    print("this is a yatzy game")
    print("press enter to roll the dice")
    input()
    roll1 = random.randint(1,6)
    if roll1 == 1:
                print("the number you rolled is", roll1)
    if roll1 == 2:
                print("the number you rolled is", roll1)
    if roll1 == 3:
                print("the number you rolled is", roll1)
    if roll1 == 4:
                print("the number you rolled is", roll1)
    if roll1 == 5:
                print("the number you rolled is", roll1)
    if roll1 == 6:
                print("the number you rolled is", roll1)
    roll2 = random.randint(1,6)
    if roll2 == 1:
                print("the number you rolled is", roll2)
    if roll2 == 2:
                print("the number you rolled is", roll2)
    if roll2 == 3:
                print("the number you rolled is", roll2)
    if roll2 == 4:
                print("the number you rolled is", roll2)
    if roll2 == 5:
                print("the number you rolled is", roll2)
    if roll2 == 6:
                print("the number you rolled is", roll2)
    roll3 = random.randint(1,6)
    if roll3 == 1:
                print("the number you rolled is", roll3)
    if roll3 == 2:
                print("the number you rolled is", roll3)
    if roll3 == 3:
                print("the number you rolled is", roll3)
    if roll3 == 4:
                print("the number you rolled is", roll3)
    if roll3 == 5:
                print("the number you rolled is", roll3)
    if roll3 == 6:
                print("the number you rolled is", roll3)

    if roll1 == roll2 == roll3:
        print("YAAAAAAAATZY")

# SHORT VERSION:

while True:
    import random
    print("this is a yatzy game")
    print("press enter to roll the dice")
    input()
    x=random.randint(1,6)
    y=random.randint(1,6)
    z=random.randint(1,6)
    print("The number for the first dice is",x)
    print("The number for the second dice is",y)
    print("The number for the third dice is", z)

    if x == y and x == z and y == z:
        print("YAAAAAAAATZY")