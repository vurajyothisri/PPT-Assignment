def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False
    
    if s == goal:
       
        seen = set()
        for char in s:
            if char in seen:
                return True
            seen.add(char)
        return False
    
    differences = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            differences.append((s[i], goal[i]))
            if len(differences) > 2:
                return False
    
    return len(differences) == 2 and differences[0] == differences[1][::-1]







s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)  

