rolodex = {
    'Aaron' : 5556069,
    'Bill': 5559824,
    'Dad': 5552603,
    'David': 5558331,
    'Dillon': 5553538,
    'Jim': 5555547,
    'Mom': 5552603,
    'Olivia': 5556397,
    'Verne': 5555309
    }

print(rolodex['Verne'])
print(hash('Verne'))

# adding a dictionary
rolodex['Amanda'] = 5559754
print(rolodex)

rolodex['David'] = 5550902
print(rolodex['David']) # 5550902   // overriding

rolodex['David'] = (5558331, 5550902)   # stored as tuple for multiple items but not good solution just knowledge
print(rolodex['David']) # (5558331, 5550902)

rolodex['David'] = 5558331
rolodex['David (Amanda)'] = 5550902

#! reverse lookup function
def caller_id(lookup_number):
    for name, number in rolodex.items():
        if number == lookup_number:
            return name
        
print(caller_id(5556397))   # Olivia
print(caller_id(5552603))   # Dad   // Dad is declared first rather than Mom