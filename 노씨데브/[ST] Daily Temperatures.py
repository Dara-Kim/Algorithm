'''
매일의 온도를 나타내는 int형 배열 temperatures가 주어진다.
answer 배열에의 원소 answer[i]는 i번째 날의 온도보다
더 따뜻해지기까지 며칠을 기다려야하는지 나타낸다.
만야 더 따뜻해지는 날이 있다면 answer[i] == 0 이다.
answer 배열을 반환하는 함수를 구현하시오.

제약조건
1. 1 <= temperatures.length <= 10^5
2. 30 <= temperatures[i] <= 100

'''

def day(temperatures):
    return None

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(day(temperatures))
# output = [1, 1, 4, 2, 1, 1, 0, 0]

temperatures = [30, 40, 50, 60]
print(day(temperatures))
# output = [1, 1, 1, 0]

temperatures = [30, 60, 90]
print(day(temperatures))
# output = [1, 1, 0]