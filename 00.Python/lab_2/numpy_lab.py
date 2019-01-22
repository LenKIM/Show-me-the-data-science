import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    n = n ** 2
    return n


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type is 0:
        return np.zeros(shape=shape, dtype=dtype)
    elif type is 1:
        return np.ones(shape=shape, dtype=dtype)
    else:
        return np.empty(shape=shape, dtype=dtype)


def change_shape_of_ndarray(X, n_row):
    # return np.reshape(X, [n_row, -1])
    return X.flatten() if n_row == 1 else X.rehape(n_row, -1)


def concat_ndarray(X_1: np.ndarray, X_2: np.ndarray, axis):
    # 사전에 이것이 복사가능한지 안가능한지 여부 판별은 어떻게??
    # if axis > 1:
    #     return False
    # else:
    #     try:
    #         return np.concatenate((X_1, X_2), axis=axis)
    #     except ValueError as e:
    #         return False

    if X_1.ndim == 1:
        X_1 = X_1.reshape(1, -1)
    if X_2.ndim == 1:
        X_2 = X_2.reshape(1, -1)
    return np.concatenate((X_1, X_2), axis=axis)


def normalize_ndarray(X, axis=99, dtype=np.float32):
    # 3가지 타입이 있음.
    X = X.astype(np.float32)
    n_row, n_column = X.shape
    if axis == 99:
        x_mean = np.mean(X)
        x_std = np.std(X)
        z = (X - x_mean) / x_std
    if axis == 0:
        x_mean = np.mean(X, 0).reshape(1, -1)
        x_std = np.std(X, 0).reshape(1, -1)
        z = (X - x_mean) / x_std
    if axis == 1:
        x_mean = np.mean(X, 0).reshape(n_row, -1)
        x_std = np.std(X, 0).reshape(n_row, -1)
        z = (X - x_mean) / x_std

    return z


# if axis == 99:
#     avg = np.mean(X, axis=None)
#     _std = np.std(X, axis=None)
#     np.
#

# return np.linalg.norm(X, axis=None)
# else:
# return np.linalg.norm(X, axis=axis)


def save_ndarray(X, filename="test.npy"):
    file_test = open(filename, 'wb')
    return np.save(file_test, X)


def boolean_index(X, condition):
    # cond_arrays = condition.split(' ')
    # operator = {
    #     '<': lt,
    #     '<=': le,
    #     '==': eq,
    #     '>=': ge,
    #     '>': gt,
    # }
    # print(cond_arrays)
    # oper = operator[cond_arrays[0]]
    # return X[oper(X, int(cond_arrays[1]))]
    condition = eval(str("X") + condition)
    return np.where(condition)


def find_nearest_value(X, target_value):
    # np.argmin()
    temp = np.abs(X - target_value)
    idx = np.argmin(temp, axis=0)
    return X.flat[idx]


def get_n_largest_values(X, n):
    # argXXX -> d인텍스 뱃어냅.
    return np.sort(X)[:n]

    return X[np.argsort(X[::-1])[:n]]


def p(_):
    print(_)
