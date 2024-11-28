import os
import time
from teste_de_codigo import fmt_nome, testa_mat

os.system('clear')

class Banco_de_notas:
    def __init__(self,nome,matricula,notas=None):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas if notas is not None else [0,0,0]

    def Adcionar_nota(self,pos,nota):
        self.notas[pos-1] = int(nota)
        print('Nota adcionada com sucesso!')
            
    def Remove_nota(self,pos):
        del self.notas[pos-1]
        print(f'Nota {pos} removida com sucesso')
        return self.notas
    
    def Calc_med_a(self):
        media = sum(self.notas)/3
        return media     
             
    def Exibir_nota(self):
        print(f'{self.nome}  {self.matricula}: {self.notas} ')
        
    def __str__(self):
        return f'{self.nome}   {self.matricula}:  {self.notas}'  
    
        
estudantes = []

while True:
    escolha = str(input(f'O que gostaria de fazer? \n [1]Adicionar um estudante \n [2]Consultar Nota Pessoal \n [3]Exibir Resultado da turma \n [4]Adcionar Notas \n [5]Remover uma nota \n [q]Sair\n'))
    os.system('clear')
    
    if escolha == '1':
        nome = str(input('Qual o nome do estudante? '))
        nome = fmt_nome(nome)
        matricula = str(input('Qual a matricula? '))
        if testa_mat(matricula):
            estudantes.append(Banco_de_notas(nome,matricula))
            print(f'O estudante {nome} foi adcionado com sucesso! \n')
        
        time.sleep(2)
        os.system('clear')
        
    elif escolha == '2':
        matricula = input('Digite a matricula do aluno: ')
        os.system('clear')
        encontrado = False
        for estudante in estudantes:
            if estudante.matricula == matricula:
                estudante.Exibir_nota()
                print()
                encontrado = True
                break
            if not encontrado:
                print(f'Estudante não encontrado, tente novamente.')
                
    elif escolha == '3':
        print('Alunos cadastrados: \n')
        for estudante in estudantes:
            print(estudante)
        print()
        
    elif escolha == '4':
        matricula = input('Qual a matricula do aluno?\n')
        encontrado = False
        for estudante in estudantes:
            if estudante.matricula == matricula:
                encontrado = True
                pos = int(input('Qual a nota que gostária de modificar? [1] [2] [3]\n'))
                nota = float(input('Digite a nota: ')) 
                estudante.Adcionar_nota(pos,nota)
        if not encontrado:
            print('Estudante não encontrado')
            
        time.sleep(2)
        os.system('clear')
        
    elif escolha == '5':
        matricula = input('Qual a matrícula do aluno?\n')
        encontrado = False
        for estudante in estudantes:
            if estudante.matricula == matricula:
                encontrado = True
                nota = int(input('Qual a prova que deseja remover? [1] [2] [3]'))
                estudante.Remove_nota(nota)
            if not encontrado:
                print('Estudante não encontrado')

        time.sleep(2)
        os.system('clear')
        
    elif escolha == 'q':
        print('Obrigado por usar o nosso sistema! ')
        time.sleep(2)
        os.system('clear')
        break
    