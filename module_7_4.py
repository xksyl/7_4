team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

formated_string_1 = 'В команде Мастера кода участников: %s !' % team1_num
formated_string_2 = 'Итого сегодня в командах учасников: %s и %s !' % (team1_num, team2_num)
formated_string_3 = 'Команда Волшебники данных решила задач {} !'.format(score_2)
formated_string_4 = 'Волшебники данных решили задачи за {} !'.format(team1_time)
formated_string_5 = f'Команды решили {score_1} и {score_2} задач.'
formated_string_6 = f'Результат битвы:{challenge_result}!'
formated_string_7 = f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!'

print(formated_string_1)
print(formated_string_2)
print(formated_string_3)
print(formated_string_4)
print(formated_string_5)
print(formated_string_6)
print(formated_string_7)