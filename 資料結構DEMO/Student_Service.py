from student import Student
from data_structures import Stack, Queue, BinaryTree
import os

DATA_FILE = "students.txt"  # 模擬資料庫的檔案名稱

class StudentService:
    def __init__(self):
        self.students = {}  # 使用字典存儲學生資料
        self.history = Stack()  # 堆疊用於記錄歷史操作
        self.batch_queue = Queue()  # 佇列用於批次操作
        self.tree = BinaryTree()  # 二元樹用於成績排序

    def load_data(self):
        #從檔案中載入學生資料
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r") as file:
            for line in file:
                name, grade = line.strip().split(",")
                grade = int(grade)
                student = Student(name, grade)
                self.students[name] = student
                self.tree.insert(student)
        print("資料已載入。")

    def save_data(self):
        #將學生資料保存到檔案
        with open(DATA_FILE, "w") as file:
            for student in self.students.values():
                file.write(f"{student.name},{student.grade}\n")
        print("資料已保存。")

    def add_student(self, name, grade):
        #新增學生資料
        if name in self.students:
            print("學生已存在！")
            return
        student = Student(name, grade)
        self.students[name] = student
        self.tree.insert(student)
        self.history.push(("add", name))
        print(f"已新增學生：{student}")

    def update_student(self, name, grade):
        #更新學生成績
        if name not in self.students:
            print("學生不存在！")
            return
        old_grade = self.students[name].grade
        self.students[name].grade = grade
        self.history.push(("update", name, old_grade))
        print(f"已更新學生 {name} 的成績為 {grade}")

    def delete_student(self, name):
        #刪除學生資料
        if name not in self.students:
            print("學生不存在！")
            return
        student = self.students.pop(name)
        self.tree.delete(student.grade)
        self.history.push(("delete", student))
        print(f"已刪除學生：{student}")

    def get_student(self, name):
        #查詢特定學生成績
        if name in self.students:
            print(self.students[name])
        else:
            print("學生不存在！")

    def display_students(self):
        #顯示所有學生的成績，按成績排序
        print("所有學生（按成績排序）:")
        sorted_students = sorted(self.tree.in_order_traversal(), key=lambda s: s.grade, reverse=True)
        for student in sorted_students:
            print(student)

    def undo(self):
        #復原最近的操作
        if self.history.is_empty():
            print("無操作可復原！")
            return
        action = self.history.pop()
        if action[0] == "add":
            self.students.pop(action[1])
            print(f"已復原新增操作：刪除學生 {action[1]}")
        elif action[0] == "update":
            self.students[action[1]].grade = action[2]
            print(f"已復原更新操作：恢復學生 {action[1]} 的成績為 {action[2]}")
        elif action[0] == "delete":
            student = action[1]
            self.students[student.name] = student
            self.tree.insert(student)
            print(f"已復原刪除操作：恢復學生 {student}")

    def batch_add(self, batch_data):
        #批次新增學生資料
        pairs = batch_data.split(";")
        for pair in pairs:
            try:
                name, grade = pair.split(",")
                grade = int(grade)
                if 0 <= grade <= 100:
                    self.batch_queue.enqueue(Student(name.strip(), grade))
                else:
                    print(f"成績 {grade} 超出範圍，略過 {name.strip()}！")
            except ValueError:
                print(f"格式錯誤，略過資料：{pair}")
        while not self.batch_queue.is_empty():
            student = self.batch_queue.dequeue()
            self.add_student(student.name, student.grade)