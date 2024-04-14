def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def operations(data):
    if data:
        try:
            data = [int(d) for d in data]
            total_sum = sum(num for num in data)
            average = total_sum / len(data)
            max_value = max(data)
            min_value = min(data)
            print(f"Total sum: {total_sum}")
            print(f"Average: {average}")
            print(f"Maximum value: {max_value}")
            print(f"Minimum value: {min_value}")
        except ValueError:
            print("Error: Invalid data in the file.")
    else:
        print("No data to perform operations.")


def main():

    file_path = input("Enter the path to the text file: ")
    try:
        data = read_file(file_path)
        if data:
            operations(data)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
