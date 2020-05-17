import requests
import sys
global input_content
def get_type_list():
    '''获取类型列表'''
    # 中译英、英译中和其他语言翻译为中文都归为AUTO
    type_list = ['AUTO', 'ZH_CN2JA', 'ZH_CN2KR', 'ZH_CN2FR', 'ZH_CN2RU', 'ZH_CN2SP']
    return type_list

def select_trans_type():
    '''选择翻译类型'''
    
    type_num = (input("提供的翻译类型有：\n1.自动检测（中英互译+其他语言译中), \n2.中->日\n3.中->韩\n4.中->法\n5.中->俄\n6.中->西\
                         \n7.结束翻译请输入#\n请输入您选择类型的字符:"))
    if type_num in ['1','2','3','4','5','6']:
        type_num = int(type_num)
        return type_num
    elif type_num == '#':
        return type_num
    else:
        print('\n','*'*46,'请输入上述类型对应的字符!','*'*46,'\n')
        return select_trans_type()

def translate(url, data):
    '''翻译内容，返回结果'''
    #模拟浏览器，抗反爬
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple"
                   "WebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    # 爬给定网页内容，得到响应的json内容
    response = requests.get(url, headers=headers, params=data).json()
    # 获取翻译结果
    trans_result = response['translateResult'][0][0]['tgt']
    print(input_content,'->',trans_result)

if __name__ == '__main__':
    # 翻译链接网站
    url = 'http://fanyi.youdao.com/translate'

    # 翻译主体
    while True:
        type_num = select_trans_type()
        if type_num == '#':
            print('\n','*'*44,'感谢您的使用，欢迎再次使用！','*'*44,'\n')
            sys.exit()
        input_content = input("\n请输入要翻译的文本(重选类型请输入:*，结束翻译请输入:#)：")
        if input_content == '#' or type_num == '#':
            print('\n','*'*44,'感谢您的使用，欢迎再次使用！','*'*44,'\n')
            sys.exit()
        elif input_content == '*':
            continue
        data = {
            "doctype": "json",
            "type": get_type_list()[type_num-1],
            "i": input_content
        }
        translate(url, data)
        print('-'*100)

