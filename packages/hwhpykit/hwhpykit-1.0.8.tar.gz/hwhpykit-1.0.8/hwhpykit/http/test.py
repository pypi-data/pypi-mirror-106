

def t(name, *, dic={}):
    return dic

def t2():
    return {}


if __name__ == '__main__':
    t('1', dic={})["a"] = 111
    t('1', dic={})["b"] = 222
    print(t('1', dic={}))

    t2()["√a"] = 111
    t2()["b"] = 222
    print(t2())