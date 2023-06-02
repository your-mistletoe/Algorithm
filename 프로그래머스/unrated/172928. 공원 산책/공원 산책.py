def solution(park, routes):
    # 딕셔너리 시작 좌표 (북, 남, 동, 서)
    dx = {'N': -1, 'S': 1, 'E': 0, 'W': 0}
    dy = {'N': 0, 'S': 0, 'E': 1, 'W': -1}

    # # 시작 좌표
    x, y = -1, -1
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j

    # routes 순회
    for i in routes:
        # 이동할 방향, 이동할 칸에 따른 좌표 이동
        op, n = i.split(' ')
        # 장애물 만남, 범위 이탈 여부
        back = False

        # 입력된 명령에 따른 이동 (입력된 방향으로 한 칸씩 이동)
        for d in range(1, int(n)+1):
            nx = x + dx[op] * d
            ny = y + dy[op] * d

            # 장애물 만남, 범위 이탈시
            if nx < 0 or ny < 0 or nx > len(park)-1 or ny > len(park[0])-1:
                back = True
                break
            if park[nx][ny] == 'X':
                back = True
                break

        if back:
            continue
        # 이동 중 장애물 만남과 범위 이탈 X 이었을 때 주어진 칸수만큼 이동
        x += dx[op] * int(n)
        y += dy[op] * int(n)
        print(x, y)

    return [x, y]