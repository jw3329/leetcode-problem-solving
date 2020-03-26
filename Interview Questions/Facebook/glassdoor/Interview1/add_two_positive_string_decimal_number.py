

def add_two_positive_string_decimals(s1,s2):
    s1_integer, s1_decimal = s1.split('.')
    s2_integer, s2_decimal = s2.split('.')
    len_small = s1_decimal if len(s1) < len(s2) else s2_decimal
    len_large = s2_decimal if len_small == s1_decimal else s1_decimal
    while len(len_small) != len(len_large):
        len_small = len_small + '0'
    decimal_addition = add_two_positive_string_integers(len_small, len_large)
    carry = '1' if len(decimal_addition) != len(len_large) else '0'
    return add_two_positive_string_integers(add_two_positive_string_integers(s1_integer,carry),s2_integer) + '.' + (decimal_addition[1:] if carry == '1' else decimal_addition)
    

        
        

def add_two_positive_string_integers(s1,s2):
    if not s2 or s2 == '0': return s1
    if len(s1) < len(s2): return add_two_positive_string_integers(s2,s1)
    # assume s1 in length is always larger
    last_digit_added = int(s1[-1]) + int(s2[-1])
    carry = last_digit_added // 10
    digit = last_digit_added % 10
    return add_two_positive_string_integers(add_two_positive_string_integers(s1[:-1],str(carry)),s2[:-1]) + str(digit)


# print(add_two_positive_string_integers('002345141412','1234500'))

print(add_two_positive_string_decimals('123.56243','34567.192830153'))