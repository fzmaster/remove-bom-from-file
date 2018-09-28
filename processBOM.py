
# Open file with list of BOM-ed files
with open(r'C:\testes\output\Lista-Arquivos-Problemas.txt') as f:
    lines = f.read().splitlines()
#print(lines.__len__())

# Loop each file solving the problem - It will overwrite the original file
for file in lines:
    s = open(file, mode='r', encoding='utf-8-sig').read()
    open(file, mode='w', encoding='utf-8').write(s)
