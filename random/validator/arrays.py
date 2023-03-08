SSOT_DATA = ['pear','apple','mango','banana','orange']
CLOUD_DATA = ['pear','apple','mango','orange','carrot']
VALIDATED_DATA = []

# With arrays
for fruit in SSOT_DATA:
    if fruit in CLOUD_DATA:
        VALIDATED_DATA.append(fruit)

for validated_fruit in VALIDATED_DATA:
    SSOT_DATA.pop(SSOT_DATA.index(validated_fruit))
    CLOUD_DATA.pop(CLOUD_DATA.index(validated_fruit))
    

print(f'The SSOT DATA: {SSOT_DATA}')
print(f'THE LEFT OVER: {CLOUD_DATA}')
print(f'THE VALIDATED DATA: {VALIDATED_DATA}')

        