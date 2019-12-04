
from manager import Manager
from message_box import MessageBox
from underline_pen import UnderlinePen


def main():
    # ready
    manager = Manager()
    upen = UnderlinePen('~')
    mbox = MessageBox('*')
    sbox = MessageBox('/')
    manager.register('strong message', upen)
    manager.register('warning box', mbox)
    manager.register('slash box', sbox)

    # create
    p1 = manager.create('strong message')
    p1.use('Hello, world.')
    p2 = manager.create('warning box')
    p2.use('Hello, world.')
    p3 = manager.create('slash box')
    p3.use('Hello, world.')


if __name__ == '__main__':
    main()
