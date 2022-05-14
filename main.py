def AAAA(qwert):

    def BBBB():
        q = "результат от %s это % s" % (qwert(),
            eval(qwert())
            )

        return q

    return BBBB()

def DDDD():
    return '1000000000000 + 1'


if __name__ == "__main__":
    value = DDDD()
    print(value)
    decorator = AAAA(DDDD)
    print(decorator)
    