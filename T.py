import os

def Google():
    Search = input(" Search = ")
    os.system(f"lynx https://google.com/search?q={Search}")

def Ecosia():
    Search = input(" Search =")
    os.system(f"lynx https://google.com/search?q={Search}")

def DuckDuckgo():
    Search = input(" Search =")
    os.system(f"lynx https://duckduckgo.com/?q={Search}")

while True:
    
    os.systen("pkg install lynx")
    os.system("clear")
    print(" By KiNGEX | https://GitHub.com/KiNGEX1")
    print("__________________________________________")
    
    print("Options:")
    print("1. Google")
    print("2. Ecosia")
    print("3. DuckDuckGo")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        Google() 
    elif choice == '2':
        Ecosia()
    elif choice == '3':
        DuckDuckgo()
    
