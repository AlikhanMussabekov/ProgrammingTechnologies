# 1.
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему
def me(words):
    count = 0
    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            count += 1
    return count


# 2.
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words):
    x_list = []
    other_list = []
    for word in words:
        x_list.append(word) if word[0] == 'x' else other_list.append(word)
    return sorted(x_list) + sorted(other_list)


# 3.
# Вх: список непустых кортежей,
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def sort_tuples_list(list):
    return sorted(list, key=lambda value: value[-1])


def test(res, expt):
    result = 'Test ✅: \'{}\' equals \'{}\''.format(res, expt) if res == expt else 'Test 🚫: expected \'{}\', but \'{}\' found'.format(expt, res)
    print(result)

def main():
    test(me(['test ing', 'lorem ipsuml', 'hello world h', 'll']), 2)
    test(fx(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']), ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix'])
    test(sort_tuples_list([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
    return

if __name__ == '__main__':
    main()
