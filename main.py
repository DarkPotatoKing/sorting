from sorting_hat import SortingHat
import sys

def main():
    s = SortingHat()
    code = 0

    if len(sys.argv) > 1:
        code = int(sys.argv[1])

    if code == 0:
        s.start()
    elif code == 1:
        s.load()
        s.sort_students()
    else:
        print 'Invalid code!'


if __name__ == '__main__':
    main()