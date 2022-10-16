# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
# абвг привет лоркабв шнур


text = (input('введите текст содержащий слова с абв: ').split())
newdata = ''
for item in text:
    if 'абв' not in item:
        newdata += item+' '

print(newdata)
