import time # время
import requests # HTTP запросы

def getPacket():
    adress = input("Введите адрес, к которому будем стучаться: ")

    requests_times = []
    global_bytes = 0
    global_start = time.perf_counter()
    
    for i in range(10):
        start = time.perf_counter()
        response = requests.get(adress, timeout=30)
        response.raise_for_status()
        end = time.perf_counter()
        elapsed = end - start
        size_byte = len(response.content) # размер в байтах
        size_mb = size_byte / (1024 * 1024) # перевод в мегабайты
        requests_times.append(elapsed)
        global_bytes += len(response.content)
        print(f"Запрос №{i + 1}: {round(elapsed, 2)} sec, {round(size_mb, 4)} mb")

    average_times = sum(requests_times) / len(requests_times)
    global_mb = global_bytes / (1024 * 1024)
    global_end = time.perf_counter()
    global_time = global_end - global_start
    speed_mbps = (global_bytes * 8) / (global_time * 1000000)

    print("============ Общая информация о данных: ============")
    print(f"Среднее время скачанных данных со всех запросов: {round(average_times, 2)} sec")
    print(f"Общее количество скачанных данных: {round(global_mb, 4)} mb")
    print(f"Скорость скачивания: {round(speed_mbps, 2)} mbps")

if __name__ == "__main__":
    getPacket()