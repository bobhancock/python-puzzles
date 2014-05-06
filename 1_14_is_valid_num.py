def is_valid_rational(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True
    
print(is_valid_rational("3.14"))
print(is_valid_rational("0.93949"))
print(is_valid_rational("39"))
print(is_valid_rational("-0.4"))
print(is_valid_rational("1/8"))

      
    