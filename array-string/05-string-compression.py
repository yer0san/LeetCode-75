# difficulty: medium

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1 or len(chars) == 0:
            return 1
        s = ""
        l = chars[0]
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == l:
                count += 1
            else:
                s += l
                l = chars[i]
                if count > 1:
                    s += f"{count}"   
                count = 1
        s += l
        if count > 1:
            s += f"{count}"
        chars[:] = list(s)
        print(chars)
        return len(chars)
        
