import os

ip = str(input('Digite o ip desejado: '))

ping = os.system('ping {}'.format(ip))

if ping == 0:
    print('O IP digitado está ON :)')
else:
    print('O IP digitado está OFF :(')