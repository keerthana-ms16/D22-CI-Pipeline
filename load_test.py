import concurrent.futures
from app import add


def user_request(user_id):
    result = add(user_id, 10)
    return result


print("Load Test Started")

users = 10

with concurrent.futures.ThreadPoolExecutor(max_workers=users) as executor:
    results = list(executor.map(user_request, range(users)))

print("Number of simulated users:", users)
print("Requests completed:", len(results))

assert len(results) == users+1, "Load test failed"

print("Load test passed")