from keras.datasets import mnist 
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Conv2D, MaxPooling2D, Flatten

def loda_data():
    (train_image, train_label), (test_image, test_label) = mnist.load_data()
    return train_image, train_label, test_image, test_label

#build_model(summary=True)
train_image, train_label, test_image, test_label = loda_data()  # 加载数据
train_image_4D = train_image.reshape(60000, 28, 28, 1).astype(float)
test_image_4D = test_image.reshape(10000, 28, 28, 1).astype(float)
#最后的1表示单色域，3表示彩色域
train_image_4D_normalize = train_image_4D/255
test_image_4D_normalize = test_image_4D/255
#标准化
train_label_onehotencoding = np_utils.to_categorical(train_label)
test_label_onehotencoding = np_utils.to_categorical(test_label)
#归一化数据标签

model = Sequential()
#卷积层1建立:
#filters=16:产生滤镜的个数
#kernel_size=(5,5):指定产生滤镜的尺寸
#padding='same':指定不改变图片的大小
#input_shape=(28,28,1):指定输入图片的尺寸规格为28*28*1
model.add(Conv2D(filters=16, kernel_size=(5,5), padding='same', input_shape=(28,28,1),
                 activation='relu'))
#池化层1建立:
#pool_size=(14,14):池化结果
model.add(MaxPooling2D(pool_size=(14,14)))

#卷积层2建立
model.add(Conv2D(filters=36, kernel_size=(5, 5), padding='same',activation='relu'))

#池化层2建立:
model.add(MaxPooling2D(pool_size=(2,2)))

#平坦层建立
model.add(Flatten())

#隐藏层建立
model.add(Dense(units=1000, activation='relu', kernel_initializer='normal', name='hidden'))
model.add(Dropout(0.5))
#建立输出层和隐藏层的关系
model.add(Dense(units=10, activation='softmax', name='output'))

print(model.summary())
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
train_history = model.fit(x=train_image_4D_normalize,y=train_label_onehotencoding, validation_split=0.2, epochs=10, batch_size=200, verbose=2)
plt.plot(train_history.history['accuracy'])
plt.plot(train_history.history['val_accuracy'])
plt.title("Train History")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.show()
model.save("./CNN_Model.h5")