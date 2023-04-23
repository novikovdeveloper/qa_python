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



