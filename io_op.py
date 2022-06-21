def io_op():
    f = open('./data/test.txt', 'a+', encoding='utf-8')
    data = f.write('\n' 'g234')
    f.seek(0)
    read1 = f.read()
    print(read1)
    f.close()


def one_by_one():
    f = open('./data/test.txt', encoding='utf-8')
    line = f.readline()
    while line:
        s = line.__str__().replace('\n', '')
        f2 = open('./data/' + s + '.md', 'a+', encoding='utf-8')
        f2.write('# ' + s)
        print('- [' + s + '](./' + s + '.md)')
        line = f.readline()
    f.close()


if __name__ == '__main__':
    # io_op()
    one_by_one()
