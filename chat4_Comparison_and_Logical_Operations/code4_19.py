'''
1. accuracy
2. TP, TN, FP, FN
3. confusion matrix
4. precision, recall, f1-score
'''


'''
acc = 맞은 개수 / 전체개수
'''

'''
confusion matrix 정리
'''

from numpy.random import randint

n_data = 10
preds = randint(0, 2, n_data)
labels = randint(0, 2, n_data)

print(f"preds: {preds}")
print(f"labels: {labels}\n")

corrects = (preds == labels)
n_corrects = corrects.sum()

print(f"ncorrects: {corrects}")
print(f"n_corrects: {n_corrects}\n")

acc = n_corrects / len(preds)
print(f"corrects: {acc}")