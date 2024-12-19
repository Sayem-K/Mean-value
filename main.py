prev_mean = 38
total = 40
correct = 56
wrong = 36

prev_sum = prev_mean * total
new_sum = prev_sum + correct - wrong

print("New Sum:" ,new_sum)

new_mean = new_sum / total
print("New Mean:" ,new_mean)