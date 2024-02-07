import timeit
import sys


def test_dict_lookup(size):
    dict_ = {n: n for n in range(size)}
    start = timeit.default_timer()
    for i in range(size):
        if i in dict_:
            pass
    end = timeit.default_timer()
    return (end - start) / size


def test_set_lookup(size):
    set_ = set(range(size))
    start = timeit.default_timer()
    for i in range(size):
        if i in set_:
            pass
    end = timeit.default_timer()
    return (end - start) / size


def test_tuple_lookup(size):
    tuple_ = tuple(range(size))
    start = timeit.default_timer()
    for i in range(size):
        if i in tuple_:
            pass
    end = timeit.default_timer()
    return (end - start) / size


def test_list_lookup(size):
    list_ = [n for n in range(size)]
    start = timeit.default_timer()
    for i in range(size):
        if i in list_:
            pass
    end = timeit.default_timer()
    return (end - start) / size


def do_test(size):
    print("Set lookup time:   ", test_set_lookup(size))
    print("Tuple lookup time: ", test_tuple_lookup(size))
    print("Dict lookup time:  ", test_dict_lookup(size))
    print("List lookup time:  ", test_list_lookup(size))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please supply the size of the collections to test")
        sys.exit(1)
    size = int(sys.argv[1])
    do_test(size)
