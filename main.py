import pytest

def print_hi(name):
    print(f'OI, {name}')

def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possivel dividir por 0'

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

#Calcular e testar a area de um quadrado
# Area = lado


#calcular e testar a area de um retangulo
#area = lado1 * Lado 2

#calcular e testar a area de um triangulo
#area = Lado1 + Lado 2 / 2

#calcular e testar area de um circulo
#Area = Pi * Raio  ** 2

def calcular_area_do_circulo(raio):
    return 3.14 * raio ** 1



if __name__ == '__main__':
    print_hi('Evelyn')
    soma = somar_dois_numeros(5,7)
    print(f'A soma é {soma}')

    subtracao = subtrair_dois_numeros(7,5)
    print(f'A subtração é {subtracao}')

    multiplicacao = multiplicar_dois_numeros(7,5)
    print(f'A multiplicação é {multiplicacao}')

    divisao = dividir_dois_numeros(10,0)
    print(f'A divisão é {divisao}')

    elevacao = elevar_um_numero_pelo_outro(4,2)
    print(f'A elevação é {elevacao}')



    # Testar

def testar_somar_dois_numeros():
    # - 1 Etapa: Configura / Prepara
    # Entrada / Input
    num1 = 8
    num2 = 9
    # Saida / Output
    resultado_esperado = 17

    # 2 Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # 3 Etapa: Confirma/ check / Valida
    assert resultado_atual == resultado_esperado


