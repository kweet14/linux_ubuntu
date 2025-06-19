import psutil  """получение информации о системе и процессах"""
import platform  """получение информации об ОС"""
import socket  """работа с сетевыми интерфейсами"""
import time  """работа со временем"""
import getpass  """получение имени текущего пользователя"""
from datetime import datetime  """работа с датой и временем"""


def bytes_to_readable(n):
    """перевод байтов в другие форматы"""
    units = ('Б', 'КБ', 'МБ', 'ГБ', 'ТБ')  
    for unit in units:
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} ПБ"  


def get_ip_addresses():
    """получение IP-адресов сетевых интерфейсов"""
    addresses = {}
    for interface, interface_addresses in psutil.net_if_addrs().items():
        for address in interface_addresses:
            if address.family == socket.AF_INET and not address.address.startswith("127."):
                addresses[interface] = address.address
    return addresses


def top_processes(n=5):
    """получение процессов по загрузке CPU"""
    processes = []

    """сброс значения CPU"""
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    time.sleep(1)

    """получение информации о загрузке CPU"""
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    """сортировка по убыванию"""
    return sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)[:n]


def system_info():
    """информация о системе"""
    print(f"Имя хоста     : {socket.gethostname()}")
    print(f"Пользователь  : {getpass.getuser()}")
    print(f"Время         : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"ОС            : {platform.system()} {platform.release()}")
    uptime = time.strftime('%H:%M:%S', time.gmtime(time.time() - psutil.boot_time()))
    print(f"Аптайм        : {uptime}")


def memory_info():
    """информация об оперативной памяти"""
    mem = psutil.virtual_memory()
    print("\nИспользование оперативной памяти:")
    print(f"Всего     : {bytes_to_readable(mem.total)}")
    print(f"Использовано : {bytes_to_readable(mem.used)} ({mem.percent}%)")
    print(f"Свободно  : {bytes_to_readable(mem.available)}")


def disk_info():
    """информация о дисковом пространстве"""
    disk = psutil.disk_usage('/')
    print("\nИспользование диска (/):")
    print(f"Всего     : {bytes_to_readable(disk.total)}")
    print(f"Использовано : {bytes_to_readable(disk.used)} ({disk.percent}%)")
    print(f"Свободно  : {bytes_to_readable(disk.free)}")


def cpu_info():
    """информация о загрузке процессора"""
    print("\nЗагрузка процессора:")
    print(f"Логических ядер: {psutil.cpu_count(logical=True)}")
    print(f"Загруженность  : {psutil.cpu_percent(interval=1)}%")


def network_info():
    """информация о сетевых интерфейсах и их IP-адресах"""
    print("\nIP-адреса сетевых интерфейсов:")
    for interface, ip in get_ip_addresses().items():
        print(f"  {interface}: {ip}")


def show_processes():
    """вывод списка процессов по загрузке процессора"""
    print("\nТоп-5 процессов по загрузке CPU:")
    for proc in top_processes():
        print(f"PID {proc['pid']:5} | {proc['cpu_percent']:5.1f}% | {proc['name']}")


def show_battery():
    """информация о батарее"""
    battery = psutil.sensors_battery()
    if battery:
        status = "(заряжается)" if battery.power_plugged else "(разряжается)"
        print(f"\nБатарея: {battery.percent}% {status}")
    else:
        print("\nБатарея: недоступна")


def main():
    """вызов всех функций"""
    system_info()
    cpu_info()
    memory_info()
    disk_info()
    network_info()
    show_processes()
    show_battery()


if __name__ == "__main__":
    main()
