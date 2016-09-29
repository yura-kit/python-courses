import math

vowels = ('a', 'e', 'i', 'o',  'u')

# just some comment
def is_vovel(char):
    return (char.lower() in vowels)


def clip(lo, x, hi):
    print(min(max(x, lo), hi))


def polysum(n, s):
    area = 0.25*n*s**2/math.tan(math.pi/n)
    perimeter = n*s
    return (area + perimeter**2)


if __name__ == '__main__':

    print("check clip function:")
    clip(-1.62, -6.63, 1.64)
    clip(-3.09, 3.51, 4.56)

    print('check is_vovel function: ' + str(is_vovel('E')))
    print('check is_vovel function: ' + str(is_vovel('e')))
    print('check is_vovel function: ' + str(is_vovel('uue')))

    print('check polysum: %0.4f' % polysum(22, 28))
