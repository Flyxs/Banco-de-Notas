n_provas = int(input('Quantas provas houve ao decorrer do semestre? '))

lista_de_notas = []

for i in range(n_provas):
    lista_de_notas.append(int(input(f'Quanto vc tirou na prova {i+1}? ')))
    
soma_total = sum(lista_de_notas)
    
tipo_de_prova = str(input('Qual foi é o modelo de cálculo? [a]aritimetica ou [p]ponderada) ')).lower()[0]

def calc_media_a():
    resultado = soma_total/n_provas
    print(f'{resultado:.2f}')

if tipo_de_prova == 'a':
    resultado = soma_total/n_provas
    print(f'{resultado:.2f}')
    
elif tipo_de_prova == 'p':
    soma_total_ponderada = 0
    divisor = 0
    
    for i in range(n_provas):
        soma_total_ponderada += lista_de_notas[i] * (i+1)
        divisor += (i+1)
    
    print(f'{soma_total_ponderada/divisor:.2f}')
    
else:
    print('Responde direirto baiano')