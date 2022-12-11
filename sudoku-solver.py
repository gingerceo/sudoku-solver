mysudoku = 'sudoku.txt'


boxes = []
for n in range(0, 3):
    for m in range(0, 3):
        box = []
        for i in range(3*n+27*m, 3*n+27*m+3):
            box.append(i)
            for j in range(1, 3):
                box.append(i+9*j)
        box.sort()
        boxes.append(box)


def checkrow(sudoku, x):
    n = 9*(x//9)
    row = []
    for i in range(n, n+9):
        if sudoku[i] != 0:
            row.append(int(sudoku[i]))
    return len(row) == len(set(row))


def checkcol(sudoku, x):
    n = x % 9
    col = []
    for i in range(0, 9):
        if sudoku[9*i+n] != 0:
            col.append(int(sudoku[9*i+n]))
    return len(col) == len(set(col))


def checkbox(sudoku, n):
    box = []
    for i in boxes:
        if n in i:
            for j in i:
                if sudoku[j] != 0:
                    box.append(int(sudoku[j]))
            break
    return len(box) == len(set(box))


def valid(sudoku, n):
    return checkrow(sudoku, n) and checkcol(sudoku, n) and checkbox(sudoku, n)


sudoku = []
with open(mysudoku, 'r') as fin:
    for line in fin:
        for i in line:
            if i != '\n':
                if i == '0':
                    sudoku.append(0)
                else:
                    sudoku.append(i)

for i in range(0, 9):
    for j in range(9*i, 9*i+9):
        print(f"{sudoku[j]}", end=" ")
    print()
print()

i = 0
while i <= 80:
    if sudoku[i] == 0:
        sudoku[i] = 1
    while (isinstance(sudoku[i], int) and not valid(sudoku, i)) or (
           sudoku[i] == 10):
        while sudoku[i] == 10:
            sudoku[i] = 0
            i -= 1
            while isinstance(sudoku[i], str):
                i -= 1
        sudoku[i] += 1
    i += 1

for i in range(0, 9):
    for j in range(9*i, 9*i+9):
        print(f"{sudoku[j]}", end=" ")
    print()

with open('sol.txt', 'w') as fout:
    for i in range(0, 9):
        for j in range(9*i, 9*i+9):
            fout.write(f"{sudoku[j]}")
        fout.write("\n")
