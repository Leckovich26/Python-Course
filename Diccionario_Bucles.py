
capitales={"China": "Pekin", "Costa Rica": "San Jose", "Nicaragua": "Managua", "Bangladesh": "Dacca", "India": "Nueva Delhi"}

for key in capitales:
    value=capitales[key]
    print(key)
    print(value)

print(capitales.items())

for clave, valor in capitales.items():
    print(f"{clave} -> {valor}")