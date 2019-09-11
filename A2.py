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
        max_ind = np.argmax(abs(A[k:, k])) + k
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
    swaps = []
    L = np.zeros((n, n))
    for k in range(n):
        max_r_ind , max_c_ind = np.unravel_index(np.argmax(abs(A[k:, k:])), A[k:, k:].shape)
        max_r_ind += k
        max_c_ind += k
        if A[max_r_ind, max_c_ind] == 0:
            return None
        if max_r_ind != k:
            swaps.append(['r', k, max_r_ind])
            A[[max_r_ind, k]] = A[[k, max_r_ind]]
            b[[max_r_ind, k]] = b[[k, max_r_ind]]
        if max_c_ind != k:
            swaps.append(['c', k, max_c_ind])
            A[:, [max_c_ind, k]] = A[:, [k, max_r_ind]]
        L[k, k] = A[k, k]
        for m in range(k-1):
            L[k, k] -= np.power(A[m, k], 2)
        L[k, k] = np.power(L[k, k], 0.5)
        for row in range(k+1, n):
            L[row, k] = A[row, k]
            for m in range(k-1):
                L[row, k] -= L[row, m] * L[k, m]
            L[row, k] = L[row, k] / L[k, k]
    return L, swaps

def doolittle(n, A, b):
    swaps = []
    L = np.identity(n, dtype=float)
    U = np.zeros((n, n))
    for k in range(n):
        max_r_ind, max_c_ind = np.unravel_index(np.argmax(abs(A[k:, k:])), A[k:, k:].shape)
        max_r_ind += k
        max_c_ind += k
        if A[max_r_ind, max_c_ind] == 0:
            return None
        if max_r_ind != k:
            swaps.append(['r', k, max_r_ind])
            A[[max_r_ind, k]] = A[[k, max_r_ind]]
            b[[max_r_ind, k]] = b[[k, max_r_ind]]
        if max_c_ind != k:
            swaps.append(['c', k, max_c_ind])
            A[:, [max_c_ind, k]] = A[:, [k, max_c_ind]]
        for col in range(n):
            if k > col:
                L[k, col] = A[k, col]
                for m in range(col-1):
                    L[k, col] -= L[k, m] * U[m, col]
                L[k, col] = L[k, col] / U[col, col]
            else:
                U[k, col] = A[k, col]
                for m in range(k-1):
                    U[k, col] -= L[k, m] * U[m, col]
    return L, U, swaps

def crout(n, A, b):
    swaps = []
    L = np.zeros((n, n))
    U = np.identity(n, dtype=float)
    for k in range(n):
        max_r_ind, max_c_ind = np.unravel_index(np.argmax(abs(A[k:, k:])), A[k:, k:].shape)
        max_r_ind += k
        max_c_ind += k
        if A[max_r_ind, max_c_ind] == 0:
            return None
        if max_r_ind != k:
            swaps.append(['r', k, max_r_ind])
            A[[max_r_ind, k]] = A[[k, max_r_ind]]
            b[[max_r_ind, k]] = b[[k, max_r_ind]]
        if max_c_ind != k:
            swaps.append(['c', k, max_c_ind])
            A[:, [max_c_ind, k]] = A[:, [k, max_c_ind]]
        for col in range(n):
            if k >= col:
                L[k, col] = A[k, col]
                for m in range(col-1):
                    L[k, col] -= L[k, m] * U[m, col]
            else:
                U[k, col] = A[k, col]
                for m in range(k-1):
                    U[k, col] -= L[k, m] * U[m, col]
                U[k, col] = U[k, col] / L[k, k]
    return L, U, swaps

def gaussJordon (n, A):
    Aug = np.append(A, np.identity(n), axis=1)
    for k in range(n):
        for j in range(k, 2 * n):
            Aug[k, j] = Aug[k, j] / Aug[k, k]
        for i in range(n):
            if i == k:
                continue
            for j in range(k, 2 * n):
                Aug[i, j] -= Aug[i, k] * Aug[k, j]
    A_Inv = Aug[:, n:]
    return A_Inv

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
                A = np.append(A, [float(l) for l in lines[i + 1].split()], axis=0)
            A = A.reshape((n, n))
            b = np.array([float(l) for l in lines[n + 1].split()])
            x = gaussElimination(n, A, b)
            print(x)
            with open('out_' + fn, 'w+') as f:
                for i in range(n):
                    f.write(str(x[i])+"\n")
    elif method == 'B':
        opt = input('Is the matrix symmetric and positive definite? (Y/N) : ').upper()
        if opt == 'Y':
            fn, lines = fileInput()
            n = int(lines[0])
            A = np.array([])
            for i in range(n):
                A = np.append(A, [float(l) for l in lines[i + 1].split()], axis=0)
            A = A.reshape((n, n))
            b = np.array([float(l) for l in lines[n + 1].split()])
            L, swaps = cholesky(n, A, b)
            print(L)
            with open('out_' + fn, 'w+') as f:
                for i in range(n):
                    for j in range(n):
                        f.write(str(L[i, j])+"\t")
                    f.write("\n")
                f.write("\n")
                for swap in swaps:
                    f.write(swap[0] + str(swap[1]+1) + "\t" + swap[0] + str(swap[2]+1) + "\n")
        elif opt == 'N':
            fn, lines = fileInput()
            print()
            print('A. Doolittle')
            print('B. Crout')
            algo = input('Choose one of the above algorithms : ').upper()
            n = int(lines[0])
            A = np.array([])
            for i in range(n):
                A = np.append(A, [float(l) for l in lines[i + 1].split()], axis=0)
            A = A.reshape((n, n))
            b = np.array([float(l) for l in lines[n + 1].split()])
            if algo == 'A':
                L, U, swaps = doolittle(n, A, b)
            elif algo == 'B':
                L, U, swaps = crout(n, A, b)
            print(L)
            print()
            print(U)
            with open('out_' + fn, 'w+') as f:
                f.write("L\n")
                for i in range(n):
                    for j in range(n):
                        f.write(str(L[i, j])+"\t")
                    f.write("\n")
                f.write("\n")
                f.write("U\n")
                for i in range(n):
                    for j in range(n):
                        f.write(str(U[i, j])+"\t")
                    f.write("\n")
                f.write("\n")
                for swap in swaps:
                    f.write(swap[0] + str(swap[1]+1) + "\t" + swap[0] + str(swap[2]+1) + "\n")
    elif method == 'C':
        fn, lines = fileInput()
        n = int(lines[0])
        A = np.array([])
        for i in range(n):
            A = np.append(A, [float(l) for l in lines[i + 1].split()], axis=0)
        A = A.reshape((n, n))
        A_Inv = gaussJordon(n, A)
        print(A_Inv)
        with open('out_' + fn, 'w+') as f:
            for i in range(n):
                for j in range(n):
                    f.write(str(A_Inv[i, j])+"\t")
                f.write("\n")

if __name__ == '__main__':
    takeInput()