pilot_name = input()
total_distance = float(input())
time_in_hours = float(input())
average_speed = total_distance / time_in_hours

if(average_speed > 227):
  print(f"{pilot_name} se deu muito bem na prova de hoje!!")
elif(average_speed == 227):
  print(f"{pilot_name} teve um ótimo resultado. Mas, acredito que temos potencial para melhorar um pouco mais!")
else:
  print(f"{pilot_name} não se deu tão bem. É preciso melhorar isso!")