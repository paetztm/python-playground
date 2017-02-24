import operator


def num_rows(d):
    '''
    Get number of data rows. Raise ValueError if not all columns have the same number of rows.
    '''
    if len(d) == 0:
        return 0

    def gen_columns():
        for v in d.values():
            yield v
    columns = gen_columns()
    length = len(next(columns))
    for index, column in enumerate(columns, 1):
        if len(column) != length:
            raise ValueError(index)
    return length


def pprint_dataset(dataset):
    '''
    Render the contents of a Dataset nicely, as a string.
    '''
    # helpers
    def width_of(label):
        width = max(len(str(value)) for value in dataset.data[label])
        width = max([width, len(str(label))])
        return width
    def format(value, label):
        return '{value:>{width}}'.format(value=str(value), width=field_widths[label])

    # precompute
    field_widths = {label: width_of(label) for label in dataset.labels}
    table_width = sum(width for width in field_widths.values()) + 3 * (len(dataset.labels)-1) + 4
    HR = '-' * table_width

    # render lines
    labels_line = '| ' + ' | '.join(format(label, label) for label in dataset.labels) + ' |'
    lines = [
        HR,
        labels_line,
        HR,
    ]
    for row_number in range(dataset.length):
        formatted_values = (format(dataset.data[label][row_number], label) for label in dataset.labels)
        lines.append('| ' + ' | '.join(formatted_values) + ' |')
    lines.append(HR)
    return '\n'.join(lines)


class Dataset:
    def __init__(self, data: dict):
        self.data = data
        self.length = num_rows(data)
        self.labels = sorted(data.keys())

    def __str__(self):
        return pprint_dataset(self)

    def __getattr__(self, label):
        if label not in self.data:
            raise AttributeError("'{} object has no attribute '{}'".format(self.__class__.__name__, label))
        return LabelReference(label)

    def __getitem__(self, comparison):
        filtered_data = dict((label, [])
                             for label in self.labels)

        # Internal helper function.
        def append_row(row_number):
            for label in self.labels:
                value = self.data[label][row_number]
                filtered_data[label].append(value)

        # Now add in rows.
        for row_number in range(self.length):
            if comparison.apply(self.data, row_number):
                append_row(row_number)
        return Dataset(filtered_data)


class LabelReference:
    def __init__(self, label: str):
        self.label = label

    def __gt__(self, other):
        return Comparison(self.label, other, operator.gt)

    def __lt__(self, other):
        return Comparison(self.label, other, operator.lt)

    def __ge__(self, other):
        return Comparison(self.label, other, operator.ge)

    def __le__(self, other):
        return Comparison(self.label, other, operator.le)

    def __eq__(self, other):
        return Comparison(self.label, other, operator.eq)


class GeneralComparison:
    def __and__(self, other):
        return Conjunction(self, other, logical_and)

    def __or__(self, other):
        return Conjunction(self, other, logical_or)

    def __init__(self, lookup, value, operate):
        self.lookup = lookup
        self.value = value
        self.operate = operate

    def apply(self, data, row_number):
        other_value = self.lookup(data, row_number)
        return self.operate(other_value, self.value)


class Conjunction:
    '''
    Represents a logical "and" or "or" relationship between two expressions.
    combine will generally be set to either logical_and or logical_or.
    '''
    def __init__(self, left: GeneralComparison, right: GeneralComparison, combine: 'func'):
        self.left = left
        self.right = right
        self.combine = combine

    def apply(self, data: dict, row_number: int):
        return self.combine(self.left.apply(data, row_number), self.right.apply(data, row_number))


class Comparison(GeneralComparison):
    def __init__(self, label, value, operate):
        self.label = label
        self.value = value
        self.operate = operate

    def apply(self, data, row_number):
        other_value = data[self.label][row_number]
        return self.operate(other_value, self.value)


class PairedLabelReference(LabelReference):
    def __init__(self, first: LabelReference, second: LabelReference, operate: 'func'):
        self.first = first
        self.second = second
        self.operate = operate

    def lookup(self, data: dict, row_number: int):
        first_value = data[self.first.label][row_number]
        if isinstance(self.second, LabelReference):
            second_value = data[self.second.label][row_number]
        else:
            second_value = self.second
        return self.operate(first_value, second_value)

    def compare(self, value, operate: 'func'):
        return GeneralComparison(self.lookup, value, operate)


class Triplet:
    def __init__(self, a, b, c):
        self._data = {"a": a, "b": b, "c": c}

    def __getitem__(self, item):
        return self._data[item]


def logical_and(a, b):
    return a and b


def logical_or(a, b):
    return a or b




ds = Dataset({
    'A': [-137, 22, -3, 4, 5],
    'B': [10, 11, 121, 13, 14],
    'C': [3, 6, 91, 12, 15],
})
print(ds)

print(ds.A)

triplet = Triplet(10, 20, 30)
print("b is: {}".format(triplet["b"]))

print(ds[ds.B >= 12])

print(ds[(ds.A > 0) & (ds.B >= 12)])

