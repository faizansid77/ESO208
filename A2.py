import numpy as np

def fileInput():
    file_name = input('Enter the file name : ')
    lines = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return file_name, lines

def thomas(n, l, d, u, b):
    alpha = [None] * n
    alpha[0] = d[0]
    beta = [None] * n
    beta[0] = b[0]
    for i in range(1, n):
        alpha[i] = d[i] - l[i] * u[i-1] / alpha[i-1]
        beta[i] = b[i] - l[i] * beta[i-1] / alpha[i-1]
    x = [None] * n
    x[n-1] = beta[n-1] / alpha[n-1]
    for i in range(n-2, -1, -1):
        x[i] = beta[i] - u[i] * x[i+1] / alpha[i]
    return x

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

def takeInput():
    print('A. Solve a System  of Equation')
    print('B. Perform a LU decomposition')
    print('C. Perform a Matrix Inversion')
    method = input('Choose one of the above methods : ').upper()
    if method == 'A':
        opt = input('Is the system tri-diagonal? (Y/N) : ').upper()
        if opt ==  'Y':
            fn, lines = fileInput()
            n = int(lines[0])
            l = [float(l) for l in lines[1].split()]
            l.insert(0, 0.0)
            d = [float(l) for l in lines[2].split()]
            u = [float(l) for l in lines[3].split()]
            u.append(0.0)
            b = [float(l) for l in lines[4].split()]
            x = thomas(n, l, d, u, b)
            with open(fn+'_out', 'w+') as f:
                for i in range(n):
                    f.write(x[i])
        elif opt == 'N':
            fn, lines = fileInput()
            n = int(lines[0])
            A = []
            for i in range(n):
                A.append([float(n) for n in lines[i + 1].split()])
            b = [float(l) for l in lines[n + 1].split()]
            gaussElimination(n, A, b)
    if method == 'B':
        opt = input('Is the matrix symmetric and positive definite? (Y/N) : ').upper()
        if opt == 'Y':
            lines = fileInput()
            n = int(lines[0])
            A = []
            for i in range(n):
                A.append([float(n) for n in lines[i + 1].split()])
            b = [float(l) for l in lines[n + 1].split()]
            cholesky(n, A, b)
        elif opt == 'N':
            lines = fileInput()
            print()
            print('A. Doolittle')
            print('B. Crout')
            algo = input('Choose one of the above algorithms : ').upper()
            n = int(lines[0])
            A = []
            for i in range(n):
                A.append([float(l) for l in lines[i + 1].split()])
            b = [float(l) for l in lines[n + 1].split()]
            if algo == 'A':
                doolittle(n, A, b)
            elif algo == 'B':
                crout(n, A, b)
    elif method == 'C':
        lines = fileInput()
        n = int(lines[0])
        A = []
        for i in range(n):
            A.append([float(l) for l in lines[i + 1].split()])
        gaussJordon(n, A)




            

if __name__ == '__main__':
    takeInput()