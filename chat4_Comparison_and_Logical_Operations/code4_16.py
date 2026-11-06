import numpy as np

arr = np.array([[True, False, True],
                [False, True, True]])
print(f"arr: \n{arr}")
print(f"-> {np.all(arr) =}")
print(f"-> {np.any(arr) =}\n")

'''
all -> 전체가 True 여야 True
any -> 하나라도 True 이면 True
'''


arr2 = np.array([[True, True, True],
                 [True, True, True]])
print(f"arr2: \n{arr2}")
print(f"-> {np.all(arr2) =}")
print(f"-> {np.any(arr2) =}\n")


arr3 = np.array([[False, False, False],
                 [False, False, False]])
print(f"arr3: \n{arr3}")
print(f"-> {np.all(arr3) =}")
print(f"-> {np.any(arr3) =}\n")