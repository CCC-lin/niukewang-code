T=int(input())
for _ in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    x=max(nums)-min(nums)
    avg=sum(nums)/n
    sums=0
    for i in nums:
        sums+=(i-avg)**2
    y=sums/n
    print(f'{x} {y:.3f}')