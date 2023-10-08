def purchase(quantity,price_per_unit):
    return quantity*price_per_unit
def calculate_total_spent(purchases):
    return sum(purchases)
def apply_discounted(price,discount_percentage):
    return price*(1-discount_percentage/100)
class Book:
    def __init__(self,ibsn,title,author,price,stock):
        self.ibsn = ibsn
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    def display_info(self):
        return f"Title:{self.title}, Author:{self.author}, Price:${self.price}"
def view():
    print("書庫存量:")
    for i in range(len(books)):
        print(f"{i+1}.書名: {books[i].title} 作者: {books[i].author} 價格: {books[i].price} IBSN: {books[i].ibsn} 庫存數量: {books[i].stock}")
    print(f"購買總價的折扣: {discount_percentage}")
books = []
quantities = []
discount_percentage = 0
while True:
    print("1.店家(輸入書籍資料並加入庫存和輸入折扣)")
    print("2.顧客(購買書籍)")
    print("3.退出")
    choice1 = input("請選擇身分(1/2/3): ")
    if choice1 == "3":
        break
    print()
    if choice1 == "1":
        while True:            
            books.append(Book(input("請輸入書籍的IBSN: "),input("請輸入書籍的標題: "),input("請輸入書籍的作者: "),float(input("請輸入書籍的價格: ")),int(input("請輸入庫存數量: "))))
            quantities.append(0)
            print("加入成功")
            view()
            choice2 = input("是否繼續加入書籍?(是/否)")
            if choice2 == "是":
                continue
            else:
                discount_percentage = int(input("請輸入折扣百分比: "))
                view()
                break
    elif choice1 == "2":
        while True:
            print("1.輸入欲購買書籍之書名或IBSN編號")
            print("2.結帳")
            print("3.退出")
            choice3 = input("請輸入進行動作(1/2/3)")
            if choice3 == "1":
                while True:
                    view()
                    to_buy = input("請輸入欲購買書籍之書名或IBSN編號或退出:")                        
                    if to_buy == "退出":
                        print("感謝使用")
                        break
                    else:
                        check = -1
                        for i in range(len(books)):
                            if to_buy == books[i].title or to_buy == books[i].ibsn:
                                check = i
                        if check == -1:
                            print("查無此書，請再試一次")
                            continue
                        else:
                            quantity = int(input("請輸入欲購買數量"))
                            if quantity > books[check].stock:
                                print("庫存不足，請再試一次")
                            else:    
                                quantities[check] = quantity
            elif choice3 == "2":
                cost = []
                print("\n購買成功!")
                print("書籍資訊:")
                for i in range(len(books)):
                    if quantities[i] != 0:
                        books[i].stock -= quantities[i]
                        cost.append(purchase(books[i].price,quantities[i]))
                        print(f"{i+1}.書名: {books[i].title} 作者: {books[i].author} 價格: {books[i].price} IBSN: {books[i].ibsn} 購買數量: {quantities[i]}")
                total = calculate_total_spent(cost)
                print(f"消費總金額: ${total}")
                print(f"折扣後價格: ${apply_discounted(total,discount_percentage)}")
                view()
                break
            elif choice3 == "3":
                break