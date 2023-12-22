import random as rnd

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def verifyDivide(min,max):
    list = []
    for i in range(min, max//2):
        if i == 1:
            continue
        for j in range(min, max//2):
            j = max -j
            if j%i == 0:
                list.append([j,i])
    return list


def check_answer(a,b):
    return True if a==b else False

def setDificultyRange(level, range):
    return [(level*range)-range+1, level*range]

def setDificultyMax(level, range):
    return level*range

def verifyDigit(input):
    return input.isdigit()

def verifyInput(character, char_list):
    for i in char_list:
        if i.isupper():
            char_list.append(i.lower())
    return character in char_list

def game():
    # MAIN GAME
    print("\n--------------MATH QUIZ------------------\n")
    while True:
        op = input("Select operator: A-add, S-subtract, M-multiply, D-divide:, E-Exit ")

        if op in ["E", "e"]:
            print("goodbye!")
            break
        if verifyInput(op,["A", "D", "S", "M"]):
            level = input("select level: 1-easy, 2-medium, 3-hard, 4-extreme ")
            if verifyInput(level, ["1", "2", "3", "4"]):
                min, max= 1,setDificultyMax(int(level),10)
                num1, num2 = 0, 0
                ans = 0
                op_symbol = ""
                
                print(op)
                
                if op in ["D", "d"]:
                    posiblevalues = verifyDivide(min, max)
                    values = rnd.choice(posiblevalues)
                    num1 = values[0]
                    num2 = values[1]
                    ans = int(divide(num1, num2))
                    op_symbol = "/"
                else:
                    num1 = rnd.randint(min,max)
                    num2 = rnd.randint(min,max)
                    if op in ["A", "a"]:
                        ans = add(num1, num2)
                        op_symbol = "+"
                    if op in ["S", "s"]:
                        ans = subtract(num1, num2)
                        op_symbol = "-"
                    if op in ["M", "m"]:
                        ans = multiply(num1, num2)
                        op_symbol = "*"
                        
                while True:            
                    print(num1, op_symbol, num2, " = ", end = "")
                    user_input = input("")
                    if verifyDigit(user_input):
                        if user_input == ans:
                            print("Correct!")
                        else:
                            print("Incorrect")
                        break
                    else:
                        print("invalid input")
                        continue
                    
                print("\n--------------MATH QUIZ------------------\n")
            else:
                print("invalid level")
        else:
            print("invalid operator")
