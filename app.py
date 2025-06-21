def create_message(name):
    return f"Hello, {name} Student."

def main():
    user = "DevOps Student"
    message = create_message(user)
    print(message)

if __name__ == "__main__":
    main()
