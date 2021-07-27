import bisect

def grade(score, breakpoints=[30, 50, 70, 90], grades='12345'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 45, 23, 66, 82, 99]])