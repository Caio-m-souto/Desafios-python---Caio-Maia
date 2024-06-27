vagas = []
n = int(input('\nVagas existentes: '))
while n < 1 or n > 2000:
    n = int(input('\nVagas existentes: '))
m = int(input('\nExpectativa de clientes: '))
while m < 1 or m > 2000:
    m = int(input('\nExpectativa de clientes: '))
for i in range(1, m+1):
    v_i = int(input(f'{i}° Cliente - Plano de estacionamento: '))
    if v_i > i:
        pass
    elif v_i not in vagas:
        vagas.append(v_i)
estacionados = len(vagas)
print(estacionados)
