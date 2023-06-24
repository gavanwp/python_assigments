# import requests
# import json
# '''Pylance  '''
# city = input("Enter your city name")
# url = f"https://api.weatherapi.com/v1/current.json?key=dc92fba4963c47cfbb3191716232206&q={city}"
# r = requests.get(url)
# weather_dic = json.loads(r.text)
# print(weather_dic["location"])

x = ''
if __name__ == '__main__':

    for  i in range(int(input())):
        name = input()
        score = float(input())
        foo = score
        bar = map(float, foo)
        x = min(bar)
        print(x)
    
        
