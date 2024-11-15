import os
import time

os.system('clear')

class Banco_de_notas:
    def __init__(self,nome,matricula,notas=None):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas if notas is not None else []

    def Adcionar_nota(self,nota):
        if len(self.notas) < 3:
            self.notas.append(nota)
        else:
            print('Banco de notas cheio')
            
    def Exibir_nota(self):
        print(f'{self.nome}  {self.matricula}: {self.notas}')
        
    def __str__(self):
        return f'{self.nome}   {self.matricula}:  {self.notas}'  
        
estudantes = []

while True:
    escolha = str(input(f'O que gostaria de fazer? \n [1]Adicionar um estudante  [2]Consultar Nota Pessal  [3]Exibir Resultado da turma  [4]Adcionar Notas  [q]Sair\n'))
    os.system('clear')
    
    if escolha == '1':
        nome = str(input('Qual o nome do estudante? '))
        matricula = str(input('Qual a matricula? '))
        estudantes.append(Banco_de_notas(nome,matricula))
        print(f'O estudante {nome} foi adcionado com sucesso! \n')
        
        time.sleep(2)
        os.system('clear')
        
    elif escolha == '2':
        matricula = input('Digite a matricula do aluno ')
        encontrado = False
        for estudante in estudantes:
            if estudante.matricula == matricula:
                estudante.Exibir_nota()
                encontrado = True
                break
            if not encontrado:
                print(f'Estudante não encontrado, tente novamente.')
                
    elif escolha == '3':
        for estudante in estudantes:
            print(estudante)
        print()
        
        
    elif escolha == 'q':
        print('Obrigado por usar o nosso sistema! ')
        time.sleep(2)
        os.system('clear')
        break