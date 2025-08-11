import os
val1 = input("是否开启电脑管家检测电脑里的病毒和垃圾文件?(Y/N)")
if val1 == "Y":
    content = os.listdir(os.getcwd())
    print(f"{content}无任何病毒或垃圾文件！")