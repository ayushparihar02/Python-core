start = 99
end = 199
divisor = 7
total_sum = 0

for n in range(start, end):
    if n % divisor == 0:
        total_sum += n

print(f"The sum is: {total_sum}")