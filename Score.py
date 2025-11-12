score = input().split()
count = 0
total = 0

for i in score:
    if int(i) < 60:
        count += 1
    total += int(i)

average = total / len(score)

print(count)
min = int(score[0])
max = int(score[0])
for i in score:
    if (int(i) < min):
        min = int(i)
    if (int(i) > max):
        max = int(i)
print(max)
print(min)
print(f"{average:.2f}")
