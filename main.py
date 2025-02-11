def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    #print(word_count(file_contents))
    #print(char_count(file_contents))
    word_counter = word_count(file_contents)
    sorting_list = sorted(char_count(file_contents).items(), key=lambda x:x[1], reverse=True)
    sorting_dict = dict(sorting_list)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_counter} words found in the document")
    print()
    for char in sorting_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {sorting_dict[char]} times")
    print("--- End report ---")
   
def word_count(content):
    words_counter = content.split()
    return len(words_counter)

def char_count(file_contents):
    lowered_file = file_contents.lower()
    counter_dict = {}
    for char in lowered_file:
        if char.isprintable():
            if char not in counter_dict:
                counter_dict[char] = 1
            else:
                counter_dict[char] += 1
    return counter_dict

main()