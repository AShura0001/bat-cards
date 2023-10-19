import os

class character:
    def __init__(self, 
                 name, title, form,
                 rank, ATK, HP, DP, SP, Battle_IQ,
                 rank_flag, atk_flag, hp_flag, dp_flag, sp_flag, iq_flag,
                 rating, signature_move, 
                 card_image):
        self.name = name
        self.title = title
        self.form = form
        self.rank = rank
        self.ATK = ATK
        self.HP = HP
        self.DP = DP
        self.SP = SP
        self.IQ = Battle_IQ 
        self.rank_flag = rank_flag
        self.atk_flag = atk_flag
        self.hp_flag = hp_flag
        self.dp_flag = dp_flag
        self.sp_flag = sp_flag
        self.iq_flag = iq_flag
        self.rating = rating
        self.signature_move = signature_move
        self.card_image = card_image
        pass

'''
list 52 characters from seven deadly sins anime based on strength and mention
their title form and rank etc in the class defined above but limit the attributes as follows:

name - name
form - form
title - any designation
rank - 0 to 60
atk - 0 to 5000 i.e. Attack Power
hp - 0 to 5000 i.e. Health Power
dp - 0 to 5000 i.e. Defence Power
sp - 0 to 5000 i.e. Speed Power
iq - 0 to 5000 i.e. Battle IQ
rating - SSS+, SS, S, A, B, C, D and U (U for undefined; should be most rare rating)
signature_move - name of the signature move
card_image - image of the card
'''

cwd = os.getcwd()

meliodas_demon_king = character(
    "Meliodas", "Captain of the Seven Deadly Sins", "Demon King Form",
    "01", 4782, 4905, 4678, 4982, 5000,
    True, True, True, True, True, True,
    "SSS", "Full Counter",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "1_meliodas_demon_king.png")))

escanor_the_one = character(
    "Escanor", "Lion's Sin of Pride", "The One Form - Daytime",
    "02", 4939, 4532, 4541, 4919, 4957,
    True, True, True, True, True, True,
    "SSS+", "Pride Flare",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "2_escanor_the_one.png")))

merlin_boar_sin = character(
    "Merlin", "Boar's Sin of Gluttony", "Normal Form",
    "03", 4639, 4571, 4637, 4779, 4859,
    True, True, True, True, True, True,
    "SS", "Perfect Cube",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "3_merlin_normal.png")))

king_spirit_spear = character(
    "King", "Grizzly's Sin of Sloth", "True Spirit Spear Chastiefol",
    "04", 4154, 3709, 3712, 4041, 4079,
    True, True, True, True, True, True,
    "SS", "Disaster",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "4_king_spirit_spear.png")))

gowther_demon = character(
    "Gowther", "Goat's Sin of Lust", "Demon Gowther",
    "05", 3809, 3849, 4124, 3803, 4150,
    True, True, True, True, True, True,
    "SS", "Invasion",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "5_gowther_demon.png")))

ban_purgatory = character(
    "Ban", "Fox's Sin of Greed", "Post-Purgatory Form",
    "06", 3440, 3384, 3369, 3209, 3628,
    True, True, True, True, True, True,
    "A", "Fox Hunt",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "6_ban_purgatory.png")))

diane_gideon = character(
    "Diane", "Serpent's Sin of Envy", "Giant Form - Gideon",
    "07", 3104, 3406, 3347, 3941, 3440,
    True, True, True, True, True, True,
    "A", "Mother Catastrophe",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "7_diane_gideon.png")))

zeldris_demon_king_rep = character(
    "Zeldris", "Demon King's Right Hand", "Ominous Nebula Form",
    "08", 3444, 3192, 3352, 3233, 3079,
    True, True, True, True, True, True,
    "A", "Dark Nebula",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "8_zeldris_demon_king_rep.png")))

estarossa_fake_demon = character(
    "Estarossa", "Fallen Archangel", "Love Commandment Form",
    "09", 2705, 2502, 3359, 2801, 3237,
    True, True, True, True, True, True,
    "A", "Crimson Requiem",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "9_estarossa_fake_demon.png")))

mael_strongest_archangel = character(
    "Mael", "Strongest Archangel", "Sunshine Form",
    "10", 2592, 2835, 2261, 2668, 2996,
    True, True, True, True, True, True,
    "A", "Ark",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "10_mael_strongest_archangel.png")))

chandler_demonic_sorcerer = character(
    "Chandler", "Demonic Sorcerer", "Original Demon Form",
    "11", 1773, 2133, 1680, 1510, 2463,
    True, True, True, True, True, True,
    "A", "Dark Nebula",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "11_chandler_demonic_sorcerer.png")))

cusack_mystic_enigma = character(
    "Cusack", "Mystic Enigma", "Original Demon Form",
    "12", 2142, 2159, 1581, 1632, 1769,
    True, True, True, True, True, True,
    "A", "Black Hole",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "12_cusack_mystic_enigma.png")))

ludociel_heavenly_luminary = character(
    "Ludociel", "Heavenly Luminary", "Grace",
    "13", 1570, 1581, 1642, 1751, 1691,
    True, True, True, True, True, True,
    "B", "Flash",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "13_ludociel_heavenly_luminary.png")))

derieri_purity = character(
    "Derieri", "Purity Incarnate", "Purity Form",
    "14", 1968, 1666, 1735, 1645, 1501,
    True, True, True, True, True, True,
    "B", "Combo Star",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "14_derieri_purity.png")))

monspeet_hellfire_master = character(
    "Monspeet", "Hellfire Master", "Reticence Form",
    "15", 1202, 1324, 1535, 1471, 1587,
    True, True, True, True, True, True,
    "B", "Hellfire Bird",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "15_monspeet_hellfire_master.png")))

sariel_skyward_guardian = character(
    "Sariel", "Skyward Guardian", "Tornado Form",
    "16", 1720, 1662, 1074, 1675, 1059,
    True, True, True, True, True, True,
    "C", "Tempest Wing",
    str(os.path.join(cwd, "assets", "cards", "seven deadly sins cards", "16_sariel_skyward_guardian.png")))

# tarmiel_oceanic_protector = character(
#     "Tarmiel", "Oceanic Protector", "Tornado Form",
#     17, 3533, 3356, 3622, 3264,  3533,
#     True, True, True, True, True, True,
#     "B", "Ocean Seal")

# king_fairy_king = character(
#     "King", "Fairy King", "Fairy King Form",
#     18, 3622, 3264, 3533, 3356,  3622,
#     True, True, True, True, True, True,
#     "B", "True Spirit Spear")

# ban_immortal_thief = character(
#     "Ban", "Immortal Thief", "Human Form",
#     19, 3264, 3264, 3622, 3533,  3356,
#     True, True, True, True, True, True,
#     "C", "Snatch")

# elaine_wind_wielder = character(
#     "Elaine", "Wind Wielder", "Forest Guardian Form",
#     20, 3445, 3445, 3264, 3264,  3445,
#     True, True, True, True, True, True,
#     "C", "Wind Manipulation")

# galand_crimson_goliath = character(
#     "Galand", "Crimson Goliath", "Colossal Form",
#     21, 3078, 3264, 3078, 3264,  3264,
#     True, True, True, True, True, True,
#     "D", "Critical Over")

# meliodas_berserk_form = character(
#     "Meliodas", "Sealed Wrath", "Berserk Form",
#     22, 3167, 3264, 3167, 3167,  3264,
#     True, True, True, True, True, True,
#     "D", "Puppeteer")

# hawk_talking_sage = character(
#     "Hawk", "The Talking Sage", "Talking Pig Form",
#     23, 3078, 3078, 3264, 3167,  3167,
#     True, True, True, True, True, True,
#     "D", "Snort")

# hawk_mama_huge_mother = character(
#     "Hawk Mama", "The Huge Mother", "Huge Mother Form",
#     24, 0, 5000, 5000, 5000,  5000,
#     True, True, True, True, True, True,
#     "U", "Mother Charge")

# twigo_timid_fighter = character(
#     "Twigo", "Timid Fighter", "Normal Form",
#     25, 3167, 3167, 3078, 3167,  3078,
#     True, True, True, True, True, True,
#     "D", "Cower")

# guila_explosive_warrior = character(
#     "Guila", "Explosive Warrior", "Armored Form",
#     26, 3264, 3078, 3078, 3167,  3264,
#     True, True, True, True, True, True,
#     "D", "Explosion Arrow")

# griamore_fortress_keeper = character(
#     "Griamore", "Fortress Keeper", "Increased Size Form",
#     27, 3078, 3264, 3078, 3078,  3264,
#     True, True, True, True, True, True,
#     "D", "Wall")

# elaine_aerial_huntress = character(
#     "Elaine", "Aerial Huntress", "Aerial Huntress Form",
#     28, 3167, 3167, 3078, 3167,  3167,
#     True, True, True, True, True, True,
#     "D", "Aerial Hunt")

# gideon_earthshaker = character(
#     "Gideon", "Earthshaker", "Giant Golem Form",
#     29, 3264, 3078, 3264, 3078,  3078,
#     True, True, True, True, True, True,
#     "D", "Earthquake")

# oslo_shadow_grabber = character(
#     "Oslo", "Shadow Grabber", "Black Hound Form",
#     30, 3167, 3167, 3167, 3078,  3167,
#     True, True, True, True, True, True,
#     "D", "Shadow Grab")

# albion_demonic_behemoth = character(
#     "Albion", "Demonic Behemoth", "Behemoth Form",
#     31, 2890, 3078, 2890, 3078,  3078,
#     True, True, True, True, True, True,
#     "E", "Destruction Roar")

# galand_crimson_demon = character(
#     "Galand", "Crimson Demon", "Normal Form",
#     32, 2981, 3078, 2981, 2981,  3078,
#     True, True, True, True, True, True,
#     "E", "Critical Over")

# meliodas_huggable_hero = character(
#     "Meliodas", "Huggable Hero", "Plush Toy Form",
#     33, 3078, 2981, 3078, 3078,  2981,
#     True, True, True, True, True, True,
#     "E", "Puppeteer")

# gustaf_fearless_guard = character(
#     "Gustaf", "Fearless Guard", "Normal Form",
#     34, 2981, 2981, 3078, 3078,  3078,
#     True, True, True, True, True, True,
#     "E", "Brave Shield")

# nadja_kind_soul = character(
#     "Nadja", "Kind Soul", "Normal Form",
#     35, 2890, 2890, 3078, 3078,  2981,
#     True, True, True, True, True, True,
#     "E", "Warm Embrace")

# jenna_fiery_maiden = character(
#     "Jenna", "Fiery Maiden", "Normal Form",
#     36, 2981, 3078, 2981, 2981,  3078,
#     True, True, True, True, True, True,
#     "E", "Flame Burst")

# weinheidt_caring_smith = character(
#     "Weinheidt", "Caring Smith", "Normal Form",
#     37, 3078, 2981, 2981, 3078,  2981,
#     True, True, True, True, True, True,
#     "E", "Forge Master")

# solaseed_floral_warrior = character(
#     "Solaseed", "Floral Warrior", "Normal Form",
#     38, 2981, 2981, 3078, 2981,  2981,
#     True, True, True, True, True, True,
#     "E", "Blossom Strike")

# taizoo_roaring_lion = character(
#     "Taizoo", "Roaring Lion", "Normal Form",
#     39, 3078, 3078, 2981, 2981,  2981,
#     True, True, True, True, True, True,
#     "E", "Lion's Roar")

# ban_the_outlaw = character(
#     "Ban", "The Outlaw", "Human Form",
#     40, 2981, 2890, 2890, 2981,  2981,
#     True, True, True, True, True, True,
#     "E", "Thief's Grin")

# elaine_wind_sorceress = character(
#     "Elaine", "Wind Sorceress", "Wind Sorceress Form",
#     41, 2981, 2890, 2981, 2981, 2890,
#     True, True, True, True, True, True,
#     "E", "Gale Manipulation")

# golgius_silent_shadow = character(
#     "Golgius", "Silent Shadow", "Normal Form",
#     42, 2890, 2981, 2890, 2981,  2981,
#     True, True, True, True, True, True,
#     "E", "Stealth Strike")

# guila_explosive_archer = character(
#     "Guila", "Explosive Archer", "Armored Form",
#     43, 3078, 2981, 2981, 2981,  2981,
#     True, True, True, True, True, True,
#     "E", "Explosive Arrow")

# griamore_human_fortress = character(
#     "Griamore", "Human Fortress", "Human Form",
#     44, 3078, 2890, 2890, 2981,  2981,
#     True, True, True, True, True, True,
#     "E", "Shield of Valor")

# veronica_valiant_princess = character(
#     "Veronica Liones", "Valiant Princess", "Normal Form",
#     45, 2981, 2981, 2890, 3078,  2890,
#     True, True, True, True, True, True,
#     "E", "Royal Grace")

# gustaf_fearless_knight = character(
#     "Gustaf", "Fearless Knight", "Normal Form",
#     46, 2981, 2981, 2981, 3078,  2981,
#     True, True, True, True, True, True,
#     "E", "Brave Charge")

# nadja_nurturing_spirit = character(
#     "Nadja Liones", "Nurturing Spirit", "Normal Form",
#     47, 3078, 3078, 2890, 2981,  2981,
#     True, True, True, True, True, True,
#     "E", "Guiding Light")

# jenna_blazing_damsel = character(
#     "Jenna", "Blazing Damsel", "Normal Form",
#     48, 2981, 3078, 2981, 2981,  3078,
#     True, True, True, True, True, True,
#     "E", "Inferno Blaze")

# weinheidt_master_forger = character(
#     "Weinheidt", "Master Forger", "Normal Form",
#     49, 3078, 2981, 2981, 3078,  2890,
#     True, True, True, True, True, True,
#     "E", "Craftsman's Touch")

# solaseed_floral_artist = character(
#     "Solaseed", "Floral Artist", "Normal Form",
#     50, 2981, 2981, 2981, 2981,  3078,
#     True, True, True, True, True, True,
#     "E", "Petal Splash")

# griamore_human_fortress = character(
#     "Griamore", "Human Fortress", "Human Form",
#     51, 3078, 2890, 2890, 2981,  2981,
#     True, True, True, True, True, True,
#     "E", "Shield of Valor")

# veronica_noble_lady = character(
#     "Veronica Liones", "Noble Lady", "Normal Form",
#     52, 2890, 2981, 2981, 2981,  2890,
#     True, True, True, True, True, True,
#     "E", "Royal Elegance")


sevendeadlysins_index = {
    1 : meliodas_demon_king,
    2 : escanor_the_one,
    3 : merlin_boar_sin,
    4 : king_spirit_spear,
    5 : gowther_demon,
    6 : ban_purgatory,
    7 : diane_gideon,
    8 : zeldris_demon_king_rep,
    9 : estarossa_fake_demon,
    10 : mael_strongest_archangel,
    11 : chandler_demonic_sorcerer,
    12 : cusack_mystic_enigma,
    13 : ludociel_heavenly_luminary,
    14 : derieri_purity,
    15 : monspeet_hellfire_master,
    16 : sariel_skyward_guardian
    }