# 1.
# Входящие параметры: int ,
# Результат: string в форме
# "Number of: ", где число из вход.парам.
# Если число равно 10 или более, напечатать "many"
# вместо # Пример: (5) -> "Number of: 5"
# (23) -> 'Number of: many'

def num_of_items(count):
    return 'Number of: {}'.format(count) if count < 10 else 'Many'


# 2.
# Входящие параметры: string s,
# Результат: string из 2х первых и 2х последних символов s
# Пример 'welcome' -> 'weme'.
def start_end_symbols(s):
    return s[0:2] + s[-2:]


# 3.
# Входящие параметры: string s,
# Результат: string где все вхождения 1го символа заменяются на '*'
# (кроме самого 1го символа)
# Пример: 'bibble' -> 'bi**le'
# s.replace(stra, strb)

def replace_char(s):
    first_char = s[0]
    return first_char + s[1:].replace(first_char, '*')


# 4
# Входящие параметры: string a и b,
# Результат: string где и разделены пробелом
# а превые 2 симв обоих строк заменены друг на друга
# Т.е. 'max', pid' -> 'pix mad'
# 'dog', 'dinner' -> 'dig donner'
def str_mix(a, b):
    return '{} {}'.format(b[0:2] + a[2:], a[0:2] + b[2:])


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(res, expt):
    result = 'Test ✅: \'{}\' equals \'{}\''.format(res, expt) if res == expt else 'Test 🚫: expected \'{}\', but \'{}\' found'.format(expt, res)
    print(result)


def main():
    test(num_of_items(10), 'Many')
    test(start_end_symbols('welcome'), 'weme')
    test(replace_char('bibble'), 'bi**le')
    test(str_mix('dog', 'dinner'), 'dig donner')
    return

if __name__ == '__main__':
    main()
