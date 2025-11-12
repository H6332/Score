score = input().split()
count = 0
total = 0

for i in score:
    if int(i) < 60:
        count += 1
    total += int(i)

average = total / len(score)

print(count)
print(f"{average:.2f}")