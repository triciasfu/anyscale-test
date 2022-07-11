import ray
import anyscale.job

@ray.remote
def hello_world():
    return "Hello World!"

result = ray.get(hello_world.remote())

anyscale.job.output({
  "result": result
})
