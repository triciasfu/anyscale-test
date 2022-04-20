import ray
import requests

# ray.init("anyscale://snickerdoodle/triciasfu-test")

@ray.remote
class Counter:
    def __init__(self):
        self.counter = 0

    def inc(self):
        self.counter += 1

    def get_counter(self):
        return self.counter

counter = Counter.remote()

for _ in range(5):
    ray.get(counter.inc.remote())
    print(ray.get(counter.get_counter.remote()))

print(requests.__version__)

# cld-k8wcxpgjutse8rvmfzptlukm@anyscale-bridge-e235a270.iam.gserviceaccount.com
