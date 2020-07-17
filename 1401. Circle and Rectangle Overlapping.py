class Solution:
    def checkOverlap(self, r: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def inRect(x,y,x1,y1,x2,y2):
            return x>=x1 and x<=x2 and y>=y1 and y<=y2
        if inRect(x_center,y_center, x1,y1,x2,y2):
            return True
        
        for x in [x1,x2]:
            if abs(x-x_center)<=r and y1<=y_center<=y2:
                return True
        for y in [y1,y2]:
            if abs(y-y_center)<=r and x1<=x_center<=x2:
                return True
        return False
        # v = [(x1,y1),(x2,y2),(x1,y2),(x2,y1)]
        # for v in v1:
        #     if v[0]==-4391:
        #         import ipdb;ipdb.set_trace(context=20)
        #     if inRect(v[0],v[1], x1,y1,x2,y2):
        #         return True
        # for v in v2:
        #     if inCircle(v[0],v[1], x_center, y_center, r):
        #         return True
        # return False

    def checkOverlap(self, r: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def helper(val, _min, _max):
            return max(_min, min(val,_max))
        xc = helper(x_center, x1, x2)
        yc = helper(y_center, y1, y2)
        if (xc-x_center)**2 + (yc-y_center)**2 <= r**2:
            return True
        else:
            return False

if __name__ == "__main__":
    input = [1206,-5597,-276,-5203,-1795,-4648,1721]
    t = Solution().checkOverlap(*input)
    print(t)