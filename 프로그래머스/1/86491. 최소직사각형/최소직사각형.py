def solution(sizes):
    answer = 0
    wid = 0
    hei = 0
    for recs in sizes : 
        # print(recs)
        rec_wid = recs[0]
        rec_hei = recs[1]
        # print(rec_hei)
        if rec_wid < rec_hei :  # 가로가 세로보다 작은 경우 -> 세로값을 가로값에 
            rec_wid, rec_hei = rec_hei, rec_wid

        if rec_wid > wid :
            wid = rec_wid

        if rec_hei > hei :
            hei = rec_hei

    answer =  wid * hei    
    
    return answer