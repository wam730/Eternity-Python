import requests
def start():
	cookies = {
		'MUSIC_U': '31b2af9d20b96304785c59cc9808f530b37639b7eb569e50b1b032d14717ef034f04614efa762751561d2ab6e4c37528b4c6e05649d650bf',
		'__csrf':'134b147d11ff6373410ca3f0900f7cbb; ntes_kaola_ad=1',
	}
	res = requests.post('http://wyy.52blog.cf:88/api.php?do=sign', cookies=cookies)
	resp = requests.get('http://wyy.52blog.cf:88/api.php?do=daka', cookies=cookies)
	print(res.text,resp.text)
def main_handler(event, context):
	return start()
if __name__ == '__main__':
	start()
