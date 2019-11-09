from singleton import SingletonTest


def main():
    print('Start.')
    obj1 = SingletonTest()
    obj2 = SingletonTest()
    print(obj1, obj2)
    if obj1 == obj2:
        print('obj与obj2是相同的实例。')
    else:
        print('obj与obj2是不同的实例。')
    print('End.')


if __name__ == '__main__':
    main()
