import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(THIS_FOLDER, 'data.txt')

comp_data = []
with open(data_file) as f:
    comp_data = f.readlines()
    comp_data = [x.strip() for x in comp_data] 
print(sum(int(i) // 3 - 2 for i in comp_data))
