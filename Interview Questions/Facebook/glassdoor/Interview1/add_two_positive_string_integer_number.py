

def add_two_positive_string_integers(s1,s2):
    if not s2 or s2 == '0': return s1
    if len(s1) < len(s2): return add_two_positive_string_integers(s2,s1)
    # assume s1 in length is always larger
    last_digit_added = int(s1[-1]) + int(s2[-1])
    carry = last_digit_added // 10
    digit = last_digit_added % 10
    return add_two_positive_string_integers(add_two_positive_string_integers(s1[:-1],str(carry)),s2[:-1]) + str(digit)


print(add_two_positive_string_integers('123','34567'))