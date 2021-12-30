#replace word in Dictionary
value = 'Пили пиво, ели кащу'
word = {'Пили':'ели', 'ели':'пили'}
print(value)
for x in word:
    value = value.replace(x, word[x])
print(value)
