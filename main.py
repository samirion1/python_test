    Insira o trecho de código abaixo no arquivo main.py:

def in_autotests_we_trust(a, b):
    if a == b:
        print('PASSOU')
    else:
        print('FALHOU')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
