def add_course():
    while True:
        course_name = input("請輸入課程名稱")
        course_number = input("請輸入課程代碼四碼")
        if len(course_number) != 4:
            print("錯誤的代碼，請重試\n")
            continue
        course_professor = input("請輸入授課教授")        
        course_time = input("請輸入上課時間(第一碼為星期，第二碼起為節次)")
        courses.append({"course_name":course_name,
                        "course_number":course_number,
                        "course_professor":course_professor,
                        "course_time":course_time,
                        "enrolled_students":[]})
        print("添加成功\n")
        print("目前課程:")
        for i in range(len(courses)):
            print(f"{i+1}.{courses[i]['course_name']}")
        choice1 = input("是否繼續輸入(是/否)")
        print()
        if choice1 == "否":
            break       
def add_or_withdraw():
    while True:
        check1 = 0
        name = input("請輸入學生姓名或學號")
        for i in range(len(students)):
            if name == students[i]["student_name"] or name == students[i]["student_number"]:
                check1 = students[i]["student_name"]
                student = i
        if check1 == 0:
            print("查無此人，請再試一次\n")
            break
        choice1 = input(f"{check1}同學，請問要1.加選2.退選")
        if choice1 =="1":
            check2 = 0
            check3 = 0
            name = input("請輸入課程名稱或代碼")
            for i in range(len(courses)):
                if name == courses[i]["course_name"] or name == courses[i]["course_number"]:
                    check2 = courses[i]["course_name"]
                    check3 = i
            if check2 == 0:
                print("不存在的課程，請再試一次\n")
                break
            students[student]["student_course"].append(check2)
            courses[check3]["enrolled_students"].append(check1)
            print("加選成功\n")
            print(f"{students[i]['student_name']}同學目前課表")
            for i in range (len(students[student]["student_course"])):
                print(students[student]["student_course"][i])
            choice2 = input("是否繼續輸入(是/否)")
            print()
            if choice2 == "否":
                break
        elif choice1 == "2":
            check2 = 0
            check3 = 0
            name = input("請輸入課程名稱或代碼")
            for i in range(len(courses)):
                if name == courses[i]["course_name"] or name == courses[i]["course_number"]:
                    check2 = courses[i]["course_name"]
                    check3 = i
            if check2 == 0:
                print("不存在的課程，請再試一次\n")
                break
            if check2 not in students[student]["student_course"]:
                print("你沒有選這門課\n")
                break
            students[student]["student_course"].remove(check2)
            courses[check3]["enrolled_students"].remove(check1)
            print("退選成功\n")
            print(f"{students[i]['student_name']}同學目前課表:")
            for i in range (len(students[student]["student_course"])):
                print(students[student]["student_course"][i])      
            choice2 = input("是否繼續輸入(是/否)")
            print()
            if choice2 == "否":
                break
def add_student():
    while True:    
        student_name = input("請輸入學生姓名")
        student_number = input("請輸入學生學號十碼")
        if len(student_number) != 10:
            print("錯誤的學號，請重試\n")
            continue
        students.append({"student_name":student_name,
                         "student_number":student_number,
                         "student_course":[]})
        print("添加成功\n")
        print("目前學生:")
        for i in range(len(students)):
            print(f"{i+1}.{students[i]['student_name']}")            
        choice1 = input("是否繼續輸入(是/否)")
        print()
        if choice1 == "否":
            break 
def view_course():
    for i in range(len(courses)):
        print(f"{i+1}.{courses[i]['course_name']} 課程代碼:{courses[i]['course_number']} 授課教授:{courses[i]['course_professor']} 上課時間:{courses[i]['course_time']}")
def view_enrolled_students():
    while True:
        view_course()   
        check1 = 0
        check2 = 0
        name = input("請輸入課程名稱或代碼")
        for i in range(len(courses)):
            if name == courses[i]["course_name"] or name == courses[i]["course_number"]:
                check1 = courses[i]["course_name"]
                check2 = i
        if check1 == 0:
            print("不存在的課程，請再試一次\n")
            break
        print(f"{courses[check2]['course_name']}")
        for i in range(len(courses[check2]['enrolled_students'])):
            print(f"{i+1}.{courses[check2]['enrolled_students'][i]}")
        choice1 = input("是否繼續輸入(是/否)")
        print()
        if choice1 == "否":
            break
def main():
    while True:
        print("1.選課系統")
        print("2.學生系統")
        print("3.退出")
        choice1 = input("請輸入動作(1/2/3)")
        if choice1 == "1":
            print("1.添加課程")
            print("2.查詢課程")
            print("3.查詢修課學生")
            choice2 = input("請輸入動作(1/2/3)")
            if choice2 == "1":
                add_course()
            elif choice2 == "2":
                view_course()
            elif choice2 == "3":
                view_enrolled_students()
        elif choice1 == "2":
            print("1.加入學生")
            print("2.加退選")
            choice2 = input("請輸入動作(1/2)")
            if choice2 == "1":
                add_student()
            elif choice2 == "2":
                add_or_withdraw()
        elif choice1 == "3":
            break
courses = []
students = []
if __name__ == "__main__":
    main()