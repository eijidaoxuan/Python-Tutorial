def spam(x):
    for i in range(x):
        yield "#"*i                 #yield = returning one by one as system typing  (can not lag if spaming)

def spam1(x):
    z = []
    for i in range(x):
        z.append("#"*i)
    return z                        #return = returning all at once    (lag if spaming)

def main():
    n = int(input("How many times: "))
    for i in spam(n):
        print (i)
    for i in spam1(n):
        print (i)

main()