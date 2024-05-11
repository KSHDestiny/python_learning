import re

five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'

five_digit_expression = r'\d{5}'
print(re.search(five_digit_expression, five_digit_zip)) # re.Match object
print(re.search(five_digit_expression, nine_digit_zip)) # re.Match object
print(re.search(five_digit_expression, phone_number))   # none

#! regular expressions
# /text/    specific text
# \d        digit
# \w        word
# .         any character   
# +         one or more character
#- *         zero or more
#- ?         zero or one