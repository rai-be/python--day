# Operadores lógicos 
# and (e) or (ou) not (não)
# and todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# são consideradas falsy (que voce ja viu)
# 0 0.0 '' false
# Também existe o tipo none que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air:')
senha_digitada = input('senha:')

senha_permitida = '1214749'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('entrar')
else:
    print('sair')    