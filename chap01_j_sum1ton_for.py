# 1부터 n까지 정수의 합 구하기 2 for

print('1부터 n까지 합을 구합니다')
n = int(input('n값을 입력하세요 : '))

sum = 0
for i in range(1,1+n):
    sum += i
    i+=1


print(f'1부터 {n}까지 정수의 합은 {sum}입니다\ni값은 {i}입니다')


# 가운스 덧셈으로 1부터 n까지의 정수의 합 구하기

n = int(input("정수를 입력하세요: "))

sum2 = n * (n + 1) // 2  # 가우스 공식 사용
print(f"1부터 {n}까지의 합은 {sum2}입니다.")
