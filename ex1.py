# 1. The email must have address@domain.extension format type. The address part can only contains letters, digits, dashes, and underscores [a-z], [A Z], [0-9], [_-]

import re

input_emails = ["abc@gmail.com", "123$tt*@xyz.com", "good@bad@uk.in", "nasa@usa12.space", "no-reply@domain.in", "ramhanuman@saketa.lok", "ruhi.mohan@exter123.123", "fake@fake123.fakercom"]
output_emails = []

for email in input_emails:
    address = re.findall("^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+.[a-zA-Z]{2,}$", email)
    

for email in input_emails:
    if address:
        output_emails.append[email]
    else:
        print("Invalid Email.")