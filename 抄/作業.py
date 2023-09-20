def buy():
    total_amount = 0
    while True:
        to_buy_book = input("請輸入欲購買書籍名稱(Book1/Book2/Book3/Book4/結帳)")
        if to_buy_book == "結帳":
            if total_amount > 500:
                total_amount *= 0.9
                print(f"恭喜!您獲得了10%的折扣，總金額為:{int(total_amount)}元")
            else:
                print(f"您的總金額為:{int(total_amount)}元")
            return True
        to_buy_quantity = input("請輸入欲購買數量")
        for item in order:
            if to_buy_book == item["name"]:
                item["quantity"] = int(to_buy_quantity)
        for item in order:
            for book in books:
                if item["name"] == book["name"]:
                    total_amount += book["price"]*item["quantity"]
                    book["quantity"] -= int(to_buy_quantity)
def add():
    item = input("請輸入欲添加之書籍(Book1/Book2/Book3/Book4)")
    quantity = input("請輸入欲添加之數量")
    for book in books:
        if item == book["name"]:
            book["quantity"] += int(quantity)
            print(f"書籍{item}已成功添加到書庫")
            print(f"書籍{item}的庫存已更新為:{book['quantity']}本")
def delete():
    item = input("請輸入欲移除之書籍(Book1/Book2/Book3/Book4)")
    quantity = input("請輸入欲移除之數量")
    for book in books:
        if item == book["name"]:
            book["quantity"] -= int(quantity)
            print(f"書籍{item}已成功從書庫移除")
            print(f"書籍{item}的庫存已更新為:{book['quantity']}本")
def inventory():
    print("當前庫存:")
    for item in books:
        print(f"書名:{item['name']} 價格:{item['price']} 庫存:{item['quantity']}")
def main():
    while True:
        action = input("請輸入欲執行之動作(購買/添加/移除/顯示庫存/退出)")
        if action == "購買":
            buy()
        elif action == "添加":
            add()
        elif action == "移除":
            delete()
        elif action == "顯示庫存":
            inventory()
        else:
            break           
books = [
    {"name":"Book1","quantity":5,"price":100},
    {"name":"Book2","quantity":5,"price":200},
    {"name":"Book3","quantity":5,"price":300},
    {"name":"Book4","quantity":5,"price":150}
]
order = [
    {"name":"Book1","quantity":0},
    {"name":"Book2","quantity":0},
    {"name":"Book3","quantity":0},
    {"name":"Book4","quantity":0}
]
if __name__ == "__main__":
    main()