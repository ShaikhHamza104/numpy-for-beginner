import numpy as np


def create_matrix(rows, cols):
    """ Create a user-defined matrix """
    print(f"Enter the {rows}x{cols} matrix row by row:")
    return [list(map(float, input().split())) for _ in range(rows)]


def add_matrices(a,b):
    """ Add two matrices A and B of the same dimensions """
    return np.add(a,b)


def subtract_matrices(a,b):
    """ Subtract matrix B from matrix A """
    return np.subtract(a,b)


def multiply_matrices(a,b):
    """ Multiply two matrices A and B (A * B) """
    return np.dot(a,b)


def transpose_matrix(matrix):
    """ Transpose the given matrix """
    return np.transpose(matrix)


def inverse_matrix(matrix):
    """ Invert the given matrix if it is invertible """
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError as e:
        print(f"Matrix inversion failed: {e}")
        return None

def determinate(matrix):
    """ Determinate a matrix """
    print(np.linalg.det(matrix))

def rank(matrix):
    """ Rank the given matrix """
    print(np.linalg.matrix_rank(matrix))

def main():
    # Example matrices
    row = int(input('Enter how many row?\n'))
    colum = int(input('Enter how many colum?\n'))
    a = np.array(create_matrix(row, colum))
    b = np.array(create_matrix(row, colum))

    print("\nMatrix A:")
    print(a)

    print("\nMatrix B:")
    print(b)

    while True:
        print("\nChoose an operation:")
        print("1. Add matrices")
        print("2. Subtract matrix B from matrix A")
        print("3. Multiply matrices (A * B)")
        print("4. Transpose Matrix A")
        print("5. Invert Matrix A")
        print("6. Determinate A")
        print("7. Rank A")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            result = add_matrices(a,b)
            print("Result of addition:")
            print(result)

        elif choice == '2':
            result = subtract_matrices(a,b)
            print("Result of subtraction (A - B):")
            print(result)

        elif choice == '3':
            result = multiply_matrices(a,b)
            print("Result of multiplication (A * B):")
            print(result)

        elif choice == '4':
            result = transpose_matrix(a)
            print("Transpose of Matrix A:")
            print(result)

        elif choice == '5':
            result = inverse_matrix(a)
            if result is not None:
                print("Inverse of Matrix A:")
                print(result)

        elif choice == '6':
            determinate(a)

        elif  choice == '7':
            rank(a)

        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()