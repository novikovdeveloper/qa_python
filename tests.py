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

    def test_add_new_book(self, collector):
        collector.add_new_book("Тестовая книга")
        assert len(collector.get_books_rating()) == 1, "Книга не добавлена!"

    def test_cant_add_same_book_twice(self, collector, book_zombie, book_cat):
        assert len(collector.get_books_rating()) == 2, "Количество книг не равно 2"

    def test_cant_rate_book_not_on_list(self, collector, book_zombie):
        collector.set_book_rating('Бойцовский клуб', 9)
        assert collector.get_books_rating() == {'Гордость и предубеждение и зомби': 1}

    def test_cant_rate_less_one(self, collector):
        collector.add_new_book("Тестовая книга")
        collector.set_book_rating("Тестовая книга", 3)
        collector.set_book_rating("Тестовая книга", 0)
        assert collector.get_book_rating("Тестовая книга") == 3, "Рейтинг книги можно установить менее 1"

    def test_cant_rate_more_ten(self, collector, book_zombie):
        collector.set_book_rating(list(collector.books_rating.keys())[0], 11)
        assert list(collector.books_rating.values())[0] == 1, "Можно установить рейтинг книги больше 10"

    def test_absent_book_has_no_rating(self, collector):
        collector.add_new_book('Искусство войны')
        collector.set_book_rating('Бойцовский клуб', 2)
        assert 'Бойцовский клуб' not in collector.get_books_rating(), 'Недобавленной книге присвоен рейтинг'

    def test_add_book_to_favorites(self, collector):
        collector.add_new_book("какая-то книга")
        collector.add_book_in_favorites('какая-то книга')
        assert len(collector.get_list_of_favorites_books()) == 1
        assert 'какая-то книга' in collector.get_list_of_favorites_books(), "Книга не добавилась в Избранное"

    def test_absent_book_has_no_favorites(self, collector):
        collector.add_book_in_favorites('Искусство войны')
        assert 'Искусство войны' not in collector.favorites, "Несуществующая книга добавилась в Избранное"

    def test_remove_book_from_favorites(self, collector, book_zombie):
        collector.add_book_in_favorites(list(collector.books_rating.keys())[0])
        collector.delete_book_from_favorites(list(collector.books_rating.keys())[0])
        collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 0, "Книга не удалилась из избранного"

    def test_get_books_with_specific_rating(self, collector, book_zombie, book_cat, book_fight):
        collector.set_book_rating(list(collector.books_rating.keys())[0], 1)
        collector.set_book_rating(list(collector.books_rating.keys())[1], 6)
        collector.set_book_rating(list(collector.books_rating.keys())[2], 10)
        assert len(collector.get_books_with_specific_rating(1)) == 1, "Вернулись книги не с тем рейтингом"

    def test_set_book_rating(self, collector, book_zombie):
        collector.add_new_book('Божественная комедия')
        collector.set_book_rating('Божественная комедия', 8)
        assert collector.books_rating.get('Божественная комедия') == 8, "Рейтинг книги не равен установленному"

