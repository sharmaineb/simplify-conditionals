# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')

def make_accept_sound():
    print('made acceptance sound')

def has_toxin(ingredients):
    return 'sodium nitrate' in ingredients or \
           'sodium benzoate' in ingredients or \
           'sodium oxide' in ingredients

def alert_about_toxin():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')

def alert_toxin_free():
    print('***')
    print('Toxin Free')
    print('***')

ingredients = ['sodium benzoate']

if has_toxin(ingredients):
    alert_about_toxin()
    make_alert_sound()
else:
    alert_toxin_free()
    make_accept_sound()
