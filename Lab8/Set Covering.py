import json
def findStation(city_list, station):
    city_list = set(city_list)
    ans_list = []
    while city_list:
        max_area, best_station = 0, None
        best_area_cities = set()
        for name, cities in station.items():
            area_cities = city_list.intersection(set(cities))
            if len(area_cities) > max_area:
                max_area = len(area_cities)
                best_station = name
                best_area_cities = area_cities
        if best_station:
            ans_list.append(best_station)
            city_list -= best_area_cities
        else:
            break
    return ans_list

def main():
    city_list = json.loads(input())
    stations = {}
    num = int(input())
    for _ in range(num):
        station = json.loads(input())
        stations[station["Name"]] = station["Cities"]
    ans = findStation(city_list, stations)
    ans.sort()
    print(ans)
main()
