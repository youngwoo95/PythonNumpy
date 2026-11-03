# 넘파이
'''
from numpy.random import uniform

arr = uniform(0, 10, 10)
print(arr, '\n')

arr2 = uniform(0, 10, (10, ))
print(arr2)

arr3 = uniform(0, 10, (2, 3))
print(arr3)

arr4 = uniform(-10, 11, (3, 4))
print(arr4)
'''

# 파이토치는 uniform() 함수를 제공하지 않는다. 대신, rand() 함수를 사용하여 0~1 사이의 균등분포 난수를 생성한 후, 원하는 범위로 변환해야 한다.