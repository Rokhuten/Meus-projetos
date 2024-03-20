# Calculadora

while True:
    print('Menu da calculadora: ')
    print('1 Adiciçao')
    print('2 Subtraçao')
    print('3 Multiplicaçao')
    print('4 Divisao')
    print('5 Sair')
    print()

    menu = input('Selecione uma das opçoes: ')

    if menu == '5':
        print('Encerrando a calculadora')
        break
    print()

    if menu not in ['1', '2', '3', '4']:
        print('Opçao invalida')
        continue

    print()

    numero1 = float(input('Selecione o primeiro valor: '))
    numero2 = float(input('Selecione o segundo valor: '))

    v1 = numero1 + numero2
    v2 = numero1 - numero2
    v3 = numero1 * numero2
    v4 = numero1 / numero2

    if menu == '1':
        resu = v1
    elif menu == '2':
        resu = v2
    elif menu == '3':
        resu = v3
    elif menu == '4':
        resu = v4
        continue

    print()
    print(f'Resulatado: {resu}')
    print()
