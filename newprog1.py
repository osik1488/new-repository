per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("введите сумму :"))
deposit=[]
for key in per_cent:
    deposit.append(per_cent[key]*money / 100)
print(deposit)
i = max(deposit)
print("максимальная сумма " + str(i))








