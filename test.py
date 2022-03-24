from data_extraction import get_phone_data, get_nrc_data

# test_str = 'My number is +959982453277 and 09982453279'
# test_str = 'My number is +959982453277'
# test_str = 'ဖုန်းလေးက ၀၉၇၅၃၆၁၂၈၄၂' 
# test_str = 'My number is 09421145678'

# get_phone_data(test_str)

test_str = 'My National ID card number is 9/MAKANA(Naing)000333'
test_str = 'မှတ်ပုံတင်အမှတ် ၉/မကန(နိုင်)၀၀၀၀၂၅'

print('NRC number is {}'.format(get_nrc_data(test_str)))
