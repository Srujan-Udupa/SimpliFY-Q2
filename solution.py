def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        N, K = map(int, input().split())
        heights = list(map(int, input().split()))
        
        count = 0
        for height in heights:
            if height > K:
                count += 1
        
        results.append(str(count))
    print()
    
    print("\n".join(results))
solve()
