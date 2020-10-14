def solution(progresses, speeds):
    dday=[]
    max=0
    answer = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]==0:
            dday.append((100-progresses[i])/speeds[i])
        else:
            dday.append(((100-progresses[i])/speeds[i])+1)
        
        if max<dday[i]:
            answer.append(1)
            max=dday[i]
        else:
            answer.append(answer.pop()+1)
    return answer

print(solution([21,25,20],[5,5,5]))