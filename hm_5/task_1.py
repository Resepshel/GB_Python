"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""

str = 'абв абвабвабв абаулвфвц пофабв уьаупщ пкртйц вцабвпое'
result_str = ''
mass = str.split()
print(mass)
for el in mass:
    if 'абв' not in el:
        result_str += f'{el} '

print(result_str)
