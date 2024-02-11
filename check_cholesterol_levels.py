# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
def is_good_cholesterol(total_cholostrol, ldl, triglyceride):
    return total_cholostrol < 200 and ldl < 100 and triglyceride < 150

def is_high_cholesterol(total_cholostrol, ldl, triglyceride):
    return (200 < total_cholostrol <= 240) or (130 < ldl <= 160) or (150 <= triglyceride < 200)

def print_good_level_message():
    print('*** Good level of cholesterol ***')

def print_high_level_message():
    print('*** High cholesterol level ***')
    print('Start taking pills such as statins')
    print('Start TLC diet')

def print_tlc_diet_message():
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')

def check_cholesterol_levels(total_cholostrol, ldl, triglyceride):
    if is_good_cholesterol(total_cholostrol, ldl, triglyceride):
        print_good_level_message()
    elif is_high_cholesterol(total_cholostrol, ldl, triglyceride):
        print_high_level_message()
    else:
        print_tlc_diet_message()

if __name__ == "__main__":
    total_cholostrol = 70
    ldl = 30
    triglyceride = 120
    check_cholesterol_levels(total_cholostrol, ldl, triglyceride)