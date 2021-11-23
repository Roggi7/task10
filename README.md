# task10

repos for pyCharm task

Пункт 5. Скрин профилировщика filter 
![Скрин1](https://github.com/Roggi7/task10/blob/main/filter_profiler.png)

Пункт 6. Скрин профилировщика old_filter
![Скрин2](https://github.com/Roggi7/task10/blob/main/old_filter_profiler.png)

Можно заметить, что old_filter выполняется быстрее, чем filter. Несмотря на то, что в файле old_filter есть проблема с переполнением беззнакового целого, эта программа всё равно отрабатывает за меньшее время. Но время работы filter начинается с момента ввода значений, из этого следует, что основное время работы filter тратится на ввод данных.

Пункт 7. Был добавлен файл filter_with_filename.py

Пункт 8. Скрин профилировщика filter_with_filename
![Скрин3](https://github.com/Roggi7/task10/blob/main/filter_with_filename.png)

На этом скриншоте видно, что без учёта ввода данных вручную, программа выполняется практически в 2 раза быстрее, чем в первоначальном варианте.

Исходное изображение:
![Исходник](https://github.com/Roggi7/task10/blob/main/img.jpg)

Изображение после преобразования исходным фильтром:
![Результат1](https://github.com/Roggi7/task10/blob/main/res1.jpg)

Изображение после преобразования изменённым фильтром:
![Результат2](https://github.com/Roggi7/task10/blob/main/res.jpg)