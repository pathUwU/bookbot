def main():
    #Main function block, pulls from other functions to do what we want our program to do
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    character_count_sorted = sort_character_count(character_count)
    #print(character_count_sorted)
    print(f"{num_words} words found in the document")
    #loop to iterate through returned sorted list of tuples in sort_character_count function and return the tuple values
    for char, count in character_count_sorted: #loop to directly unpack tuple and assign value pairs into char and count
        if char.isalpha(): #built-in python method to verify a character is an alphabetical character (removes special characters)
            print(f"The '{char}' character was found {count} times")
    print("---  End Report ---")

    #Function to get the number of words from our book_path file location
def get_num_words(text):
    words = text.split()
    return len(words)

    #Function to get the actual text from our book_path file location and put it into our program
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
    #Function to count the number of characters in "text" and assign/return it to dictionary "char_count"
def get_character_count(text):
    converted_to_lower = text.lower()
    char_count = {}
    for char in converted_to_lower:
        #print(f"currently processing character: {char}")
        if char in char_count:
            char_count[char] += 1
            #print(f"added {char} to character count")
        else:
            char_count[char] = 1
    return char_count

    #Function to convert character_count dictionary into a list (this is required to use the .sort() function since it can't be used 
    #on a dictionary)
def sort_character_count(character_count):
    items = list(character_count.items())
    items.sort(reverse=True, key=lambda item: item[1]) #sorts values from highest to lowest
    return items



main()