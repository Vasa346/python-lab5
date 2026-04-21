# Лабораторная работа №5. Генераторы

## Вариант 8

## Условия задач
Генератор, применяющий заданную функцию к каждому элементу последовательности N раз. Верните только те элементы, которые изменились значительно (зависит от N и типа данных).

## Описание проделанной работы
- Создан репозиторий `python-lab5` на GitHub.
- Склонирован в `D:\Xlam\python\python-lab5`.
- Реализован генератор `significant_change_generator`, применяющий функцию N раз и возвращающий значительно изменившиеся элементы.
- Применены функции `filter` и `reduce` к результатам генератора.
- Реализована многопоточная версия генератора `parallel_significant_change_generator`.
- Написаны модульные тесты с использованием `pytest`.
- Оформлен отчёт.

## Скриншоты результатов
1. Запуск generator.py (обычный и многопоточный генератор)
<img width="930" height="221" alt="изображение" src="https://github.com/user-attachments/assets/a4c9e185-6e5a-4199-83f0-854537c9a69d" />

2. Запуск тестов pytest (4 passed)
<img width="1200" height="283" alt="изображение" src="https://github.com/user-attachments/assets/ef42e14a-1b10-4095-af8f-2e7b5939bd1e" />

3. История коммитов (git log --oneline -5)
<img width="1155" height="110" alt="изображение" src="https://github.com/user-attachments/assets/15070e8f-eea2-496d-99f9-37174d46a24b" />

## Ссылки на используемые материалы
- [Официальная документация Python](https://docs.python.org/3/)
- [Документация pytest](https://docs.pytest.org/)
- [Модуль concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
