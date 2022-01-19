# 데이터 : 어느 커피 전문점에서 나흘 동안 기록한 메뉴별 커피 판매량
# 원하는 작업: 나흘 동안 메뉴당 전체 판매량과 하루 평균 판매량 구하기

espresso = []
americano = []
latte = []
cappucino = []

with open('coffeeShopSales.txt', 'r', encoding='UTF-8') as f:
    header = f.readline()
    for i in f:
        data_list = i.split()
        espresso.append(int(data_list[1]))
        americano.append(int(data_list[2]))
        latte.append(int(data_list[3]))
        cappucino.append(int(data_list[4]))

header_list = header.split()
#print(header_list)

total_sum = [sum(espresso), sum(americano), sum(latte), sum(cappucino)]

for k in range(len(total_sum)):
    print(f'{header_list[k+1]} 판매량\n- 나흘 전체 : {total_sum[k]}, 하루평균 {total_sum[k]/len(total_sum)}')