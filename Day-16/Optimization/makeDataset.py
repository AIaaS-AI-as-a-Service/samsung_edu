'''
#cifar10 dataset 저장
import os
from tensorflow.keras.datasets import cifar10
from PIL import Image

# CIFAR-10 데이터 로드
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

# 저장 디렉토리 설정
output_dir = "cifar10_images"
os.makedirs(output_dir, exist_ok=True)

# 각 클래스의 디렉토리 생성
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 
               'dog', 'frog', 'horse', 'ship', 'truck']

for class_name in class_names:
    os.makedirs(os.path.join(output_dir, class_name), exist_ok=True)

# 이미지 저장
for i, (image, label) in enumerate(zip(train_images, train_labels)):
    class_name = class_names[label[0]]
    image_path = os.path.join(output_dir, class_name, f"{i}.png")
    pil_image = Image.fromarray(image)
    pil_image.save(image_path)

print("CIFAR-10 이미지 저장 완료!")
'''
#fashin-mnist data 저장
import os
import numpy as np
from tensorflow.keras.datasets import fashion_mnist
from PIL import Image

# Fashion MNIST 데이터 로드
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# 저장 디렉토리 설정
output_dir = "fashion_mnist_images_original"
os.makedirs(output_dir, exist_ok=True)

# 각 클래스의 디렉토리 생성
class_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

for class_name in class_names:
    os.makedirs(os.path.join(output_dir, class_name), exist_ok=True)

# 이미지 저장
for i, (image, label) in enumerate(zip(train_images, train_labels)):
    class_name = class_names[label]
    image_path = os.path.join(output_dir, class_name, f"{i}.jpg")
    pil_image = Image.fromarray(image)
    pil_image.save(image_path)

print("Fashion MNIST 이미지 저장 완료!")
