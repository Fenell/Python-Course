import numpy as np

arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])

arr_3 = np.array([[1, 2, 3], [4, 5, 6]])

rsl = arr_1 + arr_2


# print("tong cua tung hang", arr_3.sum(axis=1))
# print("tong cua tung cot", arr_3.sum(axis=0))


# giữ nguyên số chiều


print("tong cua tung hang", arr_3.sum(axis=1, keepdims=True))
print("tong cua tung cot", arr_3.sum(axis=0, keepdims=True))
