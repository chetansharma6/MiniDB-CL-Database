#Drafting a simple command-line interface to better understanding databases

def user_input():
    print("Welcome to data container platform!")
    print("Select no to exit.")
    data = {}
    while True:
        for user in data:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            select = input("Would you like to continue? (yes/no): ")
            if select.lower() == 'no':
                print("Exiting the program.")
                return data
            else:
                continue

def main():
    data = user_input()
    print("Collected Data:", data)

if __name__ == "__main__":
    main()

