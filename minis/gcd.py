for _ in range(int(input())):
    # n = int(input())
    n, k = map(int, input().split())
    
    for i in range(n, 0, -1):
        if i % k == 0:
            st = i // k
            print(*[(j + 1) * st for j in range(k)])
            break
    