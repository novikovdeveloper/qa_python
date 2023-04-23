from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector, book_of_zombie, book_of_cat):
        collector.add_new_book(book_of_zombie)
        collector.add_new_book(book_of_cat)
        assert len(collector.get_books_rating()) == 2, "Количество книг отличное от 2"

    def test_add_new_book(self, collector, book_of_zombie):
        collector.add_new_book(book_of_zombie)
        assert len(collector.get_books_rating()) == 1, "Книга не добавлена!"

    def test_cant_add_same_book_twice(self, collector, book_of_zombie, book_of_cat):
        collector.add_new_book(book_of_zombie)
        collector.add_new_book(book_of_zombie)
        collector.add_new_book(book_of_cat)
        assert len(collector.get_books_rating()) == 2, "Количество книг не равно 2"

    def test_cant_rate_book_not_on_list(self, collector):
        collector.set_book_rating('Бойцовский клуб', 9)
        assert collector.get_books_rating() == {}

    def test_cant_rate_less_one(self, collector, book_of_zombie):
        collector.add_new_book(book_of_zombie)
        collector.set_book_rating(book_of_zombie, 0)
        assert collector.get_book_rating(book_of_zombie) == 1,  "Рейтинг книги можно установить менее 1"

    def test_cant_rate_more_ten(self, collector, book_of_zombie, book_of_war):
        collector.add_new_book(book_of_war)
        collector.set_book_rating(book_of_war, 11)
        assert collector.get_book_rating(book_of_war) != 11, "Можно установить рейтинг книги больше 10"

    def test_absent_book_has_no_rating(self, collector, book_of_war):
        collector.add_new_book(book_of_war)
        collector.set_book_rating(book_of_war, 2)
        assert 'Бойцовский клуб' not in collector.get_books_rating(), 'Не добавленной книге присвоен рейтинг'

    def test_add_book_to_favorites(self, collector, book_of_zombie):
        collector.add_new_book(book_of_zombie)
        collector.add_book_in_favorites(book_of_zombie)
        assert len(collector.get_list_of_favorites_books()) == 1
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books(), "Книга не добавилась в Избранное"

    def test_absent_book_has_no_favorites(self, collector, book_of_war):
        collector.add_book_in_favorites(book_of_war)
        assert 'Искусство войны' not in collector.get_list_of_favorites_books(), "Несуществующая книга добавилась в Избранное"

    def test_remove_book_from_favorites(self, collector, book_of_zombie):
        collector.add_book_in_favorites(book_of_zombie)
        collector.delete_book_from_favorites(book_of_zombie)
        assert len(collector.get_list_of_favorites_books()) == 0, "Книга не удалилась из избранного"

    def test_get_books_with_specific_rating(self, collector, book_of_zombie, book_of_cat, book_of_fight):
        collector.add_new_book(book_of_zombie)
        collector.add_new_book(book_of_cat)
        collector.add_new_book(book_of_fight)
        collector.set_book_rating(book_of_zombie, 1)
        collector.set_book_rating(book_of_cat, 6)
        collector.set_book_rating(book_of_fight, 10)
        assert collector.get_books_with_specific_rating(10) == ['Бойцовский клуб'], "Вернулись книги не с тем рейтингом"

    def test_set_book_rating(self, collector, book_of_war):
        collector.add_new_book(book_of_war)
        collector.set_book_rating(book_of_war, 8)
        assert collector.get_books_rating() == {'Искусство войны': 8}, "Рейтинг книги не равен установленному"
