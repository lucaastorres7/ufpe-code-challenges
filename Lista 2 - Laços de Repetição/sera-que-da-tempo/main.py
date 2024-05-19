vehicles = int(input())
accident = input() # sim ou nao
distance = float(input())
serial_number = input()
road_accident = 0
traffic = 36 * vehicles / 60
deserialized_code = ""

if(accident == "sim"):
  road_accident += 20

for i in serial_number:
  if(int(i) % 2 == 0):
    deserialized_code += i + "23"
  else:
    deserialized_code += i + "78"

# OPÇÃO A (1km/h and 18,15km/h)
car_distance = (0.2 * distance) # 6
car_time = (car_distance / 1) + road_accident + traffic
jet_distance = (0.8 * distance) # 24
jet_time = jet_distance / 18.15
time_A = jet_time + car_time
rounded_A = int((time_A * 10)) / 10
# OPÇÃO B (0,6666666666666667km/min)
bus_time = (distance / 0.6666666666666667) + road_accident + traffic
# rounded_B = int(bus_time * 10) / 10

# OPÇÃO C (6km em 1min)
helicopter_time = 5 * (distance / 6)
rounded_C = int((helicopter_time * 10)) / 10

print("Análise das opções de transporte até o show!")
print(f"Opção A - Você chegará ao show em {rounded_A} minutos")
print(f"Opção B - Você chegará ao show em {bus_time:.1f} minutos")
print(f"Opção C - Você chegará ao show em {rounded_C} minutos")
print("---")
print(f"Senha de serialização transformada: {deserialized_code}, guarde com segurança!")