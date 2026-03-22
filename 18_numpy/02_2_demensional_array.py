import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("phần tử ở hàng đầu tiên, cột đầu tiên: ", arr_2d[0, 0])
print("phần tử ở hàng 2, cột 2: ", arr_2d[1, 1])

print("hang dau tien", arr_2d[0, :])
print("cot dau tien", arr_2d[:, 0])
