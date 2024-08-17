#this counts the words in a text document and returns the count
# Open the .txt file in read mode
with open('countwords.txt', 'r') as file:
    # Read the content of the file
    text = file.read()

# Split the text into words
words = text.split()

# Initialize an empty dictionary to store the word counts
word_count = {}

# Iterate over each word in the list of words
for word in words:
    # Convert the word to lowercase to make the count case-insensitive
    word = word.lower()

    # If the word is not in the dictionary, add it with a count of 0
    if word not in word_count:
        word_count[word] = 0

    # Increment the count of the word by 1
    word_count[word] += 1

# Print the resulting dictionary of word counts
print(word_count)
