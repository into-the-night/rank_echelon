
def get_input():                          
    mylist = []
    order = input('Enter the order of the matrix (like 3x4): ').split('x')
    i = 0
    #print(order)
    print('Enter each element of the matrix seperated by a space, press enter for new row.')
    while i < int(order[0]):
        nums = input().split()
        nums = [int(x) for x in nums]
        mylist.append(nums)
        i += 1
    return mylist

# Can only find rank of matrices which can be found using just Echelon form

def echelon(m = list()):
    i = 0
    while i < len(m):
        row_n = m[i][i]
        #print(f'**{row_n}')
       
        if row_n == 0:
            k = i+1
            while k < len(m):
                if m[k][i] != 0:
                    print(f'Row({i}) <--> R({k})')
                    t1 = m[k].copy()
                    m[k] = m[i].copy()
                    m[i] = t1.copy()
                    row_n = m[i][i]
                    break
                k+=1
        if row_n != 1:
            t2 = []
            try:
                for _ in m[i]:
                    #print(f'**{row_n}')
                    t2.append(round(_/row_n, 5))
            except ZeroDivisionError:
                break
            m[i] = t2.copy()
            print(f'Row({i+1}) --> Row({i+1})/{row_n}')
            row_n = m[i][i]

        j = i+1
        while j < len(m):
            col_n = m[j][i]
            mul_fac = col_n/row_n
            #print(mul_fac)
            if mul_fac != 0:
                print(f'Row({j+1}) --> Row({j+1}) - {mul_fac}*Row({i+1})')
            else:
                print(f'Row({j+1}) --> Row({j+1}) - Row({i+1})')
            t3 = []
            _ = 0
            while _ < len(m[0]):
                t3.append(round(m[j][_] - m[i][_]*mul_fac, 4))
                _+=1
            m[j] = t3.copy()
            #print(m)
            j+=1
        i+=1
    return m

def check_rank(m):
    count = 0
    for i in m:
        if i == [0]*len(m[0]):
            count += 1
    return len(m) - count

print(check_rank(echelon(get_input())))
                
                


            
