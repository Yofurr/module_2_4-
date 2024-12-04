numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers.remove(1)
print(numbers)
# на всякий случай решил удалить (1) с самого начала и отобразить в консоли новый список
# т.к. 1 ни простое ни составное число
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    if i < 2:
        is_prime = False
    for divisor in range(2, int(i ** 0.5) + 1):
        if i % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes:', primes)
print('Not Primes:', not_primes)

