def solution(keyinput, board):
    # 가로/세로 최대 범위
    garo_max = board[0] // 2
    sero_max = board[1] // 2

    x = 0
    y = 0
    
    for d in keyinput:
        if d == 'right':
            if x + 1 <= garo_max:   # 이동했을 때 가로 멕스보다 작으면 이동 가능
                x += 1
        elif d == 'left':
            if x - 1 >= -garo_max:
                x -= 1
        elif d == 'up':
            if y + 1 <= sero_max:
                y += 1
        elif d == 'down':
            if y - 1 >= -sero_max:
                y -= 1
                
    return [x, y]
