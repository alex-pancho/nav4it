## BDD
BDD (behaviour driven development) - подход который объединяет основные принципы и техники
поведения пользователей с идеями из доменно-ориентированного проектирования для
предоставления аналитикам и разработчикам единого инструмента для взаимодействия в
процессе разработки продукта.

Ниже приведен один из примеров теста, написанного с использованием BDD:
```
        Scenario Outline: Testing ACC_TO_ACC_BUDGET direct payment
               Given open site url /ib/#/ib/payments/all
               When "Budget transfer" selected, the "ACC_TO_ACC_BUDGET" form opens
               And wait "4"
               And in the "Source account" field select value <from>
               And input <amo> in the "Amount" field
               And input <nar> in the "Payment details*" field
               And click "Next" button
               And wait "3"
               And click "Sign" button
               And wait "2"
               And in the "Token type" field select value "ETAN"
               And input "value" in the "E-TAN" field
               And click "Confirm" button
               And wait "1"
               Then successfully message will be shown
               Examples: accounts
               | from | amo | nar | 
               | "BN41BNUS91601005581700" | "12.34" | "Budget Test" | 
```
В таком виде тест прост для чтения и понимания всеми участниками проекта. Не нужно знать
тонкости технической реализации внутренних механизмов системы для написания тестов и
этим может заниматься кто-то, кроме разработчиков. Это достигается использованием “единого
языка”, полуформального набора терминов для описания бизнес-логики системы. Этот набор
разрабатывается совместно разработчиками и аналитиками, устраняя двойственные трактовки
одних и тех же аспектов бизнес-логики.

Формат описания теста напоминает описание User Story, знакомую использующим Agile
командам. Действительно, они выполняют схожую функцию - описание поведения, которое
представляет ценность для конечного клиента. Также как и в User Story здесь присутствуют
Feature (“Функция” и “Предыстория”) и Acceptance Criteria (“Сценарий”, “Дано-Когда-То”),
помогающие описать требуемое поведение и условия корректности его реализации.
Но как этот человеко читаемый текст транслируется в проверяющий условия код? За это
отвечает файл с “шагами”:
```
        @given(u'диапазон возрастов от {start_age} до {end_age} лет')
        def get_age_range(context, start_age=0, end_age=7):
        context.ages = (float(start_age), float(end_age))
        ...
        @when(u'вычисляется очередь {queue_type}')
        def calculate_specific_queue(context, queue_type):
            types = {
            u'сводная': -1,
            u'общая': 1,
            u'льготная': 2,
            u'переводников': 3
            }
        context.type = types[queue_type]
        context.queue = DeclarationQueue(context.queue_ctx)
        context.queue_decls = context.queue.get_list()[0]
        ...
        @when(u'вычисляется очередь')
        def calculate_default_queue(context):
            context.queue = DeclarationQueue(context.queue_ctx)
            context.queue_decls = context.queue.get_list()[0]
        ...
        @then(u'в очередь попадают только заявления в статусах')
        def check_declaration_selection(context):
            allowed_statuses = [row[u'Статус заявления'] for row in context.table]
            for decl in context.queue_decls:
            assert decl['status__name'] in allowed_statuses, \
            u'Status "%s" not allowed in queue!' % decl['status__name']
```
За написание кода в файле шагов ответственен отдел автоматизации тестирования.


## Подготовка
### Первый запуск
Распаковать содержимое архива фремворка (_test.zip) в папку (напр. D:\_test)
Запустить командную строку Windows:
```
>cmd
```
Создать виртуальное окружение Питон:
```
>python -m venv D:\_test
```

где D:\_test - путь к папке _test
зайти в командной строке в папку _test
напечатать команду
```
>_.bat
```

запустится виртуальное окружение:
```
>(_test) D:\_test>
```

Далее следует установить зависимые пакеты:
```
>(_test) D:\_test>pip install -r requirements.txt
```

### Следующие запуски
Зайти в папку (напр. D:\_test)
Запустить командную строку Windows
```
>cmd
```

напечатать команду
```
>_.bat
```

запустится виртуальное окружение:
```
(_test) D:\_test>
```

## Работа с фреймворком

1. Запуск всех существующих сценариев:
```
>behave
```

2. Запуск сценариев по имени файла сценария:
```
>behave -i crm (запустится тесты CRM)
```

3. Запуск из файла сценария только определенных сценариев:
```
>behave -i crm -n Login -n users (Проверяется логин и тест-кейсы для раздела Users)
```

## Анализ ошибок
Ошибки бывают двух типов: ожидаемые и внеплановые.
Ожидаемые ошибки - не найдено поле, не активна кнопка, поле невидимо, когда должно быть
видимо. Выдаются в понятном виде:

        Assertion Failed: form does not open (форма не открылась)
        Assertion Failed: url of the page does not match the expected. Received url: /urlexample
        Assertion Failed: for field Currency selector visible is False, expected True
        
Такие ошибки  означают, что вместо ожидаемого результата получена ошибка.

Возможные действия:

1. Повторить тест средствами автоматизации
2. Повторить тест вручную.

Если ошибка воспроизводится - завести баг

---