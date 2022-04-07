# Установка
```
sudo apt install python3 -y
sudo apt install python3-pip -y
python3 -m pip install -r requirements.txt
```

## Запуск
```
python3 main.py
``` 

# Файловая структура
```
├── config.ini
├── blanks.settings
├── devices.ini
├── imports
│   ├── connect.py
│   ├── debug.py
│   ├── getter.py
│   ├── messages.py
│   ├── __pycache__
│   └── waiter.py
├── main.py
├── __pycache__
├── requirements.txt
└── tests
    ├── logs
    │   ├── result
    │   └── tests_logs
    ├── SimpleRest
    └── WebSocket
```

# Описание файлов

- <h4>config.ini</h4> 
Файл, с постоянно необходимыми данными для использования в тестах.\
Заранее подготовленный сет из параметров выглядит следующим образом:
>	[host] = qa-lnx-25\
	[subprotocols] = ["wamp.2.json"]\
	[authId] = root\
	[login] = root\
	[password] = admin\
>	[newTestMachine] = qa-lnx-6

Структура строки -> "[наименование_строки] = значение_строки"\
Помимо использования стандартного сета необходимых строк, возможна его модификация и дополнение новыми данными.\
Для использования данных из данного файла, необходимо использовать функцию "from getter import getFromConfig" - она принимает в себя наименование строки\
Пример: serverHost = getFromConfig("host")
- <h4>devices.ini</h4> 
Файл, состоящий из строк - девайсов, необходимых в использовании тестов\
Структура строки -> "[название_теста.py][девайс_с_тегами_для_добавления_через_websocket]"\
Пример строки девайса:

>	["device=Devices::Computers::Linux", "ip=qa-lnx-6", "community=public", "enable-disk-io=false", "enable-disks-changes=false", "split-cpu-by-units=false", "enable-hardware-changes=false",  "enable-process-changes=false",  "enable-software-changes=false",  "enable-arp-changes=false",  "enable-network-changes=false",  "enable-icmp-changes=false",  "enable-tcp-changes=false",  "enable-udp-changes=false",  "replicated=false"]
- <h4>imports</h4>
	Директория с необходимыми библиотеками
- 
	- connect.py - модуль с авторизацией websocket
	- debug.py - модуль дебага для тестов
	- getter.py - модуль для взаимодействия с `../config.ini`
	- messages.py - модуль с необходимыми для тестов сообщениями (используется для сверок в response)
	- waiter.py - модуль с методами ожидания (ожидает необходимого ответа, либо изменения результата)
- <h4>main.py</h4>
Основной файл запуска тестов\
	Запускает тесты из папок "tests/SimpleRest" и "tests/WebSocket"\
	В конфиге `config.ini` есть строка warningFiles она принимает в себя названия файлов, которые лежат в папках с тестами. Они не будут считаться тестами и не будут учитываться при пересчете, либо запуске.\
	Функция авторизации, которая получает seal - использует параметры входа из файла `config.ini` \
	Также встроен генератор строк конфигураций для последующего использования тестами web socket
	- Генератор
      Принимает в себя как одиночные IP адреса, так и домены, и диапазон IP адресов в формате 1.1.1.1-2.2.2.2.\
      У генератора есть 3 режима работы:\
	  `n` или `nothing` - генерирует строку с выключенными флагами дополнительных функций\
	  `a` или `all` - генерирует строку с включенными флагами дополнительных функций\
	  `r` или `random` - генерирует строку со случайно включенными дополнительными функциями\
	  Сгенерированные строки пишет в файл `new_device.ini`
	  Изначальные строки для подставления флагов берет blanks.settings
- <h4>requirements.txt</h4>
Дополнительные модули для python3
- <h4>blanks.settings</h4>
Заготовки строк конфигураций для генератора. Формат строк -> [Тип девайса]=["аргумент0", "аргумент1"].
- <h4>tests</h4>
- tests/
	- logs - директория с логами
		- result - отчеты allure
		- tests_logs - лог консоли(при включенном дебаге - пишет всю информацию)
	- tests - директория с тестами
		- SimpleRest - директория с REST тестами - не нуждающихся в авторизации webSocket'a (имеет многопоточность)
		- WebSocket - директория с тестами под webSocket (выполняется авторизация в websocket и нет многопоточности)\
		
Есть возможность пропуска тестов, достаточно добавить `skip_` в наименование теста и он не будет учитываться при пересчете и запуске.

# Аргументы:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-s,--skip` [filename].py or `bpm,dms` - используется для пропуска одного теста, либо группы тестов. Принимает название групп через запятую\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Изначальное обозначение группы необходимо приписать к названию файла, с использованием знака `_`. Пример: `bpm_testfile.py` 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-h,--help` - выводит краткое пояснение по значению аргументов\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-ot,--only-this` [filename].py or `bpm,dms` - используется для пропуска одного теста, либо группы тестов. Принимает название групп через запятую. См. описание `-s,--skip`\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-ll,--log-level` DEBUG|INFO|OFF - стандартные уровни лога от pytest\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Изначально тесты запускаются с параметром INFO\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-t,--timeout` [default 0.2 sec] - задержка для запусков теста (в локальной сети корректировать ее, а не параметр -th,--threads, так как один поток успевает запускать все тесты, даже со значением 0)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-r,--repeat` [times] - перезапускает FAILED тесты, необходимо указать количество кругов перезапуска\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-th,--threads` [default 4] - установка количества потоков для запуска тестов\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-db,--debug-level` [1] - включения дебага для request в тестах\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--pk --process-killing` [default 180] - кастомная установка таймера на время выполнения теста\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--no-ssl` (demo) - отключает использование серфтификата при запуске теста\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--ssl` (demo) - включает использование серфтификата при запуске теста, если ранее оно было отключено\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-gen, --generate` - генератор конфигураций для девайсов, использует device.ini\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--hash` - используется для передачи хеша билда, для сортировки выходных логов в папки с наименованием в виде этого хеша\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-sr, --start-reconnect-times` [times] - установка количества попыток получения seal сессии\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-sr-time, --start-reconnect-timeout` [sec] - установка задержки между попытками получения seal сессии\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--allure-output-dir` [dir] - позволяет сменить папку для сохраняемых логов allure\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--simple-logs-output-dir` [dir] - позволяет сменить папку для сохраняемых логов вывода консоли\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--delete-logs` - чистка логов\
&nbsp;&nbsp;&nbsp;	Добавляет в файл теста подключение необходимой библиотеки из "../imports/debug.py" и функцию с включением дебага в тест(если ранее в тесте небыло предусмотренно использование дебага). \
&nbsp;&nbsp;&nbsp;	Необходимость иметь в тесте функцию - содержащую в своем наименовании приставку "test_". Дополнит параметры функции, при необходимости.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-wst,--webSocketTests` - запуск только WebSocket тестов из папки "tests/WebSocket"\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-srt,--simpleRestTests` - запуск только REST тестов из папки "tests/SimpleRest"\
	Функция завершения работы мониторит процессы на наличие процессов "pytest". По завершению работы теста - создается allure отчет ("tests/logs/result/") и персональный лог файл консоли ("tests/logs/tests_logs").\

# Примеры использования
	- python3 main.py
			Запустит все тесты. Сначала пойдут тесты webSocket, потом rest.
	- python3 main.py -gen
			Запустить генератор строк для файла device.ini
	- python3 main.py --help
			Выведет подсказку по аргументам
	- python3 main.py -srt
			Запустит только rest тесты.
	- python3 main.py -wst
			Запуск только тестов webSocket
	- python3 main.py -srt -s update_seal.py
			Запуск rest тестов, при этом тест update_seal.py будет пропущен
	- python3 main.py -ot update_seal.py
			Запустится только необходимый тест(если тест из папки "WebSocket", то пройдет авторизацию в веб сокете)
	- python3 main.py --timeout 0.1
			Установит таймаут между тестами на 0.1(default 0.2). В локальной сети параметром можно регулировать скорость потока многопоточных тестов не затрагивая параметра --threads.
	- python3 main.py --debug-level 1
			Запустит все тесты, включит дебаг мод для всех rest запросов
	- python3 main.py --log-level DEBUG
			Запустит все тесты, включит дебаг мод от pytest
	- python3 main.py -srt -ot testme -r 1
			Запустит rest тесты, только группу testme. Перезапустит FAILED тесты 1 раз.
	*Все параметры комбинируются
