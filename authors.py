class Authors:
    def __init__(self,name = str,surname = str,birth_date = str,death_date = str,
                 fake_name = str,country = str,works = list, add_work = str):
        """

        :param name: Name of the author
        :param surname: Surname of the author
        :param birth_date: When the author was born
        :param death_date: When did the author die(if he did)
        :param fake_name: Fictitious name
        :param country: Where are(was) from author
        :param works: His books and other creations
        :param add_work: Work which will be written by the author(if he is alive)
        """
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.death_date = death_date
        self.fake_name = fake_name
        self.country = country
        self.works = works
        self.add_work = add_work
    def add_book(self):
        """

        :return: New book
        """
        pass

    def add_author(self):
        """

        :return: New author
        """
        pass


class Works:
    def __init__(self,authors = list,publisher = list,year = str):
        """

        :param authors: Author of the work
        :param publisher: A man who is publishing authors work
        :param year: When did the work publish
        """
        self.authors = authors
        self.publisher = publisher
        self.year = year



    def add_book(adding_book):
        self.adding_book = input()
        return works.append(self.adding_book)
    def add_author(adding_author):
        self.adding_author = input()
        return author.append(self.adding_author)


    class Book(Works):
        def __init__(self, book_binding = str, book_cover = str, year = int):
            super().__init__(year)
            self.book_binding = book_binding
            self.book_cover = book_cover

    class Magazine(Works):
        def __init__(self, type_of_cover = str, year = int):
            super().__init__(year)
            self.type_of_cover = type_of_cover

    class Publishing(Works):
        def __init__(self, place_of_publication, year: int):
            super().__init__(year)
            self.place = place_of_publication


authors_list = []
adding_author = input()
authors_list.append(adding_author)
work_list = []
adding_work = input()
work_list.append(adding_work)

for a in authors_list:
    print(a.adding_author())

for b in work_list:
    print(b.adding_work())
