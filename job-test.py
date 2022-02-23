import ray
ray.init()

print("Hello from the driver!")
@ray.remote
def say_hi():
    printf("hello")
    printf("1")
    printf("2")

ray.get([say_hi.remote() for _ in range(5)])
