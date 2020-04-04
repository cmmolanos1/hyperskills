import math

def dot_product(v1, v2):
    """Performs dot product of 2 vectors with the same len

    Arguments:
        v1 {List} -- Vector 1 to multiply
        v2 {List} -- Vector 2 to multiply

    Returns:
        [Int or Float] -- Result of dot product
    """
    suma = 0
    for i in range(len(v1)):
        suma += (v1[i] * v2[i])
    return suma


def transpose(m1):
    """Transpose the matrix m1, change columns by rows

    Arguments:
        m1 {Nested List} -- Matrix to be transponse

    Returns:
        [Nested List] -- Transposed Matrix
    """
    transposed = [[] for row in m1[0]]
    for col in range(len(m1[0])):
        for row in range(len(m1)):
            transposed[col].append(m1[row][col])
    return transposed


def transpose_side(m1):
    """Transpose the matrix m1, change columns by rows
    referencing the side diagonal

    Arguments:
        m1 {Nested List} -- Matrix to be transponse

    Returns:
        [Nested List] -- Transposed Matrix
    """
    transposed = transpose(m1)
    transposed.reverse()
    for row in transposed:
        row.reverse()
    return transposed


def transpose_horizontal(m1):
    """Transpose the matrix m1 horizontally

    Arguments:
        m1 {Nested List} -- Matrix to be transponse

    Returns:
        [Nested List] -- Transposed Matrix
    """
    transposed = [[n for n in row] for row in m1]
    transposed.reverse()
    return transposed


def transpose_vertical(m1):
    """Transpose the matrix m1 vertically

    Arguments:
        m1 {Nested List} -- Matrix to be transponse

    Returns:
        [Nested List] -- Transposed Matrix
    """
    transposed = [[n for n in row] for row in m1]
    for row in transposed:
        row.reverse()
    return transposed


def minor_matrix(m, row, col):
    """Extract the minor matrix from an element

    Arguments:
        m {Nested List} -- Matrix where the element belongs to
        row {Int} -- Row where the element is located
        col {Int} -- Column where the element is located

    Returns:
        [Nested List] -- Minor matrix
    """
    copy = [[n for n in row] for row in m]
    minor = copy[:]
    del minor[row]
    for row in minor:
        del row[col]
    return minor


def determiner(m):
    """ Returns Determinant of a matrix m

    Arguments:
        m {Nested list} -- Matrix to calculate determinant

    Returns:
        [Int or Float] -- Determinant of matrix
    """
    if len(m) == 2 and len(m[0]) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    elif len(m) == 1 and len(m[0]) == 1:
        return m[0][0]
    else:
        det = 0
        for j in range(len(m)):
            det += m[0][j] * pow(-1, 1 + 1 + j) * determiner(minor_matrix(m, 0, j))
        return det


def inverse(m):
    """ Calculates the Inverse Matrix of m

    Arguments:
        m {Nested List} -- Matrix to calculate Inverse

    Returns:
        [Nested List] -- Inverse Matrix
    """
    m_copy = m[:]
    det = determiner(m_copy)
    if det != 0:
        factor = 1 / det
        pre_adj = m_copy[:]
        adjoint = [[0 for elem in row] for row in pre_adj]
        for i in range(len(pre_adj)):
            for j in range(len(pre_adj[0])):
                adjoint[i][j] = pow(-1, i + 1 + j + 1) * determiner(minor_matrix(m, i, j))
        inverse = [[factor * number for number in row] for row in transpose(adjoint)]
        return inverse

    else:
        print("This matrix doesn't have an inverse.\n")


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    choice = int(input("Your choice: "))

    if choice == 0:
        break

    if choice == 4:
        print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        transposechoice = int(input("Your choice: "))

    # MATRIX 1
    dimension1 = input(f'Enter size of{"" if choice == 2 or choice == 4 or choice == 5 or choice == 6 else " first"} matrix: ')
    rows1 = int(dimension1.split()[0])
    columns1 = int(dimension1.split()[1])

    print(f'Enter{"" if choice == 2 or choice == 4 or choice == 5 or choice == 6 else " first"} matrix:')
    matrix1 = [input().split() for count in range(rows1)]
    matrix1 = [[float(number) if "." in number else int(number) for number in row] for row in matrix1]

    if choice != 2 and choice != 4 and choice != 5 and choice != 6:
        # MATRIX 2
        dimension2 = input("Enter size of second matrix: ")
        rows2 = int(dimension2.split()[0])
        columns2 = int(dimension2.split()[1])

        print("Enter second matrix:")
        matrix2 = [input().split() for count in range(rows2)]
        matrix2 = [[float(number) if "." in number else int(number) for number in row] for row in matrix2]

        if choice == 1:
            if rows1 == rows2 and columns1 == columns2:
                suma = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

                print("The result is:")
                for row in suma:
                    print(" ".join(str(number) for number in row))
                print()

            else:
                print("The operation cannot be performed.\n")

        elif choice == 3:
            if columns1 == rows2:
                # Transponding MATRIX 2
                transpose = [[] for row in matrix2[0]]
                for col in range(len(matrix2[0])):
                    for row in range(len(matrix2)):
                        transpose[col].append(matrix2[row][col])

                # Create and fill the answer with 0's
                ans = [[0 for col in range(columns2)] for row in range(rows1)]

                # Dot product between MATRIX 1 and TRANSPONSE
                for i in range(len(ans)):
                    for j in range(len(ans[i])):
                        ans[i][j] = dot_product(matrix1[i], transpose[j])

                print("The result is:")
                for row in ans:
                    print(" ".join(str(number) for number in row))
                print()

            else:
                print("The operation cannot be performed.\n")

    else:
        if choice == 2:
            scalar = input("Enter constant: ")
            scalar = float(scalar) if "." in scalar else int(scalar)

            multiplied = [[scalar * number for number in row] for row in matrix1]

            print("The result is:")
            for row in multiplied:
                print(" ".join(str(number) for number in row))
            print()


        elif choice == 4:
            if transposechoice == 1:
                transposed = transpose(matrix1)
                print("The result is:")
                for row in transposed:
                    print(" ".join(str(number) for number in row))
                print()

            elif transposechoice == 2:
                transposed = transpose_side(matrix1)
                print("The result is:")
                for row in transposed:
                    print(" ".join(str(number) for number in row))
                print()

            elif transposechoice == 3:
                transposed = transpose_vertical(matrix1)
                print("The result is:")
                for row in transposed:
                    print(" ".join(str(number) for number in row))
                print()

            elif transposechoice == 4:
                transposed = transpose_horizontal(matrix1)
                print("The result is:")
                for row in transposed:
                    print(" ".join(str(number) for number in row))
                print()

        elif choice == 5:
            det = determiner(matrix1)
            print(f'The result is:\n{det}\n')

        elif choice == 6:
            inverse = inverse(matrix1)

            for i in range(len(inverse)):
                for j in range(len(inverse)):
                    if inverse[i][j] % 1 == 0:
                        inverse[i][j] = int(inverse[i][j])

            str_inverse = [[str(n) for n in row] for row in inverse]

            for i in range(len(str_inverse)):
                for j in range(len(str_inverse)):
                    index = str_inverse[i][j].find('.')
                    str_inverse[i][j] = str_inverse[i][j][:(index + 3)]

            for row in str_inverse:
                print(" ".join(number for number in row))
            print()
