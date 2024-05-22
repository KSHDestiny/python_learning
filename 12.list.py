row = ["Ford", "Audi", "BMW", "Lexus"]\

row.append("Mercedes")
print(row)
print(row[4])

row[2] = "Jeep"
print(row)

row.insert(0, "Kia")
print(row)
print(row[4])
print(row.index('Mercedes'))

row.pop(5)
print(row)

row.remove("Jeep")
print(row)

#! Multidimensional lists
lot_2d = [['Toyota', 'Audi', 'BMW'],
            ['Lexus', 'Jeep'],
            ['Honda', 'Kia', 'Mazda']]

lot_3 = [[['Telsa', 'Fiat', 'BMW'],
         ['Honda', 'Jeep'],
         ['Saab', 'Kia', 'Ford']],
         [['Subaru', 'Nissan'],
          ['Volvo']],
          [['Mazda', 'Chevy'],
           [],
           ['Volkswagen']]]

for floor in lot_3:
    for row in floor:
     for car in row:
        print(car)