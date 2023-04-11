# Список проверок:

Проверка добавления книг - test_add_new_book

Нельзя добавить одну и ту же книгу дважды - test_cant_add_same_book_twice

Нельзя выставить рейтинг книге, которой нет в списке - test_cant_rate_book_not_on_list

Нельзя выставить рейтинг меньше 1 - test_cant_rate_less_one

Нельзя выставить рейтинг больше 10 - test_cant_rate_more_ten

У не добавленной книги нет рейтинга - test_absent_book_has_no_rating

Добавление книги в избранное - test_add_boot_to_favorites

Нельзя добавить книгу в избранное, если её нет в словаре books_rating - test_absent_book_has_no_favorites

Проверка удаления книги из избранного - test_remove_book_from_favorites