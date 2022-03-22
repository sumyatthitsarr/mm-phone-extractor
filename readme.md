# Extract phone number from text using RegEx pattern

## Example Usage 1

```
from data_extraction import get_phone_data

test_str = 'ဖုန်းနံပါတ် ၀၉၇၅၃၆၁၂၈၄၂ ကို ဆက်ပေးပါဗျ' 

get_phone_data(test_str)
```

This should print:

```
The extracted phone number : 09753612842 and operator is Telenor
```

This works on extracting phone numbers written in both Burmese and English.

## Example Usage 2

```
from data_extraction import get_phone_data

test_str = 'My number is 09421145678 and ...' 

get_phone_data(test_str)
```

This should print:

```
The extracted phone number : 09421145678 and operator is MPT
```
