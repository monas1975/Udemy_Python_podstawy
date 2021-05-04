if __name__ == '__main__':
 IsWeekend = True
 print("is weekend", IsWeekend)

 Temperature = 25
 print("Temperature =", Temperature)

 ToDoList='shopping'
 print("ToDoList", ToDoList)

 IsHappy = IsWeekend and Temperature>=20 and ToDoList==''
 print("IsHappy",IsHappy)

 IsHappy = not IsWeekend and Temperature<20 and ToDoList !=''
 print("IsHappy",IsHappy)

 print("...............")
 IsHappy = IsWeekend and Temperature >=20 and ToDoList == '' \
 or not IsWeekend and Temperature < 20 and ToDoList !=''
 print("IsHappy", IsHappy)

