def main():
    # Container with options and messages
    options = {}

    print("Mathematical Sequence Solver")
    for key, value in options.items():
        print(f"{key}: {value['name']}")

    choice = input("Select an option: ")

    # Check if choice is valid
    if choice in options:
        n = int(input(options[choice]["message"]))
        try:
            result = options[choice]["func"](n)
            print(f"{options[choice]['name']} result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
