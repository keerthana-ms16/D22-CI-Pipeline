import time
from app import add


start_time = time.time()

for i in range(100000):
    add(i, i)

end_time = time.time()

execution_time = end_time - start_time

print("Performance Test")
print("Execution Time:", execution_time, "seconds")

assert execution_time < 1.0, "Performance test failed"

print("Performance test passed")