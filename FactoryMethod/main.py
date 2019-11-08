from idcard_factory import IDCardFactory


def main():
    factory = IDCardFactory()
    card1 = factory.create('Alvin')
    card2 = factory.create('Bob')
    card3 = factory.create('Cherry')
    card1.use()
    card2.use()
    card3.use()
    print(factory.get_owners())


if __name__ == '__main__':
    main()
