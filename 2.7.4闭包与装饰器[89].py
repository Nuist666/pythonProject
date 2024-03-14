# 将outer()函数的返回值指定为inner()函数本身
def outer():
    def inner():
        print("I'm inner func")

    print("I'm outer func")
    return inner


func = outer()
print('下面执行func')
func()
