def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    arr = list(parens)
    if len(arr) % 2 != 0:
        return False
    elif arr.count("(") != arr.count(")"):
        return False
    elif arr[0] != '(' or arr[-1] != ')':
        return False
    else:
        return True
    