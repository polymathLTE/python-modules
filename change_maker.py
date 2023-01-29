import math

def make_change(curncy_list=[], bill=0, cash=0):
    """ This function calculates the change to be 
    given to a customer for any type of currency based on cash
    
    Parameters:
        curncy_list (list): list containing the local currency
        bill (int): this is the purchase total amount
        cash (int): this is the cash as given by the customer

    return:
        dictionary containing the total change per currency denomination
    """
    #presets the values to be used for calc
    tol_cash = int(math.floor(float(cash)))
    tol_bill = int(math.floor(float(bill))) 
    if tol_bill >= tol_cash:
        return tol_cash - tol_bill
    tol_change =  tol_cash - tol_bill
    curncy_list.sort()
    curncy_list.reverse()
    change_list = {}

    #calculates the change with a loop
    try:
        for i in range(len(curncy_list)):
            if int(tol_change/curncy_list[i]) > 0:
                chk = divmod(tol_change, curncy_list[i])
                change_list[f'{curncy_list[i]} notes'] = chk[0]
                tol_change = chk[1]

        #returns a dictionary containing the change info
        return change_list
    except Exception as exc:
        return exc