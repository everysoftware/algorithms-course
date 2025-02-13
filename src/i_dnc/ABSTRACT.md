# Разделяй и властвуй

## Описание

**Разделяй и властвуй** (Divide and Conquer) - это метод решения задачи, который заключается в разбиении задачи
на более мелкие подзадачи, а затем объединении результатов решения подзадач в решение исходной
задачи. В общем случае алгоритм "разделяй и властвуй" состоит из трех шагов:

1. **Разделение**. Задача разбивается на несколько подзадач, которые являются меньшими экземплярами исходной задачи.
2. **Властвование**. Подзадачи решаются рекурсивно. Если подзадачи достаточно малы, то они решаются непосредственно.
3. **Объединение**. Решения подзадач объединяются в решение исходной задачи.

Важно, что подзадачи должны быть независимыми, то есть решение одной подзадачи не должно зависеть от решения другой.

**Принцип уменьшай и властвуй** (Decrease and Conquer) - это вариация принципа разделяй и властвуй, в которой задача
переходит в более маленькую задачу.

## Применение

Мы уже рассмотрели несколько алгоритмов, которые основаны на принципе разделяй и властвуй:

- Бинарный поиск
- Сортировка слиянием
- Быстрая сортировка
- Алгоритм Евклида
