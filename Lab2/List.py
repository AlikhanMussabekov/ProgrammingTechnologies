# 1.
# Вх: список чисел, Возвр: список чисел, где
# повторяющиеся числа урезаны до одного
# пример [0, 2, 2, 3] returns [0, 2, 3].

def rm_adj(nums):
  return list(set(nums))

# 2. Вх: Два списка упорядоченных по возрастанию, Возвр: новый отсортированный объединенный список
def sort_two(first, second):
    first += second
    first.sort()
    return first

def test(res, expt):
    result = f"Test ✅: \'{res}\' equals \'{expt}\'" if res == expt else f"Test 🚫: expected \'{expt}\', but \'{res}\' found"
    print(result)

def main():
    test(rm_adj([0, 2, 2, 3, 4]), [0, 2, 3, 4])
    test(sort_two([0, 2, 4], [2, 3 , 1]), [0, 1, 2, 2, 3, 4])

if __name__ == '__main__':
  main()
