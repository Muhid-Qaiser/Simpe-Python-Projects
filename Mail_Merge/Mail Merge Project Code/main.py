PLACEHOLDER = '[name]'


with open('./Input/Names/invited_names.txt', mode='r') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt', mode='r') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)
