from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda x:(x[1],x[0]))
        print(people)
        for i in range(len(people)):
            v,cnt = people[i]
            j = 0
            while(j<len(ans) and (ans[j][0]<v or cnt>0)):
                if ans[j][0]>=v:
                    cnt -=1
                j+=1
            ans.insert(j, people[i])
            
        return ans

if __name__ == "__main__":
    t = Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
    print(t)