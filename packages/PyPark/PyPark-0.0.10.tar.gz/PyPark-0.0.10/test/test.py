import time
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

import requests

# 并发数
MAX_WORKERS = 10

RESULT_SUCCESS = []
RESULT_ERROR = []


def run(A):
    r = requests.post("http://172.16.72.91:5253/BBBB", json={"A": A}, timeout=300, headers={
        "Content-Type": "application/json;charset=UTF-8"})
    if r.status_code == 200:
        if r.json()["is_success"]:
            RESULT_SUCCESS.append("success")
        else:
            RESULT_ERROR.append(r.text)
    else:
        RESULT_ERROR.append(r.text)


def runA(A):
    r = requests.post("http://172.16.72.91:10000/AAA", json={"a": A, "b": A}, timeout=300, headers={
        "Content-Type": "application/json;charset=UTF-8"})
    if r.status_code == 200:
        if r.json()["is_success"]:
            RESULT_SUCCESS.append("success")
        else:
            RESULT_ERROR.append(r.text)
    else:
        RESULT_ERROR.append(r.text)


start = time.time()
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as t:
    all_task = [t.submit(runA, page) for page in range(0, MAX_WORKERS)]
    wait(all_task, return_when=FIRST_COMPLETED)

print("总用时：", time.time() - start)
print("RESULT_SUCCESS", len(RESULT_SUCCESS))
print("RESULT_ERROR", len(RESULT_ERROR))
