def caculate_circle(radius):
    area = 3.14159*radius**2
    perimeter = 3.14159*radius*2
    return area,perimeter
def caculate_rectangle(length,width):
    area = length*width
    perimeter = (length+width)*2
    return area,perimeter
def check_triangle(side1,side2,side3):   
    if side1+side2 > side3 and side2+side3 > side1 and side1+side3 > side2:
        return True
    else:
        return False
def caculate_triangle(side1,side2,side3):
    s = (side1+side2+side3)/2
    area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
    perimeter = side1+side2+side3
    return area,perimeter
def main():
    while True:
        print("請選擇一個幾何形狀")
        print("1.圓形")
        print("2.矩形")
        print("3.三角形")
        print("4.退出程式\n")
        choice = input("請輸入選項(1/2/3/4):")
        print()
        if choice == "1":
            radius = float(input("請輸入圓的半徑:"))
            if radius > 0:
                area,perimeter = caculate_circle(radius)
                print(f"圓的面積是:{area}")
                print(f"圓的周長是:{perimeter}\n")
            else:
                print("半徑不能是負數或零，請再試一次。\n")
        elif choice == "2":
            length = float(input("請輸入矩形的長:"))
            width = float(input("請輸入矩形的寬:"))
            if length and width > 0 :
                area,perimeter = caculate_rectangle(length,width)
                print(f"矩形的面積是:{area}")
                print(f"矩形的周長是:{perimeter}\n")
            else:
                print("長寬不能是負數或零，請再試一次。\n")
        elif choice == "3":
            side1 = float(input("請輸入三角形的第一邊長:"))
            side2 = float(input("請輸入三角形的第二邊長:"))
            side3 = float(input("請輸入三角形的第三邊長:"))
            if side1 > 0 and side2 > 0 and side3 > 0:
                if check_triangle(side1,side2,side3) == True:
                    area,perimeter = caculate_triangle(side1,side2,side3)    
                    print(f"三角形的面積是:{area}")
                    print(f"三角形的周長是:{perimeter}\n")
                else:
                    print("此三角形不成立，請再試一次。\n")
            else:
                print("邊長不能是負數或零，請再試一次。\n")
        else:
            print("感謝使用，再見!")
            break
if __name__ == "__main__":
    main()