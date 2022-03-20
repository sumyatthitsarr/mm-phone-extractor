import re

phone_regex = '\+?95[0-9]{9}|09[0-9]{9}'

# test_str = 'My number is +959982453277 and 09982453279'
test_str = 'My number is +959982453277'

ph_num= re.findall(phone_regex, test_str)

if len(ph_num)==1:
    ph_num = ' '.join(ph_num)
    print('The extracted phone number : {}'.format(ph_num))
else:
    ph_num = ','.join(ph_num)
    print('The extracted phone numbers : {}'.format(ph_num))
    