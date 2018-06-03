

def getDictfrStr(string):
    """ if splitting give us odd numbers of keys and values \
    with ':' in the end of string, then last value will be ''"""
    l=string.split(':')
    shift = 2 if len(l) % 2 else 1
    return {l[i]: l[i + 1] for i in range(0,len(l) - shift,2)}

def main():
    print(getDictfrStr('k1:v1:k2:v2'))

if __name__=="__main__":
    main()