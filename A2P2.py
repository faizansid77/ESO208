import numpy as np

def fileInput():
    file_name = input('Enter the file name : ')
    lines = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return file_name, lines

def powerMethod(n, A, rel_err):
    itr = 0
    z = np.zeros((n,1))
    z[0, 0] = 1
    y_old = np.zeros_like(z)
    e = np.inf
    while e > rel_err:
        mod_z = np.linalg.norm(z, ord=2)
        y = z / mod_z
        z = np.dot(A, y)
        itr += 1
        e = np.linalg.norm(y - y_old, ord=np.inf)
        y_old = y
    l = np.dot(np.transpose(y), np.dot(A, y))
    return l, y, itr

def QRdecomp(n, A, rel_err):
    itr = 0
    Q = np.zeros((n, n))
    Q[:, 0] = A[:, 0] / np.linalg.norm(A[:, 0], ord=2)
    for k in range(1, n):
        z = A[:, k]
        for i in range(k-1):
            z -= np.dot(np.transpose(A[:, k]), Q[:, i]) * Q[:, i]
        Q[:, k] = z / np.linalg.norm(z, ord=2)
    R = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            R[i, j] = np.dot(np.transpose(Q[:, i]), A[:, j])
    print(Q)
    print(R)
    return [R[i, i] for i in range(n)], itr

def takeInput():
    fn, lines = fileInput()
    n = int(lines[0])
    A = np.array([])
    for i in range(n):
        A = np.append(A, [float(l) for l in lines[i + 1].split()], axis=0)
    A = A.reshape((n, n))
    rel_err = float(lines[n + 1])
    print('L. Largest Eigenvalue')
    print('A. All Eigenvalues')
    opt = input('Choose one of the above options : ').upper()
    if opt == 'L':
        l, y, itr = powerMethod(n, A, rel_err)
        print(l)
        print(y)
        with open('out_' + fn, 'w+') as f:
            f.write("Eigenvalue\n")
            f.write(str(l[0, 0]) + "\n\n")
            f.write("Eigenvector\n")
            for i in range(n):
                f.write(str(y[i, 0]) + "\n")
            f.write("\n")
            f.write("Iterations\n")
            f.write(str(itr))
    elif opt == 'A':
        ls, itr = QRdecomp(n, A, rel_err)
        print(ls)
        with open('out_' + fn, 'w+') as f:
            f.write("Eigenvalues\n")
            for i in range(n):
                f.write(str(ls[i]) + "\n")
            f.write("\n")
            f.write("Iterations\n")
            f.write(str(itr))

if __name__ == '__main__':
    takeInput()