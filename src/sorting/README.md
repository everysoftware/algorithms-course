## Сортировки

Код: `sorting`

### Какие бывают сортировки?

**По сложности:**

- `O(n^2)`: пузырьком, выбором, вставками
- `O(n log n)`: слиянием, быстрая, кучей
- `O(n)`: подсчетом, цифровая

**По способу:**

- Сравнением: пузырьком, выбором, вставками, слиянием, быстрая, кучей
- Подсчетом: подсчетом, цифровая

**По дополнительной памяти:**

- На месте: пузырьком, выбором, вставками, быстрая, цифровая
- Не на месте: слиянием, подсчетом

**По стабильности:**

Стабильная сортировка сохраняет относительный порядок равных элементов. Это значит, что если два объекта имеют
одинаковые ключи в исходном наборе данных, то они будут расположены в том же порядке и в отсортированном наборе
данных. Это особенно важно, когда у нас есть пары ключ-значение с возможными дубликатами ключей.

Нестабильная сортировка не гарантирует сохранение относительного порядка равных элементов. Это значит, что порядок
равных элементов может измениться после сортировки.

Например: у нас есть последовательность цветов и их оттенков `[(red, 1), (green, 2), (red, 3)]`.
Если мы отсортируем эту последовательность по цвету, то стабильная сортировка сохранит относительный порядок
элементов с одинаковым цветом, а нестабильная - нет:

- Стабильная сортировка: `[(red, 1), (red, 3), (green, 2)]`
- Нестабильная сортировка: `[(red, 3), (red, 1), (green, 2)]`

Какие сортировки являются стабильными, а какие нет? Понять это бывает сложно, поэтому я приведу примеры стабильных
и нестабильных сортировок:

- Стабильные пузырьком, вставками, слиянием, подсчетом, цифровая
- Нестабильные: выбором, быстрая, кучей

### Задачи

| Задача                                | Код                |
|---------------------------------------|--------------------|
| Сортировка пузырьком                  | `bubble_sort`      |
| Сортировка выбором                    | `selection_sort`   |
| Сортировка вставками                  | `insertion_sort`   |
| Слияние двух отсортированных массивов | `merge`            |
| Сортировка слияниями                  | `merge_sort`       |
| Разбиение массива                     | `partition`        |
| Быстрая сортировка                    | `quick_sort`       |
| Порядковая статистика                 | `quick_select`     |
| Сортировка подсчетом                  | `counting_sort`    |
| Цифровая сортировка                   | `digit_sort`       |
| Число инверсий                        | `count_inversions` |
| Конкурс сотрудников                   | `competition`      |