# qa.guru_lesson_8

Основы Python. Часть III. Применение ООП в написании автотестов.

Дополнительные вопросы:

– С чего проще начать выполнение домашнего задания: с тестов или с реализации классов?
 Так как тесты сгруппированы по классу, который они тестируют, и каждый тест называется именем соответствующего ему метода,
 логично начать выполнение домашнего задания с оеализации классов.

– Почему для хранения товаров в корзине используется словарь, а не список?
Использование словаря для хранения товаров в корзине обычно обусловлено необходимостью эффективного доступа к товарам по их идентификаторам или ключам.
Вот несколько причин, почему словарь может быть предпочтительнее списка для этой цели:
1. Уникальность идентификаторов товаров: Каждый товар может иметь уникальный идентификатор или код, который служит ключом в словаре. Это позволяет легко находить товары в корзине по их уникальным идентификаторам.
2. Быстрый доступ по ключу: Словари обеспечивают константное время доступа к элементам по ключу, в отличие от списков, где время доступа может зависеть от размера списка и расположения элемента в нем.
3. Логическая структура: Использование словаря позволяет логически организовать корзину, представляя товары в виде пар "идентификатор товара - количество". Это делает код более понятным и легко поддерживаемым.
4. Возможность хранения дополнительной информации: Кроме количества товаров, в словаре можно хранить дополнительную информацию о каждом товаре, например, его название, цену, скидки и т. д.
Таким образом, использование словаря обеспечивает более эффективное управление корзиной товаров, особенно при большом количестве товаров и операций с ними.

– Зачем нужен hash в классе Product? Изучите этот метод и объясните, почему он нужен.
Хеши используются для быстрого сравнения ключей словаря во время поиска по нему. 
