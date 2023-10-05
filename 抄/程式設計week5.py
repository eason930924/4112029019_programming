class Purchasable:
    def purchase(slef,quantity,price_per_unit):
        return quantity*price_per_unit
class Spendable:
    def calculate_total_spent(slef,purchases):
        return sum(purchases)
class Discountable:
    def apply_discounted(self,price,discount_percentage):
        return price*(1-discount_percentage/100)
class Book(Purchasable,Spendable,Discountable):
    def __init__(self,isbn,title,author,price,stock):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    def display_info(self):
        return f"Title:{self.title}, Author:{self.author}, Price:${self.price}"
book = Book(input("請輸入書籍的ISBN: "),input("請輸入書籍的標題: "),input("請輸入書籍的作者: "),float(input("請輸入書籍的價格: ")),int(input("請輸入庫存數量: ")))
purchase_quantity = int(input("請輸入購買的數量: "))
discount_percentage = int(input("請輸入折扣百分比: "))
purchases = [book.price*purchase_quantity]
book.stock -= purchase_quantity
print("\n購買成功!")
print("書籍資訊:")
print(f"書名: {book.title}, 作者: {book.author}, 價格: ${book.price}")
print(f"購買數量: {purchase_quantity}")
print(f"總消費金額: ${book.calculate_total_spent(purchases)}")
print(f"折扣後價格: ${book.apply_discounted(book.price,discount_percentage)}")
print(f"更新後庫存數量: {book.stock}")