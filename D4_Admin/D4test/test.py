from p_library.models import Author, Book

gogol = Author.objects.get(full_name='Николай Васильевич Гоголь')
gogol_books = Book.objects.filter(author=gogol)
gogol_books.count()

pushkin = Author.objects.get(full_name='Пушкин Александр Сергеевич')
pushkin_books = Book.objects.filter(author=pushkin)
pushkin_books.count()

turgenev = Author.objects.get(full_name='Тургенев Иван Сергеевич')
turgenev_books = Book.objects.filter(author=turgenev)
turgenev_books.count()

adams = Author.objects.get(full_name='Douglas Adams')
adams_books = Book.objects.filter(author=adams)
adams_books.count()

salinger = Author.objects.get(full_name='Jerome David Salinger')
salinger_books = Book.objects.filter(author=salinger)
salinger_books.count()

hamsun = Author.objects.get(full_name='Knut Hamsun')
hamsun_books = Book.objects.filter(author=hamsun)
hamsun_books.count()
