#list = [1, 2, 3, 4, 5]
#print(*list)
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs.get("idade"))

list = (1, 2, 3, 4, 5)
func(*list, animal="BOI", nome="CAVALO", idade=17000)