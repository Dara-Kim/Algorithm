expression = input().split('-')
chunk = []
for xp in expression:
    chunk.append(sum(map(int, xp.split('+'))))

print(sum(chunk[1:]) * -1 + chunk[0])