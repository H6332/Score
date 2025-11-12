score = input().split()
count = 0
for i in score:
    if (int(i) < 60):
        count += 1
print(count)
