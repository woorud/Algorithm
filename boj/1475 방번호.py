n = input()
dic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}


for i in range(len(n)):
    if n[i] in ['6', '9']:
        dic['6'] += 1
    else:
        dic[n[i]] += 1
dic['6'] = (dic['6']//2) + (dic['6']%2)
print(max(dic.values()))
