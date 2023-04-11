import pytest

from main import BooksCollector


# создаем экземпляр (объект) класса BooksCollector
@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector


# добавление книги в экземпляр созданного класса
@pytest.fixture()
def book_zombie(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')


# добавление ещё одной книги в экземпляр созданного класса
@pytest.fixture()
def book_cat(collector):
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')


# добавление ещё одной книги в экземпляр созданного класса
@pytest.fixture()
def book_fight(collector):
    collector.add_new_book('Бойцовкий клуб')