from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.datasets import cifar10

(train_image, train_label), (test_image, test_label) = cifar10.load_data()

print("train_data = ", len(train_image))
print("test_data = ", len(test_image))
#归一化
train_image_4d_nor = train_image.reshape(50000, 32, 32, 3).astype(float) / 255
test_image_4d_nor = test_image.reshape(10000, 32, 32, 3).astype(float) / 255
#标签一位有效编码转换
train_label_ohc = np_utils.to_categorical(train_label)
test_label_ohc = np_utils.to_categorical(test_label)
#建立模型
model = Sequential()
#卷积层1、池化层1
model.add(Conv2D(input_shape=(32,32,3), filters = 16, kernel_size = (5, 5), padding = 'same', activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
#卷积层2、池化层2
model.add(Conv2D(filters=36, kernel_size=(5, 5), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#卷积层3、池化层3
#model.add(Conv2D(filters=36, kernel_size=(5, 5), padding='same', activation='relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#平坦层
model.add(Flatten())
#隐藏层1
model.add(Dense(units=512, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dropout(0.5))
#隐藏层2
#model.add(Dense(units=256, kernel_initializer = 'normal', activation = 'relu'))
#model.add(Dropout(0.5))
#输出层
model.add(Dense(units = 10, kernel_initializer = 'normal', activation = 'softmax'))
print(model.summary())
#训练
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
train_history = model.fit(train_image_4d_nor, train_label_ohc, validation_split=0.2, epochs=30, batch_size=200, verbose=2)
#绘制图像
plt.plot(train_history.history['accuracy'], 'r', label = 'accuracy')
plt.plot(train_history.history['val_accuracy'], 'b', label = 'val_accuracy')
plt.title("Train History")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()
#打印准确率
socres = model.evaluate(test_image_4d_nor, test_label_ohc)
print(socres)
#保存模型
model.save("myModelofCNN.h5")