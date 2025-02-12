print("Welcome to-do list program ")
questions = ["Do you want to add a new item ? ", "Do you want to list our To-Do items? "]
user_answer = ""
while(user_answer != "exit"):
    try:
        for q in questions:
            user_answer = input(q)
            if user_answer == "y" and q == questions[0]:
                with open(r"C:\Users\Mohamed\tuwaiq\LABS\SECOND-WEEK\LAB_FILES_IO\to_do.txt","a+",encoding="utf-8") as file:
                    file.write(input("Enter a new item: ") + "\n")
            elif user_answer == 'y' and q == questions[1]:
                with open(r"C:\Users\Mohamed\tuwaiq\LABS\SECOND-WEEK\LAB_FILES_IO\to_do.txt","r+",encoding="utf-8") as file:
                    file.seek(0)
                    print(file.read())
            elif user_answer == 'n':continue
            elif user_answer == "exit":break
            else: 
                raise ValueError("Only Enter (y,n,exit)")                 
    except Exception as e:
        print(e.__class__ , e)
else:
    print("thank you for using the To-Do program, come back again soon")
