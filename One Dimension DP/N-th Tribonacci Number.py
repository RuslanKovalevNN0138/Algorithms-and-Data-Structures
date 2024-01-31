

def tribonacci(n:int)->int:
    """
    return n tribonacci number
    dp[n]=dp[n-1]+dp[n-2]+dp[n-3]
    :type n: int
    :type: int
    """
    if n<2:
        return n
    if n==2:
        return 1

    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=1

    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]

if __name__=="__main__":
    n=int(input())
    a=tribonacci(n)
    print(tribonacci(n))
