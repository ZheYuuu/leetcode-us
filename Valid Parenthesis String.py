class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.helper(s, 0, 0, 0)
    
    def helper(self, s, l, r, idx):
        if r>l:
            return False
        if idx==len(s):
            return l==r
        c = s[idx]
        if c=='*':
            ans =  self.helper(s, l+1, r, idx+1) or self.helper(s, l, r+1, idx+1) or self.helper(s, l, r, idx+1)
        elif c=='(':
            ans =  self.helper(s, l+1, r, idx+1)
        else:
            ans =  self.helper(s, l, r+1, idx+1)

    def checkValidString(self, s: str) -> bool:
        l,r = 0
        star = 0
        for c in s:
            if c==')':
                l -= 1
            elif c=='(':
                l += 1
            else:
                star +=1
            if l<0:
                if star>0:
                    star -= 1
                else:
                    return False
        # 此法不可行的原因在于 可能最后一个( 的位置比最后一个 * 的位置靠后
        return star>=l
    
    def checkValidString(self, s):
        left = []
        star = []
        for i in range(len(s)):
            if c=='(':
                left.append(i)
            elif c=='*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        while(left and star):
            if left.pop()>star.pop():
                return False
        return not left
        
