#2*
n= int(input('введите целое цисло  '))
odd_num = range(1,n+1,2)
print('нечетные числа от 1 до n(включительно)')
odd = [i for i in odd_num ]
print(odd)
print('#'*100)

#3


def gen_list_new(tutors,klasses):
     i=0
     while i <= len(tutors)and i<len(klasses):
        yield tutors[i],klasses[i]
        i+=1
     while i < len(tutors):
        yield tutors[i],None
        i+=1


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена','Станислав'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б',
]
for i in gen_list_new(tutors,klasses):
    print(i)
print('#'*100)

#4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(type(src), src)
result =[src[i] for i in range(1,len(src)) if src[i] > src[i-1]]
print(result)

print('#'*100)