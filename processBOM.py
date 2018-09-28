with open(r'C:\testes\output\Lista-Arquivos-Problemas.txt') as f:
    lines = f.read().splitlines()
#print(lines.__len__())

for file in lines:
    s = open(file, mode='r', encoding='utf-8-sig').read()
    open(file, mode='w', encoding='utf-8').write(s)
