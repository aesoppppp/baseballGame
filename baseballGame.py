import random

rn = []
for _ in range(3):
    a = random.randint(0, 9)
    while a in rn:
        a = random.randint(0, 9)
    rn.append(a)

# print(rn)

tries = 0
balls = 0
strikes = 0

print("Baseball Game has started!")
print("==========================")

while strikes < 3:
    balls = 0
    strikes = 0

    num = str(input("Guess: "))
    tries += 1

    if len(num) != 3 or len(num) == 0:
        print("Please input only 3 character!")
        tries -= 1

    if len(num) == 3:
        for i in range(0, 3):
            for j in range(0, 3):
                if num[i] == str(rn[j]) and i == j:
                    strikes += 1
                elif num[i] == str(rn[j]) and i != j:
                    balls += 1
        print(f"Result: {strikes} strike, {balls} ball")

print("==========================")
print(f"You've guessed {tries} times before getting 3 strikes")
