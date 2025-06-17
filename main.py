#!/usr/bin/env python3

import subprocess
import re
from collections import defaultdict

def get_wifi_networks():
    try:
        result = subprocess.run(
            ['nmcli', '-t', '-f', 'SSID,SIGNAL', 'device', 'wifi', 'list'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print("Ошибка: Не удалось получить список Wi-Fi сетей. Убедитесь, что nmcli установлен и доступен.")
        print(f"Детали: {e.stderr}")
        exit(1)

def parse_networks(network_lines):
    networks = defaultdict(list)
    for line in network_lines:
        if not line.strip():
            continue
        try:
            ssid, signal = line.split(':')[:2]
            if ssid:
                networks[ssid].append(int(signal))
        except ValueError:
            continue

    return {ssid: max(signals) for ssid, signals in networks.items()}

def signal_to_dots(signal_strength):
    if signal_strength > 75:
        return '●●●●'
    elif signal_strength > 50:
        return '●●●○'
    elif signal_strength > 25:
        return '●●○○'
    else:
        return '●○○○'

def display_networks(networks):
    sorted_networks = sorted(networks.items(), key=lambda x: x[1], reverse=True)

    print("\nДоступные Wi-Fi сети:")
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
