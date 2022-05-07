def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    st1 = set(str1)
    st2 = set(str2)

    obj1 = {num: str1.count(num) for num in st1}
    obj2 = {num: str2.count(num) for num in st2}

    return obj1 == obj2
