def safe_divide(numerator, denominator) :
    try:
        num= float(numerator)
        dem =  float(denominator)
    except ZeroDivisionError:
        return "sorry the number cant be divided by zero"
    except ValueError :
        return "it is a string can be use in  numbers please"
