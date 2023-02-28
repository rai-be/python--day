# operadores in e not in
# Strings são interaveis (interavel: navegar intem por item)
# 0 1 2 3 4 5
# r a i a n i
# -6-5-4-3-2-1
#nome = 'raiani'
#print(nome[2])
#print(nome[-4])
#print('a' in nome)
#print('z' in nome)

nome = input('digite se nome')
encontrar = input('digite oque deseja encontrar')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')