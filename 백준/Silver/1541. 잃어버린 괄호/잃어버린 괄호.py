expression = input().split('-')
result = 0
if expression[0] != '':
    result += sum(map(int, (expression[0].split('+'))))

for i in expression[1:]:
    result -= sum(map(int, (i.split('+'))))

print(result)