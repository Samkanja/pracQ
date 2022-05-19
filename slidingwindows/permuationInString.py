from typing import Counter


def checkInclusion(s1,s2):
    if len(s1) > len(s2):return False
    s1Dict = s2Dict = {}
    for i in range(len(s1)):
        s1Dict[s1[i]] = 1 + s1Dict.get(s1[i],0)
        s2Dict[s2[i]] = 1 + s2Dict.get(s2[i],0)
    if s2Dict == s1Dict:
        return True
    l = 0
    for r in range(len(s1),len(s2)):
        s2Dict[s2[r]] = 1 + s2Dict.get(s2[r],0)
        if s2Dict[s2[l]] == 1:
            del s2Dict[s2[l]]
        else:
            s2Dict[s2[l]] -= 1
        if s2Dict == s1Dict:
            return True
    return False



s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2))