import subprocess
from collections import defaultdict


def get_wifi_networks():
    try:
        # Используем nmcli для получения списка сетей
        result = subprocess.run(
            ['nmcli', '-t', '-f', 'SSID,SIGNAL', 'device', 'wifi', 'list'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка: Не удалось получить список Wi-Fi сетей. Убедитесь, что nmcli установлен.")
        print(f"Детали: {e.stderr}")
        exit(1)


def parse_networks(network_lines):
    networks = defaultdict(list)

    for line in network_lines:
        if not line.strip():
            continue
        try:
            ssid, signal = line.split(':')[:2]
            if ssid:  # Игнорируем сети без SSID
                networks[ssid].append(int(signal))
        except ValueError:
            continue

    # Для каждой сети берем максимальный сигнал
    return {ssid: max(signals) for ssid, signals in networks.items()}


def signal_to_dots(signal_strength):
    """Конвертируем силу сигнала в количество точек (1-4)"""
    if signal_strength > 75:
        return '●●●●'
    elif signal_strength > 50:
        return '●●●○'
    elif signal_strength > 25:
        return '●●○○'
    else:
        return '●○○○'


def display_networks(networks):
    # Сортируем сети по силе сигнала (от сильного к слабому)
    sorted_networks = sorted(networks.items(), key=lambda x: x[1], reverse=True)

    print("\nДоступные Wi-Fi сети (сила сигнала):")
    print("-----------------------------------")
    for ssid, signal in sorted_networks:
        dots = signal_to_dots(signal)
        print(f"{dots} {ssid} ({signal}%)")
    print()


if __name__ == "__main__":
    print("Сканирование Wi-Fi сетей...\n")
    networks = get_wifi_networks()
    parsed = parse_networks(networks)
    display_networks(parsed)
