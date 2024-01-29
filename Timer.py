from time import sleep as s
def start_prog():
    user_name = input("Enter your name: ")
    print(f"Hello {user_name}! Welcome to timer.")
    wanna_continue = input("Would you like continue?(Enter Yes/No): ")

    if wanna_continue.lower() != "yes":
        print("Okay,bye!")
        exit()

    while wanna_continue.lower() == "yes":
        time = int(input("Enter time: "))
        while time > 0:
            s(1)
            time -= 1
            print("Time now:", time)
        else:
            print("Timeout.")
            wanna_continue = input("Would you like continue?(Enter Yes/No): ")
            if wanna_continue.lower() != "yes":
                print("Okay,bye!")
                exit()
            else:
                continue

start_prog()