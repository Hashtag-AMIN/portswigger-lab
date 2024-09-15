print("--------------------------\n\tMake username list: \n--------------------------")
for i in range(110):
    if i % 3:
        print("carlos")
    else:
        print("wiener")

print("--------------------------\n\tMake password list: \n--------------------------")
with open('./Password.txt', 'r') as f:
    lines = f.readlines()

i = 0
for pwd in lines:
    if i % 3:
        print(pwd.strip('\n'))
    else:
        print("peter")
        print(pwd.strip('\n'))
        i = i+1
    i = i +1 


