def restore_ip_addresses(s):
    def is_valid(segment):
        return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)
    
    def backtrack(start=0, path=[]):
        # Base case: if we have 4 segments and we've used the entire string, add to result
        if len(path) == 4 and start == len(s):
            result.append('.'.join(path))
            return
        
        # Try all possible segment lengths (1 to 3) for the current position
        for end in range(start, min(start+3, len(s))):
            segment = s[start:end+1]
            if is_valid(segment):
                backtrack(end+1, path+[segment])
            else:
                break

    # Initialize the result list    
    result = []
    backtrack()
    return result