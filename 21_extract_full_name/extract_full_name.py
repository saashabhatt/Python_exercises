def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    k = len(people)
    fir = []
    las = []
    res = []
    for x in range(0,k):
        fir.append(people[x]['first'])
        las.append(people[x]['last'])
        res.append(fir[x] + " " + las[x])

    return res