# def solution(skill, skill_trees):
#     answer = 0
#     sk=dict()
#     for i in range(len(skill)):
#        sk[skill[i]]=i+1


        
#     for skill_tree in skill_trees:
#         cnt=1
#         check=True
#         for s in skill_tree:
#            if(sk[s] & sk[s]>cnt):
#               check=False
#               break
#            elif(sk[s] & sk[s]==cnt):
#               cnt+=1

#         if check==True:
#             answer+=1


#     return answer

def solution(skill, skill_trees):
   answer = 0
   #list comprehension
   for skill_tree in skill_trees:
         a=[skill_tree.index(i) for i in skill if i in skill_tree]
         print(a)
         a_=sorted(a)
         if a ==a_ and all(i in skill_tree for i in skill[:len(a)]):answer+=1
   
   return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))