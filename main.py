import requests


def get_location(ip_address):
    # Формируем URL для запроса
    url = f"http://ip-api.com/json/{ip_address}"

    try:
        # Отправляем GET-запрос
        response = requests.get(url)

        # Проверяем статус-код ответа
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return {
                    'IP': data['query'],
                    'Country': data['country'],
                    'Region': data['regionName'],
                    'City': data['city'],
                    'ZIP': data['zip'],
                    'Latitude': data['lat'],
                    'Longitude': data['lon'],
                    'ISP': data['isp'],
                }
            else:
                return {'Error': data['message']}
        else:
            return {'Error': 'Не удалось получить данные. Проверьте статус API.'}

    except Exception as e:
        return {'Error': str(e)}


if __name__ == '__main__':
    ip = input("Введите IP-адрес: ")
    location_info = get_location(ip)

    print("Информация о местоположении:")
    for key, value in location_info.items():
        print(f"{key}: {value}")