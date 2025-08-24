class Stock:
    def initilizer(self, *args):
        if len(args) == 3:
            self.slno, self.name, self.price = args
        else:
            self.slno, self.name, self.price = 1, 'NO STOCK', 0.0

    def printStock(self):
        print(f'SlNo: {self.slno}  Name: {self.name}  Price: {self.price}')


if __name__ == '__main__':
    infosys = Stock()
    infosys.initilizer(1, 'Infosys', 1199.30)
    infosys.printStock()