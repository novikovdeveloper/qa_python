import pytest

from main import BooksCollector


# создаем экземпляр (объект) класса BooksCollector
@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture()
def book_of_zombie():
    return 'Гордость и предубеждение и зомби'


@pytest.fixture()
def book_of_cat():
    return 'Что делать, если ваш кот хочет вас убить'


@pytest.fixture()
def book_of_fight():
    return 'Бойцовский клуб'


@pytest.fixture()
def book_of_war():
    return 'Искусство войны'


@pytest.fixture()
def add_book_of_war(collector):
    collector.add_new_book('Искусство войны')
    return add_book_of_war


@pytest.fixture()
def add_book_of_zombie(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    return add_book_of_zombie


@pytest.fixture()
def add_book_of_cat(collector):
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    return add_book_of_cat


@pytest.fixture()
def add_book_of_fight(collector):
    collector.add_new_book('Бойцовский клуб')
    return add_book_of_fight
