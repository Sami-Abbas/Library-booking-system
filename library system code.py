books = ['Lord Of The Rings','Harry Potter','Effective DevOps','DevOps Handbook']

complete="False"
while complete=="False":
  found=False
  book_taken=input("enter the name of the book you want ")
  for x in range(len(books)):
    if books[x]==book_taken:
      print("found")
      print("Book borrowed successfully")
      found=True
      y=x
  if found:
    books.pop(y)
    print("remaining books are: ",books)
    answer=input("do you want to borrow another book? ")
    if answer=="no" or answer=="No":
      complete="True"
  else:
    print("try again: ")