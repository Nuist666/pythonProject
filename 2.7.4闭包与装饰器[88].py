# 闭包
def outer():
    def inner():
        print("I'm inner func")

    print("I'm outer func")
    inner()


outer()
