def solution(board):

    n = len(board)

    # 위험구역 -> 처음에는 모두 0 이라고 설정
    danger_zone = []
    for i in range(n) :     # 행
        one_row = []           
        for j in range(n) : # 열
            one_row.append(0)  
        danger_zone.append(one_row)

    # (0,0) 기준으로 둘러싸인 곳 설정
    around = [
        (-1, -1), (-1,0), (-1,1),
        (0, -1), (0,0), (0,1),
        (1, -1), (1, 0) , (1,1)
    ]

    # 칸 한칸씩 보기
    for bomb_x in range(n) :     # 행 전체
        for bomb_y in range(n) : # 열 전체
            # 지뢰 -> 1
            if board[bomb_x][bomb_y] == 1:

                # 위험 지역으로 x, y 방향으로 얼마나 움직일지
                for move in around : 
                    danger_x = move[0]
                    danger_y = move[1]

                    new_x = bomb_x + danger_x
                    new_y = bomb_y + danger_y
                    
                    # 보드 범위
                    if 0 <= new_x < n and 0 <= new_y < n :
                        danger_zone[new_x][new_y] = 1
    # 안전한 칸
    safe_cnt = 0
    for x in range(n) :
        for y in range(n) :
            if danger_zone[x][y] == 0 :
                safe_cnt += 1

    return safe_cnt