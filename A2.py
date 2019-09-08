import numpy as np

def fileInput():
    file_name = input(‘Enter the file name ‘)
    lines = []
    with open(file_name, ‘r’) as f:
        lines = f.readlines()
    return lines

def input():
    print(’A. Solve a System  of Equation’)
    print(‘B. Perform a LU decomposition’)
    print(‘C. Perform a Matrix Inversion’)
    method = input(‘Choose any of the above methods’)
    if method == ‘A’:
        opt = input(‘Is the system tri-diagonal\? (Y/N)’)
        if opt.upper() ==  ’Y’:
            lines = fileInput()
            n = int(lines[0])
            l = map(int, lines[1].split())
            d = map(int, lines[2].split())
            u = map(int, lines[3].split())
            b = map(int, lines[4].split())
            thomas(n, l, d, u, b)
        if opt.upper() == ‘N’:
            lines = fileInput()
            n = int(lines[0])
            A = []
            for i in range(n):
                A.append(map(int, lines[i + 1].split()))
            b = map(int, lines[n + 1])
            

            

if __name__ == ‘__main__’:
    input()