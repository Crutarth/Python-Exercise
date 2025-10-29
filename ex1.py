# 1. The email must have address@domain.extension format type. The address part can only contains letters, digits, dashes, and underscores [a-z], [A Z], [0-9], [_-]
#   The domain can only have letters and digits [a-z], [A-Z], [0-9]
#   The extension can only contains letters [a-Z], [A-Z]. The minimum length of extension can be 2 and maximum length can be 3.

# Input: emails = [abc@gmail.com, 123$tt*@xyz.com, good@bad@uk.in, nasa@usa12.space, no-reply@domain.in, ramhanuman@saketa.lok, ruhi.mohan@exter123.123, fake@fake123.fakercom]
# Output: emails = [abc@gmail.com, nasa@usa12.space, no-reply@domain.in, ramhanuman@saketa.lok]

import re

input_emails = ["abc@gmail.com", "123$tt*@xyz.com", "good@bad@uk.in", "nasa@usa12.space", "no-reply@domain.in", "ramhanuman@saketa.lok", "ruhi.mohan@exter123.123", "fake@fake123.fakercom"]
output_emails = []

for email in input_emails:
    address = re.findall("^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+.[a-zA-Z]{2,5}$", email)
    if address:
        output_emails.append(email)
print(output_emails)