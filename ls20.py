import os
import json
import requests
import aiohttp
import asyncio

# ---------- СИНХРОННО: requests ----------
def fetch_json_array_sync():
    url = "https://jsonplaceholder.typicode.com/todos"
    folder = "sync_json"
    os.makedirs(folder, exist_ok=True)

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for obj in data:
            file_path = os.path.join(folder, f"todo_{obj['id']}.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(obj, f, indent=4)
        print(f"✅ Синхронно загружено и сохранено {len(data)} объектов в папку '{folder}'")
    else:
        print("❌ Ошибка загрузки (sync):", response.status_code)

# ---------- АСИНХРОННО: aiohttp ----------
async def fetch_json_array_async():
    url = "https://jsonplaceholder.typicode.com/todos"
    folder = "async_json"
    os.makedirs(folder, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                for obj in data:
                    file_path = os.path.join(folder, f"todo_{obj['id']}.json")
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(obj, f, indent=4)
                print(f"✅ Асинхронно загружено и сохранено {len(data)} объектов в папку '{folder}'")
            else:
                print("❌ Ошибка загрузки (async):", response.status)

# ---------- Запуск ----------
def main():
    fetch_json_array_sync()
    asyncio.run(fetch_json_array_async())

if __name__ == "__main__":
    main()
