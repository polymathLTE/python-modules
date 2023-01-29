calc_change = __import__('change_maker').make_change

curncy = [[1000,500,200,50,100,20,10,5], [1,5,20,10,50,100], [1,2,100,5,10,50,20]]
purch_bill = [50, 70, 560]
t_cash = [10, 100, 0]

for i in range(3):
    print(calc_change(curncy[i], purch_bill[i], t_cash[i])),