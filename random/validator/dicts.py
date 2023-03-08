SSOT_DATA = {
    
    'pear':{'texture':'smooth','color':'green'},
    'apple':{'texture':'smooth','color':'red'},
    'mango':{'texture':'soft','color':'yellow'},
    'banana':{'texture':'soft','color':'yellow'},
    'orange':{'texture':'smooth','color':'orange'},
}


CLOUD_DATA = {
    
    'pear':{'texture':'smooth','color':'green'},
    'apple':{'texture':'smooth','color':'red'},
    'mango':{'texture':'soft','color':'yellow'},
    'banana':{'texture':'soft','color':'yellow'},
    'carrot':{'texture':'rough','color':'orange'}, 
}

VALIDATED_DATA = {}

# width dicts
for fruit in SSOT_DATA:
    if fruit in CLOUD_DATA:
        VALIDATED_DATA[fruit] = SSOT_DATA[fruit]
        
for validated_fruit in VALIDATED_DATA:
    SSOT_DATA.pop(validated_fruit)
    CLOUD_DATA.pop(validated_fruit)
    
print(f'The SSOT DATA: {SSOT_DATA}')
print(f'THE LEFT OVER: {CLOUD_DATA}')
print(f'THE VALIDATED DATA: {VALIDATED_DATA}')