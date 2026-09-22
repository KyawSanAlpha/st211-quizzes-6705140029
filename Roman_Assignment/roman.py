from source.roman import convert, to_roman

__all__ = ["convert", "to_roman"]


if __name__ == "__main__":
    while True:
        print("\n--- Roman Numeral Converter ---")
        print("1. Convert Roman Numeral")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "2":
            print("Thank you for using the Roman Numeral Converter! See you next time.")
            break

        if choice == "1":
            try:
                user_input = input("Enter a Roman Numeral: ")
                result = convert(user_input)
                print(f"{user_input.upper().strip()} = {result}")
            except (ValueError, TypeError) as error:
                print(f"Error: {error}")
        else:
            print("Invalid choice. Please select 1 or 2.")