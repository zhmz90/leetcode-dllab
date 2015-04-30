#! /usr/bin/env python

class Solution:

    def convert(self,s,numRows):
        
        if len(s) <= numRows or numRows ==1:
            return s
        bkgd = []
        
        # intilize a big matrix [[],[],...] with numRows rows and len(s) cols 
        # bkgd[1][2] 
        for row in xrange(numRows):
            cell = []
            for col in xrange(len(s)):
                cell.append([])
            bkgd.append(cell)

        vertical = True
        real_col = 0
        for ncol in xrange(len(s)):
            if len(s) == 0:
                break
            if vertical:
                vertical = False
                for nrow in xrange(numRows):
                    if len(s) == 0:
                        break
                    bkgd[nrow][real_col].append(s[0])
                    s = s[1:]

            else:
                vertical = True
                for nrow in xrange(numRows):
                    if len(s) == 0:
                        break
                    real_col += 1 
                    bkgd[numRows-1-nrow][real_col].append(s[0])
                    s = s[1:]

        ret = ""
        for nrow in xrange(numRows):
            for ncol in xrange(real_col):
                item = bkgd[nrow][ncol]
                if len(item) == 1:
                    ret = ret + item[0]
                elif len(item) == 0:
                    continue
                else:
                    print bkgd
                    print "error occures"
                    return
        return ret
        """
        bkgd = []
        even = True if numRows % 2 == 1 else False  
        for ncol in xrange(len(s)/numRows+1):
            atom = []
            if len(s) == 0: break
            
            for i in xrange(numRows):
                if len(s) == 0:
                    break
                if even:
                    atom.append(s[0])
                    s = s[1:]
                else:
                    if i % 2 == 0:
                        atom.append(" ")
                    else:
                        atom.append(s[0])
                        s = s[1:]
            bkgd.append(atom)
            even = not even
        if len(bkgd[-1]) != numRows:
            for i in xrange(numRows-len(bkgd[-1])):
                bkgd[-1].append(" ")
        
        print bkgd

        ret = ""
        for row in xrange(numRows):
            for col in xrange(len(bkgd)):
                item = bkgd[col][row]
                if item != " ":
                    ret = ret + item 
            
        return ret

        """

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    rows = 3
    so = Solution()
   # s = "ABC"
   # rows = 2
    print s
    ret = so.convert(s,rows)
    print ret

