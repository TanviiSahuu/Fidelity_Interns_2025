#create function which read logfile with warning message


def warning(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if "WARNING" in line:
                    print(line.strip())

    except FileNotFoundError:
        print(f"File not found.")

    except Exception as e:
        print(f"An error occurred")

log_file = "data3[1].txt"  
warning(log_file)
