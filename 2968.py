import math
values = list(map(int, input().split()))
ten = (values[0] * values[1] / 100) * 10
twenty = (values[0] * values[1] / 100) * 20
thirty = (values[0] * values[1] / 100) * 30
forty = (values[0] * values[1] / 100) * 40
fifty = (values[0] * values[1] / 100) * 50
sixty = (values[0] * values[1] / 100) * 60
seventy = (values[0] * values[1] / 100) * 70
eighty = (values[0] * values[1] / 100) * 80
ninety = (values[0] * values[1] / 100) * 90
print(round(ten), round(twenty), round(thirty), round(forty), round(fifty), round(sixty), round(seventy), round(eighty), round(ninety))