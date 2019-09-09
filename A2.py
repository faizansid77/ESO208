import numpy as np

def fileInput():
    file_name = input('Enter the file name')
    lines = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines

def thomas(n, l, d, u, b):
    return

def gaussElimination(n, A, b):
    return

def cholesky(n, A, b):
    return

def doolittle(n, A, b):
    return

def crout(n, A, b):
    return

def gaussJordon (n, A):
    return

def input():
    print('A. Solve a System  of Equation')
    print('B. Perform a LU decomposition')
    print('C. Perform a Matrix Inversion')
    method = input('Choose one of the above methods').upper()
    if method == 'A':
        opt = input('Is the system tri-diagonal\? (Y/N)').upper()
        if opt ==  'Y':
            lines = fileInput()
            n = int(lines[0])
            l = map(int, lines[1].split())
            d = map(int, lines[2].split())
            u = map(int, lines[3].split())
            b = map(int, lines[4].split())
            thomas(n, l, d, u, b)
        elif opt == 'N':
            lines = fileInput()
            n = int(lines[0])
            A = []
            for i in range(n):
                A.append(map(int, lines[i + 1].split()))
            b = map(int, lines[n + 1])
            gaussElimination(n, A, b)
    if method == 'B':
        opt = input('Is the matrix symmetric and positive definite\? (Y/N)').upper()
        if opt == 'Y':
            lines = fileInput()
            n = int(lines[0])
            A = []
            for i in range(n):
                A.append(map(int, lines[i + 1].split()))
            b = map(int, lines[n + 1])
            cholesky(n, A, b)
        elif opt == 'N':
            lines = fileInput()
            print()
            print('A. Doolittle')
            print('B. Crout')
            algo = input('Choose one of the above algorithms').upper()
            n = int(lines[0])
            A = []
            for i in range(n):
                A.append(map(int, lines[i + 1].split()))
            b = map(int, lines[n + 1])
            if algo == 'A':
                doolittle(n, A, b)
            elif algo == 'B':
                crout(n, A, b)
    elif method == 'C':
        lines = fileInput()
        n = int(lines[0])
        A = []
        for i in range(n):
            A.append(map(int, lines[i + 1].split()))
        gaussJordon(n, A)




            

if __name__ == '__main__':
    input()