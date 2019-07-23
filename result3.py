#coding=utf-8
from urllib import request
import json

def read_http_data(url, data, header, method):
    jdata = None
    if data is not None:
        jdata = json.dumps(data)                  # 对数据进行JSON格式化编码
        jdata=bytes(jdata,'utf8')       #发送json数据需要添加这句
    requests = request.Request(url, jdata, headers = header)
    requests.get_method = method         # 设置HTTP的访问方式
    requests = request.urlopen(requests)
    return requests.read()


def fetchUrl():
	file = open('url3.txt')
	lines = file.readlines()
	aa = []
	with open("result3.txt","a+") as result_txt:
		for line in lines:
			page = 1
			#print(line)
			temp = line.replace('\n','')
			while True:
				url = temp+ "&page=%s"%page
			
				#print(url)
			
				the_page = read_http_data(url, None, {}, lambda:"GET")

				#print(the_page)
			
				result_json_data = json.loads(str(the_page,  encoding = "utf-8"))  #结果转成json数据
				pois = result_json_data["pois"]  #获取pois
				#print("count = %s"%count)
				#print(pois)
				for i in range(len(pois)):
					result_name = pois[i]['name'];
					result_typecode = pois[i]['typecode']
					result_address = pois[i]['address']
					result_location = pois[i]['location']
					result_tel = pois[i]['tel']
					result_type = pois[i]['type']
					result_txt.write("%s , %s , %s , %s , %s , %s , \n"%(result_name,result_typecode,result_address,result_location,result_tel,result_type))
				if int(len(pois)) > 1:
					page = page + 1
				else:
					break
	print('suc')
fetchUrl()