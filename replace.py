def Replace(input_filename, output_filename):

    # Read the content of the input file
    with open(input_filename, 'r') as file:
        content = file.read()

    # Initialize a count for the word "terrible"
    terrible_count = 0
    modified_text = ""

    # Define a flag to keep track of whether "terrible" is followed by punctuation
    terrible_with_punctuation = False

    i = 0
    while i < len(content):
        if content[i:i+8].lower() == "terrible":
            terrible_count += 1
            if terrible_count % 2 == 0:
                modified_text += "pathetic"
            else:
                modified_text += "marvellous"
            i += 8
            # Check if "terrible" is followed by punctuation and keep it
            while i < len(content) and content[i] in '.,!?;':
                modified_text += content[i]
                i += 1
        else:
            modified_text += content[i]
            i += 1

    # Write the modified text to the result file
    with open(output_filename, 'w') as result_file:
        result_file.write(modified_text)

    # Display the total count of "terrible"
    print(f'Total occurrences of "terrible": {terrible_count}')

# Call the function to process the text
Replace('file_to_read.txt', 'result.txt')
