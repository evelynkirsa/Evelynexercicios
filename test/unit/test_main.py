import pytest

from main import somar_dois_numeros, calcular_area_do_circulo


def testar_somar_dois_numeros():
    # - 1 Etapa: Configura / Prepara
    # Entrada / Input
    num1 = 4
    num2 = 5
    # Saida / Output
    resultado_esperado = 9

    # 2 Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # 3 Etapa: Confirma/ check / Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_circulo():
    raio = 1
    resultado_esperado = 3.14

    resultado_atual = calcular_area_do_circulo(raio)

    assert resultado_atual == resultado_esperado

