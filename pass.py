import string
import random
if __name__ == '__main__':
    s1 =string.ascii_lowercase
    s2 =string.ascii_uppercase
    s3 =string.punctuation
    s4 =string.digits
    s5 =string.whitespace
    plen=int(input("Enetr the no of digits for your password:\n"))
    s =[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    random.shuffle(s)
    print("Password is:")
    print("".join(s[0:plen]))

