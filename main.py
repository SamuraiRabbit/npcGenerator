import random

race_list = ["Dwarf", "Elf", "Halfling", "Human"] # "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]
gender_list = ["Male", "Female", "Non-Binary", "Male", "Female", "Male", "Female", "Male", "Female" ]
occupation_list = ["Blacksmith", "Labourer", "Sailor"]
demeanour_list = ["Surly", "Mysterious", "Exhausted", "Happy"]

dwarf_male_names = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
dwarf_female_names = ["Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl", "Torbera", "Torgga", "Vistra"]
dwarf_nb_names = dwarf_male_names + dwarf_female_names

elf_male_names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
elf_female_names = ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna", "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia"]
elf_nb_names = elf_male_names + elf_female_names

halfling_male_names = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]
halfling_female_names = ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"]
halfling_nb_names = halfling_male_names + halfling_female_names

human_male_names = ["Aseir", "Bardeid", "Haseid", "Khemed", "Mehmen", "Sudeiman", "Zasheir", "Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd", "Bor", "Fodel", "Glar", "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor", "Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Malcer", "Stor", "Taman", "Urth", "Aoth", "Bareris", "Ehput-Ki", "Kethoth", "Mumed", "Ramas", "So-Kehur", "Thazar-De", "Urhur", "Borivik", "Faurgar", "Jandar", "Kanithar", "Madislak", "Ralmevik", "Shaumar", "Vladislak", "An", "Chen", "Chi", "Fai", "Jiang", "Jun", "Lian", "Long", "Meng", "On", "Shan", "Shui", "Wen", "Anton", "Diero", "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"]
human_female_names = ["Atala", "Ceidil", "Hama", "Jasmal", "Meilil", "Seipora", "Yasheira", "Zasheida", "Arveene", "Esvele", "Jhessail", "Kerri", "Lureene", "Miri", "Rowan", "Shandri", "Tessele", "Alethra", "Kara", "Katernin", "Mara", "Natali", "Olma", "Tana", "Zora", "Amafrey", "Betha", "Cefrey", "Kethra", "Mara", "Olga", "Silifrey", "Westra", "Arizima", "Chathi", "Nephis", "Nulara", "Murithi", "Sefris", "Thola", "Umara", "Zolis", "Fyevarra", "Hulmarra", "Immith", "Imzel", "Navarra", "Shevarra", "Tammith", "Yuldra", "Bai", "Chao", "Jia", "Lei", "Mei", "Qiao", "Shui", "Tai", "Balama", "Dona", "Faila", "Jalana", "Luisa", "Marta", "Quara", "Selise", "Vonda"]
human_nb_names = human_male_names + human_female_names

def generate_npc():
    race = generate_race()
    gender_identity = generate_gender()
    name = generate_name(race, gender_identity)
    occupation = generate_occupation()
    demeanour = generate_demeanour()
    return f"""Name: {name}
Gender Identity: {gender_identity}
Race: {race}
Occupation: {occupation}
Demeanour: {demeanour}
"""

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

def generate_name(race, gender_identity):
    match (race, gender_identity):
        case ("Dwarf", "Male"):
            name = dwarf_male_names[random.randrange(0, len(dwarf_male_names))]
        case ("Dwarf", "Female"):
            name = dwarf_female_names[random.randrange(0, len(dwarf_female_names))]
        case ("Dwarf", "Non-Binary"):
            name = dwarf_nb_names[random.randrange(0, len(dwarf_nb_names))]
        
        case ("Elf", "Male"):
            name = elf_male_names[random.randrange(0, len(elf_male_names))]
        case ("Elf", "Female"):
            name = elf_female_names[random.randrange(0, len(elf_female_names))]
        case ("Elf", "Non-Binary"):
            name = elf_nb_names[random.randrange(0, len(elf_nb_names))]
        
        case ("Halfling", "Male"):
            name = halfling_male_names[random.randrange(0, len(halfling_male_names))]
        case ("Halfling", "Female"):
            name = halfling_female_names[random.randrange(0, len(halfling_female_names))]
        case ("Halfling", "Non-Binary"):
            name = halfling_nb_names[random.randrange(0, len(halfling_nb_names))]
            
        case ("Human", "Male"):
            name = human_male_names[random.randrange(0, len(human_male_names))]
        case ("Human", "Female"):
            name = human_female_names[random.randrange(0, len(human_female_names))]
        case ("Human", "Non-Binary"):
            name = human_nb_names[random.randrange(0, len(human_nb_names))]
                     
    return name

print(generate_npc())

# Notes
# Populate lists with Basic Races in PHB, appropriate occupations and demeanours.
# Extended Races in PHB