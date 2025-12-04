from stats import get_num_words,get_count,sort_dict
import sys

if(len(sys.argv)!=2):
 print("Usage: python3 main.py <path_to_book>")
 sys.exit(1)

def get_book_text(path_to_file):
     file_contents=""
     with open(path_to_file) as f:
      file_contents = f.read()
    
     return file_contents
def main():
   print("============ BOOKBOT ============")
   print("Analyzing book found at books/frankenstein.txt...")
   print("----------- Word Count ----------")
   text = get_book_text(sys.argv[1])
   num_words = get_num_words(text)
   print(f"Found {num_words} total words")
   print("--------- Character Count -------")
   count_dict = get_count(text)
   sorted_dict = sort_dict(count_dict)
   for dic in sorted_dict:
       if dic["char"].isalpha():
        char = dic["char"]
        num = str(dic["num"])
        print(char+": "+num)

main()


