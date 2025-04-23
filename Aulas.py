# Lista = ['Dark Side of the Moon', 'Animals', 'The Wall']
#
# for album in Lista:
#     print(album)



#Verificação
# s='the quick brown fox jumps over the lazy dog'
# if 'a' in s:
#     print('contido')
#
# if '6' not in s:
#     print('não está contido')



#Função range
# for i in range(0, 31, 6):
#     print(i)



#Enumerate
# lista = ['a', 'd', 'y', 'p']
# for i, c in enumerate(lista):
#     print(i, ':', c)


#if como parâmetro
# for i in range(0, 30):
#     if i == 15:
#         break
#     print(i)



#
# for i in range(0, 30):
#     if i%2 != 0:
#         continue
#     print(i)


#Finder
# for i in range(0, 30):
#     if i == 15:
#         print('Encontrei')
#         break
# else:
#     print('Não Encontrei')
#

#Função Zip
# a = ("John", "Carlos", "Mike")
# b = ("João", "Andre", "Douglas")
#
# x = zip(a, b)
# print(list(x))



# names = ['John', 'Robert']
# surnames = ['Smith', 'De Niro']
# numbers = [1, 2]
# for name, surname, number in zip(names, surnames, numbers):
#     print(name, surname, number)



# pares = [ ]
#
# for i in range(0, 100):
#     if i % 2 == 0:
#         pares.append(i)
# print(pares)

#List Comprehension
# pares = [i for i in range(0, 101) if i % 2 == 0]
#
# print(pares)

