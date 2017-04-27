

def item8():
    """
    Use list comprehensions instead of MAP and FILTER
    :return: 
    """
    a = [i for i in range(1, 11)]

    squares = [x**2 for x in a]
    print(squares)
    squares = map(lambda x: x**2, a)  # not as easy to read
    print(list(squares))

    squares = [x**2 for x in a if x % 2 == 0]
    print(squares)

    alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
    print(list(alt))

    chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
    rank_dict = {rank: name for name, rank in chile_ranks.items()}
    print(rank_dict)

    chile_len_set = {len(name) for name in chile_ranks.keys()}
    print(chile_len_set)
item8()


def item9():
    """
    Avoid more than two expressions in list comprehensions
    :return: 
    """
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]
    print(flat)
    squared = [[x**2 for x in row] for row in matrix]
    print(squared)

    matrix3 = [
        [[1, 2, 3], [5, 6, 7]],
        [[7, 8, 9], [10, 11, 12]]
    ]

    flat = [x for sublist1 in matrix3
            for sublist2 in sublist1
            for x in sublist2]
    print(flat)
    flat = []
    for sublist1 in matrix3:
        for sublist2 in sublist1:
            flat.extend(sublist2)
    print(flat)

    a = [x for x in range(1, 11)]
    b = [x for x in a if x > 4 and x % 2 == 0]
    c = [x for x in a if x > 4 if x % 2 == 0]
    print(b)
    print(c)

    filtered = [[x for x in row if x % 3 == 0]
                for row in matrix if sum(row) >= 10]
    print(filtered)

    a = list(range(100))
    b = [x for x in a if x % 2 == 0 if x % 3 == 0]
    print(b)

    b = [x**2 for row in matrix for x in row]
    print(b)

    b = [x**2 for x in a if x % 2 == 0]
    print(b)
item9()


def item10():
    """
    Consider generator expressions for large comprehensions
    :return: 
    """
    import random
    with open('my_file.txt', 'w') as f:
        for _ in range(10):
            f.write('a' * random.randint(0, 100))
            f.write('\n')
    value = [len(x) for x in open('my_file.txt')]
    value_generator_expression = (len(x) for x in open('my_file.txt'))  # use parentheses instead for generator expression
    print(value)
    print(value_generator_expression)
    print(next(value_generator_expression))
    roots = ((x, x**0.5) for x in value_generator_expression)  # totally lazy, value_generator_expression isn't calculated yet
    print(next(roots))
item10()


def item11():
    """
    Consider generators instead of returning lists
    :return: 
    """
    def index_words(text):
        result = []
        if text:
            result.append(0)
        for index, letter in enumerate(text):
            if letter == ' ':
                result.append(index + 1)
        return result

    def index_words_generator(text):
        if text:
            yield 0
        for index, letter in enumerate(text):
            if letter == ' ':
                yield index + 1
        return result
    address = "Four score and seven years ago"
    result = index_words(address)
    print(result)
    generator_result = index_words_generator(address)
    print(next(generator_result))

    def index_words_handle(handle):
        offset = 0
        for line in handle:
            if line:
                yield offset
            for letter in line:
                offset += 1
                if letter == ' ':
                    yield offset

    with open('address.txt', 'w') as f:
        f.write(address)

    with open('address.txt') as f:
        it = index_words_handle(f)
        print(next(it))
        print(next(it))
item11()

def item12():
    """
    Be defensive when iterating over arguments
    :return: 
    """
    data = [15, 80, 35]

    def normalize(numbers):
        # numbers = list(numbers)  # copy iterator but exhausts generator
        if iter(numbers) is iter(numbers):
            raise TypeError('Must supply a container')
        total = sum(numbers)
        result = []
        for value in numbers:
            percent = 100 * value / total
            result.append(percent)
        return result

    output = normalize(data)
    print(output)
    print(sum(output))

    with open('my_numbers.txt', 'w') as f:
        for i in data:
            f.write('%d\n' % i)

    def read_visits(data_path):
        with open(data_path) as f:
            for line in f:
                yield(int(line))

    it = read_visits('my_numbers.txt')
    # print(list(it))
    # print(list(it))
    def normalize_with_iterator(get_iter):
        # numbers = list(numbers)  # copy iterator but exhausts generator
        total = sum(get_iter())
        result = []
        for value in get_iter():
            percent = 100 * value / total
            result.append(percent)
        return result
    get_iter = lambda: read_visits('my_numbers.txt')  # calls and opens file twice
    print(normalize_with_iterator(get_iter))

    class ReadVisits:
        def __init__(self, data_path):
            self.data_path = data_path

        def __iter__(self):
            with open(self.data_path) as f:
                for line in f:
                    yield int(line)

    visits = ReadVisits('my_numbers.txt')

    print(normalize(visits))

item12()
