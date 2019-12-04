import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(THIS_FOLDER, 'data.txt')

comp_data = []
with open(data_file) as f:
    comp_data = f.readlines()
    comp_data = [x.strip() for x in comp_data] 

total_fuel = 0
for x in comp_data: 
    newFuel = int(x)
    while True: 
        newFuel = newFuel // 3 - 2
        if newFuel > 0: 
            total_fuel += newFuel
        else: 
            break
        
print(total_fuel)
