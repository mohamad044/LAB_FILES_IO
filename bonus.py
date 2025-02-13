import json,time

def add_item(file_path,new_item):
    with open(file_path,"r") as file:
        to_do =json.load(file)
    to_do.update({new_item['title'] : {'date':new_item['date'] ,'done':False}})
    with open(file_path,"w") as file:
        json.dump(to_do,file,indent=4)

def print_items(file_path):
    with open(file_path,"r") as file:
        to_do =json.load(file)
        for index, (title, details) in enumerate(to_do.items(), start=1):
            status = "Done" if to_do[title]["done"] else "Not Done"
            print(f"{index}. {title} - {details['date']} - {status}")
            
def search_item(file_path, search_title):
    with open(file_path, "r") as file:
        to_do = json.load(file)
        if search_title in to_do:
            item = to_do[search_title] 
            status = "Done" if item["done"] else "Not Done"
            print(f"{search_title.capitalize()} - {item['date']} - {status}")
        else:
            print("Title not found.")

def change_status(file_path,title):
    with open(file_path, "r") as file:
        to_do = json.load(file)
        if title in to_do:
            to_do[title]["done"] = not to_do[title]["done"]
            with open(file_path, "w") as file:
                json.dump(to_do, file, indent=4)
            status = "Done" if to_do[title]["done"] else "Not Done"
            print(f"Updated: {title.capitalize()} - {to_do[title]['date']} - {status}")
        else:
            print("Title not found.")
        

    
def main():
    print("Welcome to-do list program ")
    questions = ["Do you want to add a new item ? ", "Do you want to list our To-Do items? "]
    file_path = r"C:\Users\Mohamed\tuwaiq\LABS\SECOND-WEEK\LAB_FILES_IO\to_do.json"
    
    user_answer = ""
    while(user_answer != "exit"):
        try:
            for q in questions:
                user_answer = input(q)
                if user_answer == "y" and q == questions[0]:
                    title = input("Enter the title: ")
                    date = input("enter the date: ")
                    add_item(file_path,{"title":title,"date":date,"done":False})                        
                elif user_answer == 'y' and q == questions[1]:
                    print_items(file_path)
                    user_answer = input("Enter 1 for search\nEnter 2 for change status: ")
                    if user_answer == "1":
                        search_item(file_path,input("Enter title for search: "))
                    elif user_answer == "2":
                        change_status(file_path,input("Enter the title: "))
                        print(f"STATUS CHANGE DONE. ")
                elif user_answer == 'n':continue
                elif user_answer == "exit":break
                else: 
                    raise ValueError("Only Enter (y,n,exit)")                 
        except Exception as e:
            print(e.__class__ , e)
main()