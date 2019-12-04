import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(THIS_FOLDER, 'data-pt2.txt')

origArr = []
with open(data_file, "r") as f:
    for line in f:
        origArr.extend([int(number) for number in line.split(",")])

def save_santa(intCode): 
    for index in range(0, len(intCode), 4):
        if intCode[index] == 1:
            intCode[intCode[index + 3]] = intCode[intCode[index + 1]] + intCode[intCode[index + 2]]
        elif intCode[index] == 2:
            intCode[intCode[index + 3]] = intCode[intCode[index + 1]] * intCode[intCode[index + 2]]
        elif intCode[index] == 99:
            return intCode[0]
            
    return intCode[0]

for x in range(100):
    for y in range(100):
        arr = origArr.copy()
        arr[1] = x
        arr[2] = y
        if save_santa(arr) == 19690720:
            print("The answer is ", 100 * x + y)  
