import pandas as pd
import numpy as np
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
import matplotlib.pyplot as plt

all_df = pd.read_excel("titanic3.xls") 
cols = ['survived', 'name', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare']
all_df = all_df[cols]

#将all_df分为80%左右的训练部分和20%左右的测试部分
mask = np.random.random(len(all_df)) < 0.8
train_df = all_df[mask]
test_df = all_df[~mask]
def PreprocessData(raw_df):
    df = raw_df.drop(['name'], axis = 1)
    age_mean = df['age'].mean()
    df['age'] = df['age'].fillna(age_mean)
    fare_mean = df['fare'].mean()
    df['fare'] = df['fare'].fillna(fare_mean)
    df['sex'] = df['sex'].map({'female':0, 'male':1})
    narray = df.values
    Label = narray[:, 0]
    Feature = narray[:, 1:]
    minmax_scaler = preprocessing.MinMaxScaler((0, 1))
    scaledFeatures = minmax_scaler.fit_transform(Feature)
    return scaledFeatures, Label

#将训练部分和测试部分带入函数中，提取特征和标签
train_Feature, train_Label = PreprocessData(train_df)
test_Feature, test_Label = PreprocessData(test_df)

#Sequential:建立一个线性堆叠的模型
model = Sequential()
model.add(Dense(units = 1000, input_dim = 6, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dense(units = 1000, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dense(units = 1, kernel_initializer = 'normal', activation = 'sigmoid'))
#model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
train_history = model.fit(train_Feature, train_Label, validation_split=0.2, epochs=60, batch_size=20, verbose=2)

#绘制曲线
plt.plot(train_history.history['accuracy'])
plt.plot(train_history.history['val_accuracy'])
plt.title("Train History")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.show()
socres = model.evaluate(test_Feature, test_Label)
print(socres)

Jack = pd.Series([0, 'Jack', 3, 'male', 22, 1, 0, 5]) 
Rose = pd.Series([1, 'Rose', 1, 'female', 20, 2, 1, 200])
JR_df = pd.DataFrame([list(Jack), list(Rose)], columns=['survived', 'name', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare'])

#将Jack和Rose的数据信息，追加到原有数据集的末尾
all_df = pd.concat([all_df, JR_df])
all_Feature, all_Label = PreprocessData(all_df)
all_probability = model.predict(all_Feature)
all_probability[-2:]
all_df.insert(len(all_df.columns), 'probability', all_probability)

#找出数据集中生还率大于90%，但是却遇难的人员
all_df[(all_df['survived'] == 0)&(all_df['probability'] > 0.8)]