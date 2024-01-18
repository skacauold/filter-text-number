# membaca data dari filtering.txt
with open('filtering.txt', 'r') as file:
    data = file.read()

# filter text dan numbers
filtered_text = ' '.join(filter(str.isalpha, data.split()))
filtered_numbers = ' '.join(filter(str.isdigit, data.split()))

# menyimpan filtered text ke file text.txt
with open('text.txt', 'w') as text_file:
    text_file.write(filtered_text)

# menyimpan filtered numbers ke file numbers.txt
with open('numbers.txt', 'w') as numbers_file:
    numbers_file.write(filtered_numbers)
