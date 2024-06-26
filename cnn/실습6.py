# -*- coding: utf-8 -*-
"""실습6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pqHETYElYKlrG4c3Bm41DkMC0avkgVIU
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout, Rescaling
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.densenet import DenseNet121
from tensorflow.keras.utils import image_dataset_from_directory
import pathlib
from PIL import Image, UnidentifiedImageError
import os

# 구글 드라이브 마운트
from google.colab import drive
drive.mount('/gdrive')

# 데이터셋 경로
data_path = '/gdrive/My Drive/L09/datasets/Stanford_dogs/Images'

# 이미지 변환 및 저장할 디렉토리
converted_data_path = '/gdrive/My Drive/L09/datasets/Stanford_dogs/Images_converted'


# 이미지 변환 함수: jpg인식 오류가 나오므로 jpg --> jpeg 변환
def convert_images_to_jpeg(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp')):
                try:
                    image = Image.open(file_path)
                    # 파일 경로를 새 디렉토리로 변경하고 확장자를 .jpeg로 변경
                    new_file_path = os.path.join(target_dir, os.path.relpath(root, source_dir), os.path.splitext(file)[0] + '.jpeg')
                    new_file_dir = os.path.dirname(new_file_path)
                    if not os.path.exists(new_file_dir):
                        os.makedirs(new_file_dir)
                    image.convert('RGB').save(new_file_path, 'JPEG')
                except (UnidentifiedImageError, OSError) as e:
                    print(f"Cannot identify image file {file_path}. Skipping. Error: {e}")

# 이미지 변환 실행
convert_images_to_jpeg(data_path, converted_data_path)

# 변환된 데이터셋 경로
data_path_converted = pathlib.Path(converted_data_path)


# 데이터셋 로드
train_ds = image_dataset_from_directory(data_path_converted, validation_split=0.2, subset='training', seed=123, image_size=(224, 224), batch_size=16)
test_ds = image_dataset_from_directory(data_path_converted, validation_split=0.2, subset='validation', seed=123, image_size=(224, 224), batch_size=16)

# 모델 구성
base_model = DenseNet121(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

cnn = Sequential()
cnn.add(Rescaling(1.0/255.0))  # 입력 텐서를 0.0 ~ 1.0으로 정규화
cnn.add(base_model)
cnn.add(Flatten())  # 백본 출력 텐서를 1차원으로 flattening
cnn.add(Dense(1024, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(120, activation='softmax'))

cnn.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(learning_rate=0.000001), metrics=['accuracy'])
hist = cnn.fit(train_ds, epochs=30, validation_data=test_ds, verbose=2) # epochs30 이상은 코렙에서 수행 불가...

print('정확률 =', cnn.evaluate(test_ds, verbose=0)[1] * 100)
cnn.save('cnn_for_stanford_dogs.h5')

import pickle
f = open('dog_species_names.txt', 'wb')
pickle.dump(train_ds.class_names, f)
f.close()

import matplotlib.pyplot as plt

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Accuracy graph')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'])
plt.grid()
plt.show()

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Loss graph')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'])
plt.grid()
plt.show()