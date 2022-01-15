import random

race_list = ["Human", "Dwarf"]
gender_list = ["Male", "Female"]
occupation_list = ["Blacksmith", "Labourer", "Sailor"]
demeanour_list = ["Surly", "Mysterious", "Exhausted", "Happy"]

test_names = ["Steve", "Brian", "Susan", "Betty"]

human_male_names = []
human_female_names = []
dwarf_male_names = []
dwarf_female_names = []

def generate_race():
    race = race_list[random.randrange(0, len(race_list))]
    return race

def generate_gender():
    gender_identity = gender_list[random.randrange(0, len(gender_list))]
    return gender_identity

def generate_occupation():
    occupation = occupation_list[random.randrange(0, len(occupation_list))]
    return occupation

def generate_demeanour():
    demeanour = demeanour_list[random.randrange(0, len(demeanour_list))]
    return demeanour

def generate_name():
    name = test_names[random.randrange(0, len(test_names))]
    return name


print(f"Race: {generate_race()}")
print(f"Gender Identity: {generate_gender()}")
print(f"Occupation: {generate_occupation()}")
print(f"Demeanour: {generate_demeanour()}")
print(f"Name: {generate_name()}")



# Notes
# Name based on race/gender
# Gender Identity complexity – Combine gendered name lists
# Populate lists with Basic Races in PHB, appropriate occupations and demeanours.
# Extended Races in PHB
# Extended Names in Xanathar's