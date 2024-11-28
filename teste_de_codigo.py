def fmt_nome(a):
    nome = a.split(' ')
    nome = [i.capitalize() for i in nome]
    nome = ' '.join(nome)
    return nome

def testa_mat(a):
    if len(a) == 9:
        return True
    else:
        print('Por favor insira uma matricula válida')
        return False