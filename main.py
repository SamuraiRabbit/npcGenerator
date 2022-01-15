import random

race_list = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]
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

dragonborn_male_names = ["Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Mehen", "Nadarr", "Pandjed", "Patrin", "Rhogar", "Shamash", "Shedinn", "Tarhun", "Torinn"]
dragonborn_female_names = ["Akra", "Biri", "Daar", "Farideh", "Harann", "Havilar", "Jheri", "Kava", "Korinn", "Mishann", "Nala", "Perra", "Raiann", "Sora", "Surina", "Thava", "Uadjit"]
dragonborn_nb_names = dragonborn_male_names + dragonborn_female_names

gnome_male_names = ["Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin", "Frug", "Gerbo", "Gimble", "Glim", "Jebeddo", "Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo", "Sindri", "Warryn", "Wrenn", "Zook"]
gnome_female_names = ["Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick", "Lilli", "Loopmottin", "Lorilla", "Mardnab", "Nissa", "Nyx", "Oda", "Orla", "Roywyn", "Shamil", "Tana", "Waywocket", "Zanna"]
gnome_nb_names = gnome_male_names + gnome_female_names

half_elf_male_names = elf_male_names + human_male_names
half_elf_female_names = elf_female_names + human_female_names
half_elf_nb_names = half_elf_male_names + half_elf_female_names

half_orc_male_names = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Mhurren", "Ront", "Shump", "Thokk"]
half_orc_female_names = ["Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha", "Sutha", "Vola", "Volen", "Yevelda"]
half_orc_nb_names = half_orc_male_names + half_orc_female_names

tiefling_male_names = ["Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech", "Mordai", "Morthos", "Pelaios", "Skamos", "Therai"]
tiefling_female_names = ["Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia", "Orianna", "Phelaia", "Rieta"]
tiefling_nb_names = tiefling_male_names + tiefling_female_names

def generate_npc():
    race = generate_race()
    print(f"Race: {race}")
    gender_identity = generate_gender()
    print(f"Gender: {gender_identity}")
    name = generate_name(race, gender_identity)
    print(f"Name: {name}")
    occupation = generate_occupation()
    print(f"Occupation: {occupation}")
    demeanour = generate_demeanour()
    print(f"Demeanour: {demeanour}")


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
            
        case ("Dragonborn", "Male"):
            name = dragonborn_male_names[random.randrange(0, len(dragonborn_male_names))]
        case ("Dragonborn", "Female"):
            name = dragonborn_female_names[random.randrange(0, len(dragonborn_female_names))]
        case ("Dragonborn", "Non-Binary"):
            name = dragonborn_nb_names[random.randrange(0, len(dragonborn_nb_names))]
        
        case ("Gnome", "Male"):
            name = gnome_male_names[random.randrange(0, len(gnome_male_names))]
        case ("Gnome", "Female"):
            name = gnome_female_names[random.randrange(0, len(gnome_female_names))]
        case ("Gnome", "Non-Binary"):
            name = gnome_nb_names[random.randrange(0, len(gnome_nb_names))]
        
        case ("Half-Elf", "Male"):
            name = half_elf_male_names[random.randrange(0, len(half_elf_male_names))]
        case ("Half-Elf", "Female"):
            name = half_elf_female_names[random.randrange(0, len(half_elf_female_names))]
        case ("Half-Elf", "Non-Binary"):
            name = half_elf_nb_names[random.randrange(0, len(half_elf_nb_names))]    
        
        case ("Half-Orc", "Male"):
            name = half_orc_male_names[random.randrange(0, len(half_orc_male_names))]
        case ("Half-Orc", "Female"):
            name = half_orc_female_names[random.randrange(0, len(half_orc_female_names))]
        case ("Half-Orc", "Non-Binary"):
            name = half_orc_nb_names[random.randrange(0, len(half_orc_nb_names))] 
            
        case ("Tiefling", "Male"):
            name = tiefling_male_names[random.randrange(0, len(tiefling_male_names))]
        case ("Tiefling", "Female"):
            name = tiefling_female_names[random.randrange(0, len(tiefling_female_names))]
        case ("Tiefling", "Non-Binary"):
            name = tiefling_nb_names[random.randrange(0, len(tiefling_nb_names))] 
                   
    return name

generate_npc()

# Notes
# Expand occupations
# Expand demeanours