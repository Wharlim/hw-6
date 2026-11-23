def dot_product(vector1, vector2):
    total = 0 
    for i in range(len(vector1)):
        current_product = vector1[i] * vector2[i]
        total += current_product
    return total

def zero_matrix(rows,cols):
    zero = 0.0
    zero_matrix = []
    for i in range(rows):
        zero_matrix.append([])
        for j in range(cols):
            zero_matrix[i].append(zero)
    return zero_matrix

def identity_matrix(size):
    zero = 0.0
    one = 1.0
    identity = []
    for i in range(size):
        identity.append([])
        for j in range(size):
            if i == j:
                identity[i].append(one)
            else:
                identity[i].append(zero)
    return identity

def test_zero_matrix_aliasing():
    matrix = zero_matrix(3, 3)
    matrix[0].append(1)
    assert len(matrix[0])!= len(matrix[1]), "Aliasing detected in zero_matrix function"
    return len(matrix[0]) != len(matrix[1])

def main():
    # Test dot_product function
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]
    print("Dot Product:", dot_product(vector1, vector2))  # Expected output: 32

    # Test zero_matrix function
    zero_mat = zero_matrix(3, 3)
    print("Zero Matrix:")
    for row in zero_mat:
        print(row)

    # Test identity_matrix function
    identity_mat = identity_matrix(3)
    print("Identity Matrix:")
    for row in identity_mat:
        print(row)

    # Test for aliasing in zero_matrix
    value = test_zero_matrix_aliasing()
    print(value)

if __name__ == "__main__":
    main()