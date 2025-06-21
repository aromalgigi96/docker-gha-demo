def create_message(name):
    return f"Hello, {name}."

def main():
    user = "DevOps Student Nice to see you"
    message = create_message(user)
    print(message)

if __name__ == "__main__":
    main()
