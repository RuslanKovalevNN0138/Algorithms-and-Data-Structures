
def longest_common_subsequence(text_1,text_2):

    len_1,len_2=len(text_1),len(text_2)

    dp=[[0]*(len_1+1) for i in range(len_2+1)]

    for i in range(1,len_2+1):
        for j in range(1,len_1+1):
            if text_2[i-1]==text_1[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(dp[len_2][len_1])
    print(dp)

if __name__=="__main__":
    longest_common_subsequence("abcde","ace")
    
