def nth_fibonacci(n):
    if n == 1:
        return(1)
    elif n == 0:
        return(0)
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


def main():

    print (nth_fibonacci(2))
    print (nth_fibonacci(5))

if __name__ == '__main__':
