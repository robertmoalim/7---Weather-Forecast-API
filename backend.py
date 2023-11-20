import requests

API_KEY = "API"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3))

    # def get_data(days):
    #     dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    #     temperatures = [10, 11, 15]
    #     temperatures = [days * i for i in temperatures]
    #     return dates, temperatures
