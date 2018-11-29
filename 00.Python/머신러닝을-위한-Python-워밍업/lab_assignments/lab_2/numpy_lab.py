import numpy as np


def p(msg):
    print(msg)


def n_size_ndarray_creation(n, dtype=np.int):
    return np.arange(n * n).reshape(n, n).astype(dtype)


# print(n_size_ndarray_creation(5))


# [[ 0  1  2  3  4]
# [ 5  6  7  8  9]
# [10 11 12 13 14]
# [15 16 17 18 19]
# [20 21 22 23 24]]


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type is 0:
        return np.zeros(shape, dtype)
    elif type is 1:
        return np.ones(shape, dtype)
    elif type is 99:
        return np.empty(shape, dtype)
    else:
        raise ValueError


# p(zero_or_one_or_empty_ndarray(shape=(2, 2), type=1))
# p(zero_or_one_or_empty_ndarray(shape=(3, 3), type=99))


def change_shape_of_ndarray(X, n_row):
    return np.reshape(X, (n_row, -1))


# X = np.ones((32, 32), dtype=np.int)
# p(change_shape_of_ndarray(X, 1))


def concat_ndarray(X_1, X_2, axis):
    try:
        return np.concatenate((X_1, X_2), axis=axis)
    except ValueError:
        return False


# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])

# p(concat_ndarray(a, b, 0))
# p(concat_ndarray(a, b, 1))


# TODO
def normalize_ndarray(X: np.ndarray, axis=99, dtype=np.float32):
    # print(np.mean(X, axis=axis, dtype=dtype))
    if axis is 99:
        return (X - np.mean(X, axis=axis, dtype=dtype)) / np.math.sqrt(np.var(X, axis=axis, dtype=dtype))
    else:
        return (X - np.mean(X, axis=axis, dtype=dtype)) / np.math.sqrt(np.var(X, axis=axis, dtype=dtype))


# X = np.arange(12, dtype=np.float32).reshape(6, 2)

# print(normalize_ndarray(X, axis=0))


def save_ndarray(X, filename="test.npy"):
    np.save(file=filename, arr=X)


# X = np.arange(32, dtype=np.float32).reshape(4, -1)
# filename = "test.npy"
# save_ndarray(X, filename)  # test.npy 파일이 생성됨


def boolean_index(X, condition):
    return X[eval(str("X") + condition)]


# X = np.arange(32, dtype=np.float32).reshape(4, -1)
# print(boolean_index(X, "== 3"))
# X = np.arange(32, dtype=np.float32)
# print(boolean_index(X, "> 6"))


def find_nearest_value(X: np.ndarray, target_value):
    array = np.asarray(X)
    idx = (np.abs(array - target_value)).argmin()
    return array[idx]


X = np.random.uniform(0, 1, 100)
find_nearest_value(X, target_value=0.3)


def get_n_largest_values(X, n):
    array = np.asarray(X)
    array = sorted(array, reverse=True)
    return array[:n]


X = np.random.uniform(0, 1, 100)
print(get_n_largest_values(X, 3))
print(get_n_largest_values(X, 5))
