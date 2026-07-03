block_list = ['renil@gmail.com', 'mandip@gmail.com', 'abc@gmail.com', 'xyz@gmail.com']

email = 'mandip@gmail.com'

if email not in block_list:
    print('its not spam email')
else:
    print("its spam email")