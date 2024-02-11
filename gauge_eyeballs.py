# By Kami Bigdely
# Introduce explaining variable (alias extract variable)
# Reference: https://www.researchgate.net/publication/305768969_The_role_of_eye_characteristics_in_facial_beauty_likability_and_attractiveness
import math

# Background: You are a computer engineer trying to sift through many profiles to find your soulmate. 
# Unfortunately, there are too many profiles and it's getting tedious. 
# You write a python script to scrape profiles info (such as height, age, etc) and images (for image processing) 
# to figure out automatically who is attractive to you.

# Here is a part of the script:
# assuming you have extracted the following info from the profile's image.

eye_size = 0.47    # [cm^2]
eye_width = 24.2   # [mm]
eye_height = 23.7  # [mm]

iris_width = 20.2  # [mm]
iris_height = 19.7 # [mm]

# Calculate the area of iris
iris_area = math.pi * iris_width / 2 * iris_height / 2

# Define thresholds for attractiveness
min_eye_size = 0.45
min_iris_to_eye_ratio = 0.69
min_eye_height_to_width_ratio = 0.59

# Check if the eye is considered attractive
is_attractive_eye = eye_size > min_eye_size and iris_area / eye_size >= min_iris_to_eye_ratio \
                    and eye_height / eye_width >= min_eye_height_to_width_ratio

if is_attractive_eye:
    print("I’m sorry I wasn’t part of your past, can I make it up by being in your future?")