#Задание №4 Дано две строки. Определить являются ли они анаграммами "автор" "товар"
a = 'автор'
b = 'товар'
a = sorted(a)
b = sorted(b)
if a == b:
    print('true')
else:
    print('false')
#Задание №5 Данн массив (например [1, 2, 3, 4] представляющий число 1234. Прибавить к нему «Единицу» (например [1, 2, 3, 5])
# Еще примеры: [1, 9, 9] + 1 = [2, 0, 0] [9] + 1 = [1, 0]
a = [1,9,9]
a = int(''.join(map(str, a)))
a = a + 1
a = str(a)
a = list(a)
print(a)
#Задание №6 Дан массив чисел и число. Найти 2 числа в массиве, которые в сумме дают данное число
a = [1,2,34,5,5,7,8,10]
b = 9
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]+a[j] == b and a[i]<a[j]:
            print(a[i],a[j])

#Задание №7 Реверсировать строку
a = 'gdhjfkvdn'
print(a[::-1])
#Задание №8 Палиндром. Строка зеркальна за исключением пробелов и спецсимволов (запятых например).
a = 'dcod,sdijc jsdic,os dsi@ du,^'
for i in range(len(a)):
    if ('32'<= ord('a[i]') <= '47') or ('58' <= ord('a[i]') <= '64') or ('91' <= ord('a[i]') <= '96'):
        a = a.replace(a[i],' ',1)
b = sorted(a)
if a == b:
    print('true')
else:
    print('false')