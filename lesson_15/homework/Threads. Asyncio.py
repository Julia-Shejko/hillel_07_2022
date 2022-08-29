def get_primes_amount(num: int) -> int:
    result = 0
    for i in num:
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
                print(f"✌️{counter}")
            if counter > 2:
                break
        result += 1
        print(result)

    return result

numbers = [40000, 400, 1000000, 700]

for i in numbers:
    print(i)

get_primes_amount(numbers)

# NOTE: Щож. Ця реалізація займає досить багато часу...
#       Було б чудово, якби люди, які передають менші числа, отримували результати швидше,
#       ніж ті, хто передають великі значення

# NOTE: Обмеження максимального числа - 1000000

# Закінчіть цю функцію
# Застосуйте асинхронне програмування