# 가변인자로 여러개 들어 올것임
def vector_size_check(*vector_variables) -> bool:
    return all(len(vector_variables[0]) == x for x in [len(vector) for vector in vector_variables[1:]])


def vector_addition(*vector_variables):
    return [sum([vector_variables[i][j] for i in range(len(vector_variables))]) for j in
            range(len(vector_variables[0]))]


def vector_subtraction(*vector_variables):
    return [elements[0] * 2 - sum(elements) for elements in zip(*vector_variables)]


def vector_subtraction2(*vector_variables):
    return [
        sum([vector_variables[i][j] if i == 0 else (-1) * vector_variables[i][j] for i in range(len(vector_variables))])
        for j in range(len(vector_variables[0]))]


def scalar_vector_product(alpha, vector_variable):
    return [single_input * alpha for single_input in vector_variable]


def matrix_size_check(*matrix_variables):
    # total_list = []
    #
    # for matrix_variable in matrix_variables:
    #     shape = [len(matrix_variable), len(matrix_variable[0])]
    #     total_list.append(shape)
    #
    # print(total_list)

    # input = [[3, 2], [2, 2], [2, 2]]
    # bo = False
    # print(len([a for a in range(len(input) - 1) if input[a] == input[a + 1]]) > 0)
    # if __[a + 1] == __[a]:
    #     bo = True
    _input = [[[len(matrix_variable), len(matrix_variable[0])] for matrix_variable in matrix_variables]]
    # print(len([a for a in range(len(_input[0]) - 2)]))
    return len([a for a in range(len(_input[0]) - 2) if _input[0][a] != _input[0][a + 1]]) > 0


def is_matrix_equal(*matrix_variables):
    return all([all([len(set(row)) == 1 for row in zip(*matrix)])
                for matrix in zip(*matrix_variables)])


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[sum(row) for row in zip(*matrix)] for matrix in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    return [[row[0] * 2 - sum(row) for row in zip(*matrix)] for matrix in zip(*matrix_variables)]


def matrix_transpose(matrix_variable):
    return [[element for element in row] for row in zip(*matrix_variable)]


def scalar_matrix_product(alpha, matrix_variable):
    return [scalar_vector_product(alpha, row) for row in matrix_variable]


def is_product_availability_matrix(matrix_a, matrix_b):
    return len([column_vector for column_vector in zip(*matrix_a)]) == len(matrix_b)


def matrix_product(matrix_a, matrix_b):
    return [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
