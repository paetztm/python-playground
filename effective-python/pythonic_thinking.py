import sys


def item_1():
    """
    Know which version of python you are using
    """
    print(sys.version_info)
    print(sys.version)


def item_2():
    """
    Follow the PEP 8 Style Guide 
    """
    # use pylint for PEP 8 style
    pass


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


def item_3():
    """
    Know difference between str, bytes, and unicode
    """
    my_byte = bytes([72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100])
    my_str = "Hello world"
    print(to_str(my_byte))
    print(to_str(my_str))
    print(to_bytes(my_byte))
    print(to_bytes(my_str))


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


def item_4():
    """
    Write helper functions instead of complex expressions
    """
    from urllib.parse import parse_qs
    my_values = parse_qs('red=5&green=&blue=0', keep_blank_values=True)
    print(repr(my_values))

    # Ugly code
    red = my_values.get('red', [''])[0] or 0
    green = my_values.get('green', [''])[0] or 0

    blue = my_values.get('blue', [''])[0] or 0

    print('Red: {}'.format(red))
    print('Green: {}'.format(green))
    print('Blue: {}'.format(blue))

    # Cleaned up
    green = get_first_int(my_values, 'green')
    print('Green: {}'.format(green))


def item_5():
    """
    Know how to slice sequences
    """

    a = [chr(alpha) for alpha in range(97, 123)]
    print('First four:', a[:4])
    print('Last four:', a[-4:])
    print('Middle Two:', a[12:-12])

    # slices create new lists
    b = a[4:]
    print('Before: ', b)
    b[1] = 99
    print('After: ', b)
    print('No Change', a)

    # copies
    b = a[:]
    assert b == a and b is not a

    b = a
    print('Before', a)
    a[:] = [101, 102, 103]
    assert a is b
    print('After ', a)
item_5()





