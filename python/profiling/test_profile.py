COUNT=10000
TIME = 3


@profile
def xrange_test():
    ret = 0
    for i in xrange(COUNT):
        ret += i
    return ret


@profile
def range_test():
    ret = 0
    for i in range(COUNT):
        ret += i
    return ret


def run_main():
    for j in xrange(TIME):
        xrange_test()
        range_test()


if __name__ == '__main__':
    run_main()
