# 🔧 Python_Ubuntu
Простой консольный инструмент для отображения системной информации на Python с использованием библиотеки `psutil`.

## 📋 Описание

Скрипт собирает и отображает следующую информацию:

- 🖥️ Имя хоста, имя пользователя, ОС, аптайм
- 🔥 Загрузка процессора и количество логических ядер
- 🧠 Использование оперативной памяти
- 💾 Использование дискового пространства
- 🌐 IP-адреса всех сетевых интерфейсов
- 🔧 Топ-5 процессов по загрузке CPU
- 🔋 Статус батареи (если доступен)

Вывод информации осуществляется на русском языке.

## 🛠️ Зависимости

Перед запуском убедитесь, что у вас установлены следующие библиотеки:

- Python 3.6 или новее
- [psutil](https://pypi.org/project/psutil/)

## ⚙️ Установка

1. Клонируйте репозиторий или сохраните файл `monitor.py`.

2. Установите зависимости:

```bash
pip install psutil
```
3. Запустите скрипт:

```bash
python monitor.py
```

## Пример вывода
```bash
Имя хоста     : my-computer
Пользователь  : user
Время         : 2025-06-18 12:34:56
ОС            : Windows 10
Аптайм        : 05:12:48

Загрузка процессора:
Логических ядер: 8
Загруженность  : 23.5%

Использование оперативной памяти:
Всего     : 15.9 ГБ
Использовано : 7.2 ГБ (45.2%)
Свободно  : 8.3 ГБ

Использование диска (/):
Всего     : 475.8 ГБ
Использовано : 232.5 ГБ (48.9%)
Свободно  : 243.3 ГБ

IP-адреса сетевых интерфейсов:
  Ethernet: 192.168.1.10

Топ-5 процессов по загрузке CPU:
PID  1234 |  25.0% | python.exe
...


Батарея: 94% (заряжается)
```


## Автор

Кальметьев Эрик 302ИС-22 

Преподаватель: Гусятинер Леонид Борисович
