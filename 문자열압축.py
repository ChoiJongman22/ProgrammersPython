def solution(s):
    answer = 0
    size=len(s)
    for i in range(size):
        print(i)
        part=s[0:i+2]
        last=""
        comp=""

        count=1
        for j in range(i+1,size):
            comp=s[j:i+1]
            if part==comp:
                count+=1
            else:
                if count==1:
                    last+=part
                    part=comp
                else:
                    last=last+count+part
                    part=comp
                    count=1

            if i+j>=size:
                if(count==1):
                    last+=
    return answer


solution('aaabbbbb')