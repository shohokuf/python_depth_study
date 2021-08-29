# 通用算法库

from sklearn.datasets import load_sample_images
dataset = load_sample_images()
print(len(dataset.images))

first_img_data = dataset.images[0]
print(first_img_data.dtype)
print(first_img_data.dtype)


from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()
plt.matshow(digits.images[6])
plt.show()

