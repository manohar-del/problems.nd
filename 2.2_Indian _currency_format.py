a = float(input("Enter a number: "))
b = str(a)

if '.' in b:
    int_part, dec_part = b.split('.')
    dec_part = '.' + dec_part
else:
    int_part = b
    dec_part = ''

int_part = int_part[::-1]

formatted = ''
for i in range(len(int_part)):
    if i == 3 or (i > 3 and (i - 1) % 2 == 0):
        formatted += ','
    formatted += int_part[i]

formatted = formatted[::-1]

formatted_number = formatted + dec_part
print(formatted_number)
