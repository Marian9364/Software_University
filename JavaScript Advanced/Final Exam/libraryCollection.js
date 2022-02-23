class LibraryCollection{
    constructor(capacity){
        this.capacity = Number(capacity);
        this.books = [];
    }

    addBook(bookName, bookAuthor){
        if (this.books.length >= this.capacity){
            console.log(this.books);

            throw new Error("Not enough space in the collection.")
        } else{
            this.books.push({bookName, bookAuthor, payed: false})
            console.log(this.books);

            return `The ${bookName}, with an author ${bookAuthor}, collect.`
        }
 
    }

    payBook(bookName){
        let bookFound = this.books.find(x=> x.bookName == bookName);
        if (!bookFound){
            throw new Error(`${bookName} is not in the collection.`);
        }
        if(bookFound.payed){
            throw new Error(`${bookName} has already been paid.`);
        } else{
            bookFound.payed = true;
            return `${bookName} has been successfully paid.`
        }
    }
    removeBook(bookName){
        let bookFound = this.books.find(x=> x.bookName == bookName);
        if (!bookFound){
            throw new Error("The book, you're looking for, is not found.");
        }
        if(!bookFound.payed){
            console.log(this.books)
            throw new Error(`${bookName} need to be paid before removing from the collection..`); 
        }
        let index = this.books.indexOf(bookFound);
        this.books.splice(index, 1);
        return `${bookName} remove from the collection.`

    }
    getStatistics(bookAuthor){
        let result = "";
        
        let foundAuthor = this.books.find(x=> x.bookAuthor == bookAuthor);
        if(bookAuthor){
            if(foundAuthor){

            result += `${foundAuthor.bookName} == ${foundAuthor.bookAuthor} - ${foundAuthor.payed? 'Has Paid' : 'Not Paid'}.`
            } else{
                throw new Error(`${bookAuthor} is not in the collection.`)
            }

        } else{
            result += `The book collection has ${this.capacity - this.books.length} empty spots left.` + "\n";
            let sortedBooks = this.books.sort((a,b)=> a.bookName - b.bookName);
            for (let el of sortedBooks){
                result += `${el.bookName} == ${el.bookAuthor} - ${el.payed? 'Has Paid' : 'Not Paid'}.` + "\n"

            }
        }
        return result.trimEnd();
    }

}
const library = new LibraryCollection(5)
library.addBook('Don Quixote', 'Miguel de Cervantes');
library.payBook('Don Quixote');
library.addBook('In Search of Lost Time', 'Marcel Proust');
library.addBook('Ulysses', 'James Joyce');
console.log(library.getStatistics());
