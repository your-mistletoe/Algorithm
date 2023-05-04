arr = [' '] * 20

# 학점의 총합
score_sum = 0
# 전공과목별의 합 (학점 * 과목평점)
majors_sum = 0

for i in range(20):
  # 과목평점
  score = 0.0
  arr[i] = list(input().split(' '))

  if arr[i][2][0] == 'A':
    score = 4.0
    if arr[i][2][1] == '+':
      score += 0.5
  elif arr[i][2][0] == 'B':
    score = 3.0
    if arr[i][2][1] == '+':
      score += 0.5
  elif arr[i][2][0] == 'C':
    score = 2.0
    if arr[i][2][1] == '+':
      score += 0.5
  elif arr[i][2][0] == 'D':
    score = 1.0
    if arr[i][2][1] == '+':
      score += 0.5
  elif arr[i][2][0] == 'P':
    continue
  # print(score, end=' ')

  score_sum += float(arr[i][1])
  majors_sum += score * float(arr[i][1])


print('%.6f' % (majors_sum / score_sum))