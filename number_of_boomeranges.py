class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                d = f*f + s*s
                cmap[d] = 1 + cmap.get(d, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] -1)
        return res