

def item1():
    """
    Know how to slide sequences
    :return: 
    """
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(a[:-3])
    print(a[:3])
    print(a[3:-3])
    print(a[-3:])
    print(a[-3:7])
    print(a[-3:-1])
    b = a[:]  # copies
    print(a == b)
    print(a is not b)
    print(id(a))
    print(id(b))
    print(a[:20])
    print(a[-20:])

    c, d = a[2:4]
    print(c, d)

    a[2:7] = [99, 22, 14]  # Doesn't need to be the same size - truncates list
    print(a)

    print(a[-0:])  # Makes a copy - guard against if 0 is a variable

item1()


def item2():
    """
    Avoid using start, end, and stride in a single slide
    :return: 
    """
    a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    print(a[::2])
    print(a[1::2])

    print(a[::-2])
    print(a[2::2])
    print(a[2::-2])
    print(a[-2::-2])
    print(a[-2:2:-2])

    x = b'mongoose'
    y = x[::-1]
    print(y)

    w = '和平'
    print(w)
    print(w[::-1])
    x = w.encode('utf-8')
    print(x)
    y = x[::-1]
    print(y)
    #z = y.decode('utf-8')  Breaks unicode encoding in byte string


item2()
print('\n\n\n')


def item3():
    """
    Prefer ENUMERATE over RANGE
    :return: 
    """
    from random import randint

    random_bits = 0
    for i in range(64):
        if randint(0, 1):
            random_bits |= 1 << i
    print(bin(random_bits))

    flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
    for flavor in flavor_list:
        print("%s is delicious" % flavor)

    for i in range(len(flavor_list)):
        flavor = flavor_list[i]
        print("%d: %s is delicious" % (i + 1, flavor))

    print(list(enumerate(flavor_list)))  # list exhausts generator
    print(enumerate(flavor_list))  # Returns enumerate object

    for i, flavor in enumerate(flavor_list):
        print('%d: %s' % (i + 1, flavor))

    for i, flavor in enumerate(flavor_list, 1):  # Can start the enumeration with number 1
        print('%d: %s' % (i, flavor))
item3()
print('\n\n\n')


def item4():
    """
    Use ZIP to process iterators in parallel
    :return: 
    """
    names = ['Cecilia', 'Lisa', 'Marie']
    letters = [len(n) for n in names]
    print(letters)

    longest_name = None
    max_letters = 0
    for i in range(len(names)):
        count = letters[i]
        if count > max_letters:
            longest_name = names[i]
            max_letters = count
    print(longest_name)

    print(list(zip(names, letters)))  # zip returns generator

    for name, count in zip(names, letters):
        if count > max_letters:
            longest_name = name
            max_letters = count
    print(longest_name)
    # Python 2, zip is not a generator - use izip from itertools to get generator

    names.append('Rosalind')
    for name, count in zip(names, letters):
        print('%s has %d letters' % (name, count))  # Rosalind isn't printed since letters is exhausted

    from itertools import zip_longest
    for name, count in zip_longest(names, letters):
        if count is None:
            print('%s is of unknown length' % name)
        else:
            print('%s has %d letters' % (name, count))

item4()
print('\n\n\n')


def item5():
    """
    Avoid ELSE blocks after FOR and WHILE loops
    :return: 
    """
    for i in range(3):
        print('Loop %d' % i)
    else:
        print('Else block!')

    for i in range(3):
        print('Loop2 %d' % i)
        if i == 1:
            break
    else:
        print('Else2 block!')

    for x in []:
        print('Never runs')
    else:
        print('Else3 block!')

    while False:
        print('Never runs')
    else:
        print('Else4 block!')

item5()
print('\n\n\n')


def item6():
    """
    Take advantage of each block in TRY/EXCEPT/ELSE/FINALLY
    :return: 
    """
    try:
        #  Do something
        pass
    except:
        #  Handle exception
        pass
    else:
        #  Runs when there are no exceptions
        pass
    finally:
        #  Always runs after try
        pass

    handle = open('random_data.txt', 'w', encoding='utf-8')
    handle.write('success\nand\nnew\nlines')
    handle.close()

    '''
    handle2 = open('random_data4.txt')  # Raise IOError
    
    try:
        data = handle2.read()  # Raise UnicodeDecodeError
    finally:
        handle2.close()
    '''

    import json

    def load_json_key(data, key):
        try:
            result_dict = json.loads(data)  # Raise ValueError
        except ValueError as e:
            raise KeyError from e
        else:
            return result_dict[key]  # Raise KeyError

    try:
        load_json_key('{"foo": bad payload', 'foo')
    except KeyError:
        print('Saw KeyError')

    try:
        load_json_key('{"foo": "bar"}', 'stuff')
    except KeyError:
        print('Saw KeyError')

    print(load_json_key('{"foo": "bar"}', 'foo'))

    def divide_json(path):
        handle = open(path, 'r+')  # IOError
        try:
            data = handle.read()  # UnicodeDecodeError
            op = json.loads(data)  # ValueError
            value = op['numerator'] / op['denominator']  # ZeroDivisionError
        except ZeroDivisionError:
            return None
        else:
            op['result'] = value
            result = json.dumps(op)
            handle.seek(0)
            handle.write(result)  # IOError
            return value
        finally:
            handle.close()  # Always runs

    temp_path = 'random_data.json'
    with open(temp_path, 'w') as handle:
        handle.write('{"numerator": 1, "denominator": 10}')

    print(divide_json(temp_path))
item6()
print('\n\n\n')

def item7():
    """
    Consider CONTEXTLIB and with statements for reusable TRY/FINALLY behavior
    :return: 
    """
    from threading import Lock

    lock = Lock()
    with lock:
        print('Lock is held')

    # Better than this
    lock.acquire()
    try:
        print('Lock is also held')
    finally:
        lock.release()

    import logging
    logging.getLogger().setLevel(logging.WARNING)

    def my_function():
        logging.debug('Some debug info')
        logging.error('A real error!')
        logging.debug('More debugging')

    my_function()

    from contextlib import contextmanager

    @contextmanager
    def debug_logging(level):
        logger = logging.getLogger()
        old_level = logger.getEffectiveLevel()
        logger.setLevel(level)
        try:
            yield
        finally:
            logger.setLevel(old_level)

    with debug_logging(logging.DEBUG):
        my_function()

    my_function()

    @contextmanager
    def swallow_exception(cls):
        try:
            yield
        except cls:
            logging.exception('Swallowing exception')

    value = 20
    #with swallow_exception(ZeroDivisionError):
    #    value /= 0


    with open('random_data.txt', 'w') as handle:
        handle.write('Hello there!')

    @contextmanager
    def log_level(level, name):
        logger = logging.getLogger(name)
        old_level = logger.getEffectiveLevel()
        logger.setLevel(level)
        try:
            yield logger
        finally:
            logger.setLevel(old_level)

    with log_level(logging.DEBUG, 'my-log') as logger:
        logging.debug('This is the global logger')
        logger.debug('This is the my-log logger')


item7()
