res = '['
with open("Password.txt","r") as f:
    words = f.readlines()
for word in words :
    word = word.rstrip("\n")
    res += f'"{word}"' + ", "
res += '"amin"]'

print(res,end="")