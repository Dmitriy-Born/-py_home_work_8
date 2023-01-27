import os
os.system("cls")

n = '12 - 4 * 2 + 6 / 3 +(10 - 6)/ 4 + (6 + 2) * 6 '

m = []
p = []
m2 = []
p2 = [] #для скобок

for i in n:
    if i.isdigit():
        p.append(i)
    elif i == "+" or i == "-" or i == "/" or i == "*" or i == "(" or i == ")":
        p.append(i)
    else:
        continue


i = 0
while i < int(len(p)-1):
    if p[i].isdigit() and p[i+1].isdigit():
        m.append(p[i]+p[i+1])
        i += 2
    else:
        m.append(p[i])
        i += 1
m.append(p[-1])


def calc(a, b, ch):
    if ch == '+':
        return (a + b)

    if ch == '-':
        return (a - b)

    if ch == '*':
        return (a * b)

    if ch == '/':
        return (a / b)


result2 = int (m[0])
i = 0
while i < len(m)-1:  
    if m[i] == '(' or m[i] == ')':
        count = 1
        while m[i] != ')':

            result2 = calc(int(m[i+1]), int(m[i + 3]), m[i + 2])
            p2.append(result2)
            count += 2
            i += 4
        else:
            i += 1

    else:
        p2.append(m[i])
        i += 1
p2.append(m[-1])

result = int(p2[0])

for i in range(1, len(p2)-1, 2):  # 2 - это шаг
    if p2[i] == '*' or p2[i] == '/':
        result = calc(int(p2[i - 1]), int(p2[i + 1]), p2[i])
        m2.append(result)
    else:
        if i - 1 == 0:
            m2.append(p2[i-1])
            m2.append(p2[i])
            if i + 2 < len(m):
                if p2[i + 2] == '*' or p2[i + 2] == '/':
                    continue
                else:
                    m2.append(int(p2[i + 1]))
            else:
                m2.append(int(p2[i + 1]))
        else:
            m2.append(p2[i])
            if i + 2 < len(p2):
                if p2[i + 2] == '*' or p2[i + 2] == '/':
                    continue
                else:
                    m2.append(int(p2[i + 1]))
            else:
                m2.append(int(p2[i + 1]))

itog_result1 = m2[0]
for i in range(1, len(m2) - 1, 2):
    itog_result1 = calc(int(itog_result1), int(m2[i + 1]), m2[i])
print (f'{n} = {itog_result1}')