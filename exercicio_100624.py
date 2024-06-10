# EXERCÍCIOS DA  AULA
# Criar um Dicionário:

# 1 - Crie um dicionário chamado estudante com as chaves: "nome", "idade" e "cursos". Atribua valores à sua escolha para essas chaves.

estudante = {
    'nome': 'Helder',
    'idade': 28,
    'cursos': 'design, publicidade',
}


# Acessar Valores:

# 2 - Dado o dicionário estudante = {"nome": "João", "idade": 21, "cursos": ["Matemática", "Ciência da Computação"]}, escreva um programa para imprimir o valor associado à chave "nome".

print(estudante['nome'])

# Adicionar um Par Chave-Valor:

# 3 - Adicione um novo par chave-valor ao dicionário estudante. A nova chave deve ser "nota" e o valor deve ser "10".

estudante['nota'] = 10

# Atualizar Valores:

# 4 - Atualize o valor de "idade" no dicionário estudante para 22.

estudante['idade'] = 22

# Excluir um Par Chave-Valor:

# 5 - Remova a chave "cursos" do dicionário estudante.

del estudante['cursos']


# Iteração sobre dicionário:


# 6 - Escreva um programa que itere sobre o dicionário estudante e imprima cada chave e seu valor correspondente.

print(estudante.items())

for chave, valor in estudante.items():
    print(f'{chave.capitalize()}: {valor}')


# 7 - Use o método get para recuperar o valor da chave "nome" do dicionário estudante. Se a chave não existir, retorne "Chave não encontrada".
print(estudante.get('nome'))


# # Verificar Existência de Chave:

# # 8 - Escreva um programa que verifica se a chave "nota" existe no dicionário estudante. Imprima uma mensagem apropriada com base no resultado.

if 'nota' in estudante:
    print('A chave nota existe')
else:
    print('A chave nota não existe no dicionário')

# # Mesclar Dicionários:

# # 9 - Dado dois dicionários, dict1 = {"a": 1, "b": 2} e dict2 = {"b": 3, "c": 4}, mescle dict2 em dict1 e imprima o dicionário resultante.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)

print(dict1)

# Listas e dicionarios:

# 10 - Crie um programa que recebe informações de um estudante (nome, idade e nota) em um dicionário e adiciona esse dicionário a uma lista "estudantes";
# estudantes = []

estudante2 = {

}

# 11 - A partir da lista criada no exercício anterior, crie um algoritmo que filtre os alunos por nome (por exemplo, se o usuário pesquisar por "an" todos os nomes que contenham "an" devem ser impressos no terminal)
