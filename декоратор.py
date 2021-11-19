import time



def Time(func):
    def wrap():
        f = open('декоратор.txt', 'w', encoding='utf-8')
        start = time.time()
        print("Start", start)
        end = time.time()
        res = func()
        print("End",end)
        print("Common",end - start)
        f.write("Start", start,"End",end,"Common",end - start)
        f.close()

        return res
    return wrap


@Time
def example():
    print("Middle")
    return 123


print(example())