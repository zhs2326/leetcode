'''
A typical problem with backtrack.
One thing you need to pay attention is that string like '00' in s can't be abbreviated to '0' in the ouput, but when you
compare string with '0' and '255', you might tend to convert them to int. So remember that you should append the string
to your result.
Another thing is that '0' can be part of a valid IP address while '01' can't. You should pay attention to this.
'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def helper(words, temp, res):
            if not words and temp.count('.') == 4:
                res.append(temp[:-1])
                return
            elif temp.count('.') > 4:
                return
            for i in range(min(len(words), 3)):
                new_temp = temp
                if 0 <= int(words[:i+1]) <= 255:
                    if words[: i+1] != '0' and words[: i+1][0] == '0':
                        continue
                    new_temp += words[:i+1]+'.'
                    helper(words[i+1:], new_temp, res)
        
        helper(s, '', res)
        
        return res
