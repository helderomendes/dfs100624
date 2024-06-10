
#Modelo 

estudante = {
    'nome': 'Helder',
    'matricula': 2726615,
    'data_nascimento': '22/11/1995',
    'coeficiente_academico': 9.3
}

print(estudante['nome'])
print(estudante['matricula'])
print(estudante['data_nascimento'])

estudante['cursos'] = ['Matematica, Fisica, Biologia']

print(estudante['cursos'])

del estudante['cursos']

print(estudante.keys())

print(list)