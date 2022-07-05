print("show_sales")
with open('bakery.csv', 'r', encoding='utf-8') as f:
       for i in f:
           print(i)
n = int(input('show_sales '))
with open('bakery.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range((n-1),len(lines)):
        print(lines[i])
g = input("show_sales ").split()
A = int(g[0])
B = int(g[1])
for i in range(A-1,B):
    print(lines[i])
