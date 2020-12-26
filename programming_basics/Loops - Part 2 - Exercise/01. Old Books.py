book = input()
biblio_size = int(input())
book_to_find = False
books = 0
while books < biblio_size:
    searching_book = input()
    books += 1
    if searching_book == book:
        book_to_find = True
        print(f"You checked {books - 1} books and found it.")
        break

if not book_to_find:
    print("The book you search is not here!")
    print(f"You checked {books} books.")

