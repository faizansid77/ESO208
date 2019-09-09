import numpy as np

def fileInput():
    file_name = input('Enter the file name : ')
    lines = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return file_name, lines

def thomas(n, l, d, u, b):
    alpha = np.zeros(n)
    alpha[0] = d[0]
    beta = np.zeros(n)
    beta[0] = b[0]
    for i in range(1, n):
        alpha[i] = d[i] - l[i] * u[i-1] / alpha[i-1]
        beta[i] = b[i] - l[i] * beta[i-1] / alpha[i-1]
    x = np.zeros(n)
    x[n-1] = beta[n-1] / alpha[n-1]
    for i in range(n-2, -1, -1):
        x[i] = beta[i] - u[i] * x[i+1] / alpha[i]
    return x

def gaussElimination(n, A, b):
    for k in range(n-1):
        max_ind = abs(A[k:, k]).argmax() + k
        if A[max_ind, k] == 0:
            return None
        if max_ind != k:
            A[[max_ind, k]] = A[[k, max_ind]]
            b[[max_ind, k]] = b[[k, max_ind]]
        for row in range(k+1, n):
            multiplier = A[row, k] / A[k, k]
            A[row, k] = multiplier
            for col in range(k+1, n):
                A[row, col] = A[row, col] - multiplier * A[k, col]
            b[row] = b[row] - multiplier * b[k]
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

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
            l = np.array([float(l) for l in lines[1].split()])
            l = np.insert(l, 0, 0.0)
            d = np.array([float(l) for l in lines[2].split()])
            u = np.array([float(l) for l in lines[3].split()])
            u = np.append(u, 0.0)
            b = np.array([float(l) for l in lines[4].split()])
            x = thomas(n, l, d, u, b)
            print(x)
            with open('out_' + fn, 'w+') as f:
                for i in range(n):
                    f.write(str(x[i])+"\n")
        elif opt == 'N':
            fn, lines = fileInput()
            n = int(lines[0])
            A = np.array([])
            for i in range(n):
                A = np.append(A, [float(n) for n in lines[i + 1].split()], axis=0)
            A = A.reshape((3, 3))
            b = np.array([float(l) for l in lines[n + 1].split()])
            x = gaussElimination(n, A, b)
            print(x)
            with open('out_' + fn, 'w+') as f:
                for i in range(n):
                    f.write(str(x[i])+"\n")
    if method == 'B':
        opt = input('Is the matrix symmetric and positive definite? (Y/N) : ').upper()
        if opt == 'Y':
            lines = fileInput()
            n = int(lines[0])
            A = np.array([])
            for i in range(n):
                A = np.append(A, [float(n) for n in lines[i + 1].split()], axis=0)
            A = A.reshape((3, 3))
            b = np.array([float(l) for l in lines[n + 1].split()])
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
                A = A.append([float(l) for l in lines[i + 1].split()])
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