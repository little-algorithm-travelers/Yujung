import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]
# print(tomato)

que = deque([])
# print(que)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            que.append([i,j]) #que에 토마토 위치 좌표 저장.
            # print(que) 

def bfs():
    while que:
        x,y = que.popleft() #토마토 있는 좌표
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] #주변 토마토 탐색
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] +1 #주변 토마토가 며칠이 지나 익었는지 => 그 전 토마토 +1
                que.append([nx,ny]) #익은 주변 토마토 좌표를 저장.

bfs()

for i in tomato:
    for j in i:
        # print(j)
        if j == 0:
            print(-1)
            exit(0)
    result = max(result,max(i))
print(result-1)