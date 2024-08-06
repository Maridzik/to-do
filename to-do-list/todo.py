import time
import os



directory = 'directory'


def slow_print(text : str, end_value : str):
    for char in text:
        print(char, end = end_value, flush=True)
        time.sleep(0.01)


def slow_input(prompt: str) -> str:
    slow_print(prompt, '')
    return input()


def get_file_names(folder_path):
    file_names = []
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_names.append(filename)
    for i in range(len(file_names)):
        print(file_names[i])



def create():
    b = slow_input("Введите название файла: ")
    content = ''
    lines = []
    while True:
        content = slow_input("content ")
        if content == "/cansel":
            break
        else:
            lines.append(content)
        if content == "/save":           
            with open(f"{directory}/{b}.txt", "w", encoding="utf-8") as f:
                for line in lines:
                    if line == "/save":
                        break
                    else:
                        f.write(line + "\n")
            break
        else:
            pass


def help():
    slow_print("/create - создать файл, \n/save - сохранить файл,\n/cansel - отменить сохранение файла,\n/read - прочитать файл,\n/file_names - названия всех сохранённых файлов,\n/exit - закрыть программу,\n/help - все команды\n", '')


def read(file):
    with open(f"{directory}/{file}.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            slow_print(line, '')


def main():
    while True:
        content = input()
        if content == "/create":
            create()

        elif content == "/read":
            read(slow_input("Введите название файла: "))
        
        elif content =="/exit":
            break
        
        elif content =="/help":
            help()

        elif content == "/save":
            pass

        elif content == "/file_names":
            get_file_names(directory)

        else:
            print("Неправильная команда")


if __name__ == "__main__":
    main()

        
    
