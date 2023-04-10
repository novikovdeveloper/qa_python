from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book(self):
        new_book = BooksCollector()
        new_book.add_new_book('Гордость и предубеждение и зомби')
        assert len(new_book.get_books_rating()) == 1, "Книга не добавлена!"

    def test_cant_add_same_book_twice(self):
        twice_book = BooksCollector()
        twice_book.add_new_book('Гордость и предубеждение и зомби')
        twice_book.add_new_book('Гордость и предубеждение и зомби')
        twice_book.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(twice_book.get_books_rating()) == 2

    def test_cant_rate_book_not_on_list(self):
        not_in_lst = BooksCollector()
        not_in_lst.add_new_book('Гордость и предубеждение и зомби')
        not_in_lst.set_book_rating('Бойцовский клуб', 9)
        assert not_in_lst.books_rating == {'Гордость и предубеждение и зомби': 1}

    def test_cant_rate_less_one(self):
        books_rate = BooksCollector()
        books_rate.add_new_book('Гордость и предубеждение и зомби')
        books_rate.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert books_rate.get_books_rating != {'Гордость и предубеждение и зомби', 0}

    def test_cant_rate_more_ten(self):
        books_rate = BooksCollector()
        books_rate.add_new_book('Гордость и предубеждение и зомби')
        books_rate.set_book_rating('Гордость и предубеждение и зомби', 13)
        assert books_rate.books_rating != {'Гордость и предубеждение и зомби', 13}

    def test_absent_book_has_no_rating(self):
        absent_book = BooksCollector()
        absent_book.add_new_book('Гордость и предубеждение и зомби')
        rating = absent_book.get_book_rating('Бойцовский клуб')
        assert rating is None

    def test_add_boot_to_favorites(self):
        favorite_book = BooksCollector()
        favorite_book.add_new_book('Гордость и предубеждение и зомби')
        favorite_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert favorite_book.favorites == ['Гордость и предубеждение и зомби']

    def test_absent_book_has_no_favorites(self):
        no_rate_book = BooksCollector()
        no_rate_book.add_new_book('Гордость и предубеждение и зомби')
        without_rating = no_rate_book.get_book_rating('Бойцовский клуб')
        assert without_rating is None

    def test_remove_book_from_favorites(self):
        del_book = BooksCollector()
        del_book.add_new_book('Гордость и предубеждение и зомби')
        del_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        del_book.delete_book_from_favorites('Гордость и предубеждение и зомби')
        none_lst = del_book.get_list_of_favorites_books()
        assert none_lst == []

    def test_get_books_with_specific_rating(self):
        specific_rating = BooksCollector()
        specific_rating.add_new_book('Гордость и предубеждение и зомби')
        specific_rating.add_new_book('Бойцовский клуб')
        specific_rating.add_new_book('Искусство войны')
        specific_rating.set_book_rating('Бойцовский клуб', 9)
        total = specific_rating.get_books_with_specific_rating(1)
        assert ['Гордость и предубеждение и зомби', 'Искусство войны'] == total

    def test_set_book_rating(self):
        set_rating = BooksCollector()
        set_rating.add_new_book('Гордость и предубеждение и зомби')
        set_rating.set_book_rating('Гордость и предубеждение и зомби', 4)
        assert set_rating.books_rating == {'Гордость и предубеждение и зомби': 4}

