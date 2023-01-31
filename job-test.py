import ray
ray.init()

print("Hello from the driver!")
@ray.remote
def say_hi():
    print("hello")
    f = open("/mnt/user_storage/some_file.txt")
    f.write("Now the file has more content!")
    f.close()
    print("1")
    print("2")

ray.get([say_hi.remote() for _ in range(5)])
