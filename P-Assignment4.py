def modify_file_content(content):
    """Modify the content by converting to uppercase and adding line numbers"""
    lines = content.splitlines()
    modified_lines = [f"{i+1}: {line.upper()}" for i, line in enumerate(lines)]
    return "\n".join(modified_lines)

def process_file():
    try:
        # Get input filename from user
        input_filename = input("Enter the input filename: ")
        
        # Try to read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content
        modified_content = modify_file_content(content)
        
        # Create output filename
        output_filename = f"modified_{input_filename}"
        
        # Write to output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"File successfully processed! Modified content written to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Unable to read '{input_filename}'. It may not be a text file.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    process_file()