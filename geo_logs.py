geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def geo_filter(geo_logs):
    geo_logs_copy = []
    for visit in geo_logs:
        for country in visit:
            if visit[country][1] == 'Россия':
                geo_logs_copy.append(visit)
            else:
                pass
    geo_logs = geo_logs_copy
    return geo_logs

for visit in geo_filter(geo_logs):
    print(visit)