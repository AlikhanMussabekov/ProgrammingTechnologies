# 1.
# Вх: строка. Если длина > 3, добавить в конец "ing",
# если в конце нет уже "ing", иначе добавить "ly".

def v(s):
    return s + "ing" if len(s) > 3 else s + "ly"

# 2.
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!

def nb(s):
  return s[0:s.find("not")] + "good" + s[s.find("bad") + len("bad"):]

def test(res, expt):
    result = f"Test ✅: \'{res}\' equals \'{expt}\'" if res == expt else f"Test 🚫: expected \'{expt}\', but \'{res}\' found"
    print(result)

def main():
    test(v("ooeoo"), "ooeooing")
    test(v("oo"), "ooly")
    test(nb("This music is not so bad!"), "This music is good!")

if __name__ == '__main__':
  main()
