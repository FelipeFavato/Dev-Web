import requests
# import time

# response = requests.get("http://www.betrybe.com/")
# print(response.status_code)
# print(response.headers['Content-Type'])
# print(response.text)
# response = requests.post("http://httpbin.org/post", data="some content")
# print(response.text)
# response = requests.get(
#     "http://httpbin.org/get", headers={"Accept": "application/json"})
# print(response.text)
# response = requests.get("http://httpbin.org/get")
# print(response.json())

# response = requests.get("http://httpbin.org/status/404")
# response.raise_for_status()


# for _ in range(15):
#     response = requests.get("http://www.cloudflare.com/rate-limit-test/")
#     time.sleep(2)
#     print(response)

try:
    response = requests.get("http://...", timeout=2)
except requests.ReadTimeout:
    response = requests.get("http://...", timeout=2)
finally:
    print(response.status_code)
