import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(THIS_FOLDER, 'data-pt2.txt')

intCode = []
with open(data_file, "r") as f:
    for line in f:
        intCode.extend([int(number) for number in line.split(",")])
intCode[1] = 12
intCode[2] = 2

def save_santa(intCode): 
    for index in range(0, len(intCode), 4):
        if intCode[index] == 1:
            intCode[intCode[index +3]] = intCode[intCode[index + 1]] + intCode[intCode[index + 2]]
        elif intCode[index] == 2:
            intCode[intCode[index +3]] = intCode[intCode[index + 1]] * intCode[intCode[index + 2]]
        elif intCode[index] == 99:
            return intCode[0]
            
    return intCode[0]

print("The answer is: ", save_santa(intCode))
