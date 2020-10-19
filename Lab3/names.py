import sys
from bs4 import BeautifulSoup

# для каждого переданного аргументом имени файла, вывести имена extr_name
# напечатать ТОП-10 муж и жен имен из всех переданных файлов

def main():
    file_names = sys.argv[1:]
    
    if len(file_names) < 2:
        print('use: [--file] file [file ...]')
        sys.exit(1)
    
    for file_name in file_names[1:] : extr_name(file_name)

# Вход: nameYYYY.html,
# Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
# '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д.

def extr_name(filename):
    with open(filename, "r") as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        year = soup.find('input', id="yob")['value']
        top = top_10(soup.find('table', summary="Popularity for top 1000"))
        top.sort()
        print(f"{year}, {', '.join(map(str, top)) }")
    f.close()

def top_10(table):
    top = []
    result = [row.text.replace('\n', ' ').split(' ')[1:4] for row in table.find_all('tr')][1:11]
    for row in result:
        top.append(f"{row[1]} {row[0]}")
        top.append(f"{row[2]} {row[0]}")
    return top

if __name__ == '__main__':
  main()
