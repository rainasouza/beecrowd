salary = float(input())
if 0 <= salary <= 400.00 :
    reajuste = 0.15
elif 400.01 <= salary <= 800.00:
    reajuste = 0.12
elif 800.01 <= salary <= 1200.00:
    reajuste = 0.10
elif 1200.01 <= salary <= 2000.00:
    reajuste = 0.07
else:
    reajuste = 0.04   

new_salary = salary + (salary*reajuste) 
reajuste_ganho = salary * reajuste
print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {reajuste_ganho:.2f}")
print(f"Em percentual: {int(reajuste * 100)} %")