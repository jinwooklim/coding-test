import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        if len(scoville) <= 1 and scoville[0] < K:
            return -1

        if scoville[0] >= K:
            return cnt

        new = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new)
        cnt += 1


if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    res = solution(scoville, K)
    print(res)
