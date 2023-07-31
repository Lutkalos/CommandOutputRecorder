import subprocess


def export_command_output(command, output_file):
    with open(output_file + ".txt", "w", encoding="utf-8") as f:
        try:
            output = subprocess.run(command, shell=True, stdout=f)
        except subprocess.CalledProcessError as e:
            f.write(e.output)
            f.write("\n")
            f.write("Error: " + e.output)
        else:
            f.write("\n")
            f.write("Command not found: " + command)


def get_output_file_name():
    output_file_name = input("Enter the name of the output file: ")
    return output_file_name


if __name__ == "__main__":
    command = input("Write your command: ")
    output_file_name = get_output_file_name()
    export_command_output(command, output_file_name)
