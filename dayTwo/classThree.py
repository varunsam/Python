class Stock:
    def __init__(self, *args):
        #print(f'args: {args}')
        if len(args) == 3:
            self.slno, self.name, self.price = args
        else:
            self.slno, self.name, self.price = 1, 'NO STOCK', 0.0
    
    def __str__(self):
        return f'SlNo: {self.slno}  Name: {self.name}  Price: {self.price}'
    
if __name__ == '__main__':
    infosys = Stock(1, 'Infosys', 1199.30)
    bharat = Stock(3, 'Bharat Forge', 5022.13)
    tcs = Stock(2, 'TATA Consulting Servies',4355.90 )
    '''
    print(infosys)
    print(bharat)
    print(tcs)
    '''
    lst = [infosys, bharat, tcs]
    for i in lst:
        print(i)