
def is_id_correct(id_no, buys, boxs):
    left = boxs
    ret_item = [False,[]]
    for i in range(id_no,n_houses):
        left = left - buys[i]
        if left < 0:
            pass
            #print(id_no+1,i+1," Not Okay ",left)
        if left == 0:
            #print(id_no+1,i+1," OKAY ",left)
            if ret_item[0] is True: ret_item[1].append([id_no+1,i+1])
            else: ret_item = [True,[[id_no+1,i+1]]]
    return ret_item
def search_all_possibilities(n_houses,n_boxes,n_buys):
    is_found=False
    method=0
    for i in range(n_houses):
        deal = is_id_correct(i, buys=n_buys, boxs=n_boxes)
        if deal[0] is True:
            is_found=True
            method+=1
            print("Possibility : ",method)
            if len(deal[1])==1:
                #print(deal)
                print(f"Start your route at house {deal[1][0][0]} and go to house {deal[1][0][1]} to delivery {n_boxes} boxes of girl scout cookies.")
            else:
                for s,e in deal[1]:
                    print(f"Start your route at house {s} and go to house {e} to delivery {n_boxes} boxes of girl scout cookies.\n")
            #break
    if is_found is False:
        print("It is impossible to derivel any cookies without making a partial order.")

if __name__=='__main__':
    """
    Data Should be loaded into file named datafile.txt as coded.
    """
    # with open('datafile.txt','r') as file:
    #     data = file.read().split('\n')
    #     if data[-1]=='': data=data[:-1]
    # data = [int(i) for i in data]

    # n_houses = data[0]
    # n_boxes = data[1]
    # n_buys = data[2:]
    # if len(n_buys) is not n_houses:
    #     print("Data has errors, Please check")
    #     exit()

    ## Testing
    n_houses = 9
    n_boxes = 12
    n_buys = [4,4,4,3,3,3,5,4,4]
    search_all_possibilities(n_houses,n_boxes,n_buys)
