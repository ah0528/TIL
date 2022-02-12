# 삽입정렬

def find_ins_idx(r,v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

