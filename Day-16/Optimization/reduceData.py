import os
import random
from PIL import Image

def create_subset_dataset(original_dir, output_dir, class_names, percentage):
    """
    각 클래스에서 n% 데이터만 선택하여 새로운 데이터셋 생성.

    Parameters:
        original_dir (str): 기존 데이터 디렉토리 경로
        output_dir (str): 새로운 데이터셋 저장 경로
        class_names (list): 클래스 이름 리스트
        percentage (float): 선택할 데이터의 비율 (0 < percentage <= 100)
    """
    os.makedirs(output_dir, exist_ok=True)
    
    for class_name in class_names:
        os.makedirs(os.path.join(output_dir, class_name), exist_ok=True)
        
        # 원본 디렉토리에서 클래스별 이미지 가져오기
        class_dir = os.path.join(original_dir, class_name)
        all_images = os.listdir(class_dir)
        random.shuffle(all_images)  # 무작위로 섞기
        
        # n% 데이터 선택
        sample_count = int(len(all_images) * (percentage / 100))
        selected_images = all_images[:sample_count]
        
        # 새로운 디렉토리에 이미지 복사
        for img_name in selected_images:
            src_path = os.path.join(class_dir, img_name)
            dst_path = os.path.join(output_dir, class_name, img_name)
            Image.open(src_path).save(dst_path)
    
    print(f"각 클래스의 {percentage}% 데이터 저장 완료!")

# CIFAR-10 클래스 이름
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 
               'dog', 'frog', 'horse', 'ship', 'truck']

#class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
#               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 기존 데이터 디렉토리 및 출력 디렉토리 설정
original_dir = "cifar10_full_images"
output_dir = "cifar10_images_subset"


# 기존 데이터 디렉토리 및 출력 디렉토리 설정
#original_dir = "fashion_mnist_full_images"
#output_dir = "fashion_mnist_subset"


# 원하는 비율 (예: 25%)
percentage = 50  # 0~100 사이 값

# n% 데이터 생성
create_subset_dataset(original_dir, output_dir, class_names, percentage)