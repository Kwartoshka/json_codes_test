### Инструкция по запуску
Для проверки задачи необходимы следующие шаги:
1. Клонировать проект <br>
`git clone https://github.com/Kwartoshka/json_codes_test.git`
2. Установить зависимости (команда выполняется в корне проекта [где расположен файл manage.py])<br>
`pip install -r requirements.txt`
3. Для генерации кодов запустить команду (команда выполняется в корне проекта [где расположен файл manage.py]):<br/>
`python manage.py createcodes {amount} {group}`
<br>Пример (команда выполняется в корне проекта [где расположен файл manage.py]):<br>
`python manage.py createcodes 11 alaska`
4. Для запуска теста команды генерации (команда выполняется в корне проекта [где расположен файл manage.py]):<br>
`pytest`
5. Проверка кода на существование (команда выполняется в корне проекта [где расположен файл manage.py]):<br>
`python manage.py checkcode {code}`
<br>Пример:<br>
`python manage.py checkcode W5KT64`