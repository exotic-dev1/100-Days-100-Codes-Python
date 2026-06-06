"""
Day98 :- Restore IP Addresses
Difficulty :- Medium
Concepts :- backtracking, strings
"""
def restore_ip_addresses(s):
    result = []

    def backtrack(start, path):
        
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return
        
        for length in range(1, 4):
            if start + length > len(s):
                break

            segment = s[start:start + length]
            
            if len(segment) > 1 and segment[0] == '0':
                continue
            
            if int(segment) <= 255:
                path.append(segment)
                backtrack(start + length, path)
                path.pop()

    backtrack(0, [])
    return result
    
s = "25525511135"
print(restore_ip_addresses(s))