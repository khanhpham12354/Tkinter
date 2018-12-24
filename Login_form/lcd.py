dic = {'2':"khnh",'3':'222'}
x = {}
x = dic
for i in dic:
	x[i] = dic[i]
del x['2']
print("truoc khi xoa",dic)
print("sau khi xoa",x)