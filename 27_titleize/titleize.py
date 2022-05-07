def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_arr = phrase.split(" ")
    mod_arr = [word.capitalize() for word in new_arr]
    return " ".join(mod_arr)