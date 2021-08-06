import tkinter.messagebox
import tkinter as tk
import os
import keras.models as km
import numpy as np


#预测接口
'''用玫瑰花向日葵模型做测试,导入模型'''
def predication_image(image_name):
    from PIL import Image
    import numpy as np
    '''输入模型路径'''
    model = km.load_model(filepath = r'C:\Users\QQ\Desktop\myModel_roseandsunflower_1.h5')
    obj = ['向日葵', '玫瑰花']

    try:
        img = Image.open(image_name)
        img = img.resize((64, 64))
    
        #调整图片的尺寸以符合数据集图片的规格
        number_data = img.getdata()
        number_data_array = np.array(number_data)
        number_data_array = number_data_array.reshape(1,64,64,3).astype(float)
        number_data_nor = number_data_array / 255
    
        prediction = model.predict(number_data_nor)
        pre_list = prediction.tolist()
        index = np.argmax(prediction)
        #print('向日葵概率为：{0:.5f}%, 玫瑰花概率为：{1:.5f}%'.format(100*pre_list[0][0],100*pre_list[0][1]))
        #print("----------------------------------------------------------------------------------------------------")
        return '向日葵概率为：{0:.3f}%, 玫瑰花概率为：{1:.3f}%'.format(100*pre_list[0][0],100*pre_list[0][1]) + '，预测认为是：'+ obj[index] + '\n' 
    except ValueError:
        tk.messagebox.showerror(title='图片错误', message='你选择的图片尺寸不符合要求，请重新选择')
        return select_image()
    except:
        tk.messagebox.showerror(title='图片错误', message='由于某种原因，你选择的图片无法识别，请重新选择')
