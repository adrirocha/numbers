def aumentar(x):
    n1 = x
    n2 = float(input("Digite o valor que você quer acrescentar: "))
    global resa
    resa = n1+n2


def diminuir(x):
    n1 = x
    n2 = float(input("Digite o valor que você quer diminuir: "))
    global resd
    resd = n1-n2

def dobro (x):
    global resdo
    resdo = x*2

def metade(x):
    global resm
    resm = x/2

def resumo(num):
    metade(num)
    aumentar(num)
    dobro(num)
    diminuir(num)
    print('-'*40)
    print('-'*5,'      RESUMO DO VALOR       ','-'*5)
    print('-' * 40)
    print(f'Preço analisado: R${num}')
    print(f'Preço aumentado: R${resa}')
    print(f'Preço diminuido: R${resd}')
    print(f'Preço dobrado: R${resdo}')
    print(f'Preço pela metade: R${resm}')

