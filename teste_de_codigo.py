def fmt_nome(a):
    nome = a.split(' ')
    nome = [i.capitalize() for i in nome]
    print(' '.join(nome))
    
fmt_nome('jose alcantra soares')