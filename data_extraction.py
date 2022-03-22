import re
import json

def normalize(num):
    # print("before norm", num)
    num = str(int(num)).zfill(len(num)) #converts burmese to eng integer and filling leading zero
    if num.startswith('+959'):
        # print('true')
        num=num.replace('+959','09')
        # print("num",num)
        return num
    else:
        return num

f = open('mmphonenum.json')
data = json.load(f)

#{'prefix': '95', 'length': 9, 'operator': 'Ooredoo', 'type': ''}

def check_operator(ph_num):
    for i in data['data']:
        # print('i',i)
        # print('prefix',i['prefix'])
        # print(ph_num[2:4])
        if i['prefix'] == ph_num[2:4]:
            # print('Operator',i['operator'])
            operator = i['operator']
            return operator
        # break
# check_operator()

regex_file = open('regex.json')
r_data = json.load(regex_file)

def get_phone_data(string):

    ph_num= re.findall(r_data['phone_num'], string)
    ph_num = list(map(lambda x: normalize(x), ph_num))

    if len(ph_num)==1:
        ph_num = ' '.join(ph_num)
        print('The extracted phone number : {} and operator is {}'.format(ph_num, check_operator(ph_num)))
    else:
        ph_num = ','.join(ph_num)
        print('The extracted phone numbers : {} and operator is {}'.format(ph_num, check_operator(ph_num)))
    
