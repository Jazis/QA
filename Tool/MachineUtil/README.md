# Описание
Скрипт помогает управлять тестовым стендом

# Функции
`-h`, `--help`                                         - Short banner and full banner\
`--get-req`                                            - Generate requirements\
`--get-license`                                        - Get license\
`-v`, `--verbose`                                      - Show log\
\
`--get-scenarios`                                      - Get scenarios on server\
`--get-configs`                                        - Get configs on server\
`--get-chains`                                         - Get saved presets from server\
`--get-chains-full`                                    - Get full info about presets\
`--get-preset-cmd` <chain number or scenario name>     - Show all variables from configs in as cmd line \
`--get-preset-screen` <chain number or scenario name>  - Show all variables from configs in as simple sceen text \
`--modules` <module-name>                              - Show all modules \
\
`--scenario-local` <local-path-to-scenario>            - run scenario from local machine\
`--scenario-remote` <scenario-name-from-server>        - run scenario from server machine\
`--scenario-description` <scenario-name-from-server>   - Show scenario description\
`--load-module` <module-name>                          - Load module from server
\
`--set-camunda-path`                                   - Set camunda path\
`--install-config` <config-name-from-server>           - Get config from server\
`--import-file` <file-path>                            - File import for easy scenario generation\
\
`--run-chain` <name or number of chain>                - Run selected chain\
`--batch`                                              - Selects default values everywhere\
`--preset` <preset filename>                           - Run chain or scenario with prepared preset\
\
`--clear-temp-logs`                                    - Delete all logs from /tmp/ (locally only)\
`--upgrade`                                            - Install updates from server


# Примеры команд
```
python3 machine-checker.py -h
python3 machine-checker.py --get-req
python3 machine-checker.py --get-scenarios
python3 machine-checker.py --scenario-description new_product_remove.scenario
python3 machine-checker.py --scenario-remote new_product_remove
python3 machine-checker.py --run-chain 2 --preset preset.txt
```

# Установка

Копируем репозиторий
```
git clone https://github.com/Jazis/QA.git
```
Устанавливаем библиотеки
```
python machine-checker.py
```
или
```
python machine-checker.py --get-req
python -m pip install requirements.txt
```

# Описание функций

`-h`, `--help` - Отображение баннера помощи со списком всех команд и расширенного(`--help`) баннера с дополнением в виде списка сценариев и описания к ним. Также возможно получить справку по каждой команде отдельно, добавив `-h` в конце команды
- `python machine-checker.py -h` или `python machine-checker.py --help`


`--get-req` - Генерирует файл requirements.txt в папке со скриптом для дальнейшей установки руками пользователя `python -m pip install requirements.txt`.
- `python machine-checker.py --get-req`

`--get-license` - Получение лицензии на сервере (только локальное использование).
- `python machine-checker.py --get-license`

`-v`, `--verbose` - Отображение детального лога работы программы и запуска сценариев.

`--get-scenarios` - Получение списка сценариев хранящихся на сервере.
- `python machine-checker.py --get-scenarios`

`--get-configs` - Получение списка конфураций хранящихся на сервере.
- `python machine-checker.py --get-configs`\
Информация выводится в виде: `Наименование конфига` -> Install path: `путь установки зараднее прописанный в файле config.manage`

`--get-chains` - Получение списка цепочек
- `python machine-checker.py --get-chains`\
Информация выводится в виде: `[номер цепочки] наименование цепочки`

`--get-chains-full` - Получение списка цепочек и дополнительной информации о хостах и наименованиях сценариев используемых в цепочке.
- `python machine-checker.py --get-chains-full`

`--modules` - Отображение дополнительных модулей

`--get-preset-cmd` - Получение заготовки пресета в виде консольной команды для дальнейшего редактирования  
- `python machine-checker.py --get-preset-cmd`
- - Пример использования команды
```
[login@test-machine-25 ~]# python machine-checker.py --get-preset-cmd 2

python machine-checker.py --run-chain 2  --tag "zookeeper_port=your_value" --tag "clickhouse_port=your_value" --tag "zookeeper_host=your_value" --tag "main_host=your_value" --tag "clickhouse_host=your_value"
```
`2` - номер цепочки\
В ответе команды выдается команда, в которой необходимо заполнить значения поменяв `your_value` на реальное значение.

`--get-preset-screen` - Получение заготовки пресета в виде вывода на экран тела `.txt` файла, для дальнейшего редактирования  
- `python machine-checker.py --get-preset-screen`
- - Пример использования команды
```
[login@test-machine-25 ~]# python machine-checker.py --get-preset-screen 2
zookeeper_port=
clickhouse_port=
zookeeper_host=
main_host=
clickhouse_host=
```
Необходимо создать файл `.txt` (можно дополнить команду ` > preset.txt`) для записи в него вывода команды и заполнения переменных.

`--scenario-local` - Запуск сценариев находящихся на локальном компьютере
- `python machine-checker.py --scenario-local new_product_remove.scenario`

`--scenario-remote` - Запуск сценариев находящихся на сервере
- `python machine-checker.py --scenario-remote new_product_remove.scenario`

`--scenario-description` - Отображение описания сценария 
- `python machine-checker.py --scenario-description new_product_remove.scenario`
- - Пример использования команды
```
[login@test-machine-25 ~]# python machine-checker.py --scenario-description new_product_remove.scenario

Remove all new_product packages by yum
Remove clickhouse
Remove zookeeper

```
`--load-module` - Подключение дополнительного модуля
- `python machine-checker.py --load-module nexus`


`--set-camunda-path` - Установка пути до камунды.

`--install-config` - Установка конфига с сервера, по тому пути, который указан в `config.manage`
- `python machine-checker.py --install-config bpm-platform.xml`

`--import-file` - Позволяет переформатировать обычные текстовые документы с командами в сценарии
- `python machine-checker.py --import-file commands.txt`
- - Первый пример использования команды\
commands.txt в виде простого списка команд. В таком формате - нумерация шагов будет производиться автоматически и тэг action будет заполнятся значением `Manual`.\
```
uptime
touch test.txt
echo "Hi"
```
В кастомном виде.
```
0,Manual,uptime
1,Manual,touch test.txt
2,Manual,echo "Hi"
```

Вывод:
```
[login@test-machine-25 ~]# python machine-checker.py --import-file commands.txt
[01/16/2023, 11:51:04][SUCCESS] - File successfull created!
```
После выполнения команды - создается файл `runme.scenario`. В этот файл записывается новый сценарий.

runme.scenario
```
<id>0</id>
        <action>Manual</action>
        <parameters>uptime</parameters>
<id>1</id>
        <action>Manual</action>
        <parameters>touch test.txt</parameters>
<id>2</id>
        <action>Manual</action>
        <parameters>echo "Hi"</parameters>
```

`--run-chain` - запуск цепочки сценариев
- Одна из версий для использования
```
[login@test-machine-25 ~]#  python machine-checker.py --get-chains 2
[0]Web monitoring clickhouse zookeeper
[1]product Web monitoring clickhouse zookeeper custom
[2]new_product Web monitoring clickhouse zookeeper custom
[3]Remove product
[4]Remove new_product
[5]Lil_test
[6]zookeeper
[7]test_zoo
[8]test

[login@test-machine-25 ~]# python machine-checker.py --get-preset-screen 2 > preset.txt

*preset.txt*
{host}=login@test-machine-999:password
{host}=login@test-machine-999:password
{host}=login@test-machine-999:password
{host}=login@test-machine-999:password
zookeeper_port=2181
clickhouse_port=9000
zookeeper_host=test-machine-999
main_host=test-machine-999
clickhouse_host=test-machine-999

[login@test-machine-25 ~]# python machine-checker.py --run-chain 2 --preset preset.txt
.....

```
Если же не представлен пресет, тогда скрипт будет предлагать вам ввести значение по мере прохождения сценариев и найденных в них метках.

`--batch` - команда предназначена для автоматизации выборов
- Использование - дописать в конец команды

`--preset` - позволяет дополнить исполнение сценария уже заготовленными данными
- `python machine-checker.py --run-chain 2 --preset preset.txt`
Содержимое `preset.txt` в этом случае 
```
*2*
{host}=login@test-machine-999:password
{host}=login@test-machine-999:password
{host}=login@test-machine-999:password
{host}=login@test-machine-999:password
zookeeper_port=2181
clickhouse_port=9000
zookeeper_host=test-machine-999
main_host=test-machine-999
clickhouse_host=test-machine-999
```
`{host}` - в этом параметре данные для входа на необходимую машину. Порядок расположения `{host}` зависит от сценариев расположенных в цепочке.\
Пример:
```
Цепочка - [2]new_product Web monitoring clickhouse zookeeper custom
Список сценариев в цепочке:
1 - zookeeperinstall.scenario - будет использовать test-machine-111
2 - chinstall.scenario - будет использовать test-machine-222
3 - new_productRedosMonitoringWeb.scenario - будет использовать test-machine-333
4 - lil_fix.scenario - будет использовать test-machine-444
```
Файл `preset.txt` будет выглядить так:
```
{host}=login@test-machine-111:password
{host}=login@test-machine-222:password
{host}=login@test-machine-333:password
{host}=login@test-machine-444:password
zookeeper_port=2181
clickhouse_port=9000
zookeeper_host=test-machine-111
main_host=test-machine-333
clickhouse_host=test-machine-222
```
Также пресеты можно использовать в коллаборации с простыми тестами, без указания данных для входа.\
Пример использования:
- `python machine-checker.py --scenario-remote chinstall.scenario --preset preset.txt`

Файл `preset.txt` будет выглядить так:
```
clickhouse_port=9000
clickhouse_host=127.0.0.1
```

`--clear-temp-logs` - удаление временных логов скрипта
- `python machine-checker.py --clear-temp-logs`\
При запуске, скрипт начинает логировать весь поток информации от запуска команд (вне зависимости от тега `-v`) и сохранять его в файлы, в папку `/tmp/`

`--upgrade` - Позволяет обновить программу 
- `python machine-checker.py --upgrade`
