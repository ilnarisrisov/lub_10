import random
import logging

logging.basicConfig(filename='lub_10.log', level=logging.DEBUG)

print('Игра началась')
logging.debug('Программа запущена')

while True:
    try:
        N = int(input('Введите, до какого целого натурального числа может загадывать компьютер: '))
        logging.info('Введено число ' + str(N))
        if N < 1:
            print('Недопустимый диапазон')
            logging.error('Недопустимый диапазон')
        else:
            break
    except ValueError:
        print('Введите целое натурльное число')
        logging.error('Введите целое натурально число')

while True:
    try:
        k = int(input('Введите количество попыток на отгадку: '))
        logging.info('Введено число ' + str(k))
        if k < 1:
            print('Недопустимое число')
            logging.error('Недопустимое число')
        else:
            break
    except ValueError:
        print('Введите целое натуральное число')
        logging.error('Введите целое натуральное число')

print('')

the_secret_of_the_computer = random.randint(1, N)

i = 0
while i < k:
    attempt = int(input('\nВведите число, которое, как вы считаете, загадал компьютер: '))
    print('Вы ввели число ' + str(attempt))
    logging.info('Вы ввели число ' + str(attempt))
    if attempt < the_secret_of_the_computer:
        print('Загаданное число больше вашего')
        logging.info('Загаданное число больше вашего')
    elif attempt > the_secret_of_the_computer:
        print("Загаданное число меньше вашего")
        logging.info("Загаданное число меньше вашего")
    elif attempt == the_secret_of_the_computer:
        print('Вы угадали, компьютер загадал число ', the_secret_of_the_computer)
        logging.info('Вы угадали, компьютер загадал число ' + str(the_secret_of_the_computer))
        break
    i += 1

if i == k:
    print('Попытки закончились. Число, которое загадал компьютер - ', the_secret_of_the_computer)
    logging.info('Попытки закончились. Число, которое загадал компьютер - ' + str(the_secret_of_the_computer))

logging.debug('Программа завершена\n')
