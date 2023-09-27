class character:
    def __init__(self, 
                 name, title, form,
                 rank, ATK, HP, DP, SP, Battle_IQ,
                 rating, signature_move 
                 ):
        self.name = name
        self.title = title
        self.form = form
        self.rank = rank
        self.ATK = ATK
        self.HP = HP
        self.DP = DP
        self.SP = SP
        self.IQ = Battle_IQ 
        self.rating = rating
        self.signature_move = signature_move
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
'''

meliodas_demon_king = character(
    "Meliodas", "Captain of the Seven Deadly Sins", "Demon King Form",
    1, 4782, 4905, 4678, 4982, 5000,
    "SSS", "Full Counter")

escanor_the_one = character(
    "Escanor", "Lion's Sin of Pride", "The One Form - Daytime",
    2, 4765, 4800, 4950, 4723, 4967,
    "SSS", "Pride Flare")

merlin_boar_sin = character(
    "Merlin", "Boar's Sin of Gluttony", "Normal Form",
    3, 4905, 4678, 4800, 4678, 4905,
    "SS", "Perfect Cube")

king_spirit_spear = character(
    "King", "Grizzly's Sin of Sloth", "True Spirit Spear Chastiefol",
    4, 4782, 4782, 4678, 4905, 4782,
    "SS", "Disaster")

gowther_demon = character(
    "Gowther", "Goat's Sin of Lust", "Demon Gowther",
    5, 4678, 4950, 4678, 4800, 4678,
    "A", "Invasion")

ban_purgatory = character(
    "Ban", "Fox's Sin of Greed", "Post-Purgatory Form",
    6, 4655, 4523, 4800, 4905, 4723,
    "A", "Fox Hunt")

diane_gideon = character(
    "Diane", "Serpent's Sin of Envy", "Giant Form - Gideon",
    7, 4800, 4905, 4550, 4782, 4678,
    "A", "Mother Catastrophe")

zeldris_demon_king_rep = character(
    "Zeldris", "Demon King's Right Hand", "Ominous Nebula Form",
    8, 4678, 4550, 4905, 4678, 4905,
    "S", "Dark Nebula")

estarossa_fake_demon = character(
    "Estarossa", "Fallen Archangel", "Love Commandment Form",
    9, 4905, 4678, 4550, 4678, 4550,
    "S", "Crimson Requiem")

mael_strongest_archangel = character(
    "Mael", "Strongest of Four Archangels", "Sunshine Form",
    10, 4782, 4678, 4678, 4782, 4550,
    "S", "Ark")

chandler_demonic_sorcerer = character(
    "Chandler", "Demonic Sorcerer", "Original Demon Form",
    11, 3356, 3264, 3445, 3356,  3264,
    "C", "Dark Nebula")

cusack_mystic_enigma = character(
    "Cusack", "Mystic Enigma", "Original Demon Form",
    12, 3445, 3356, 3264, 3356,  3445,
    "C", "Black Hole")

ludociel_heavenly_luminary = character(
    "Ludociel", "Heavenly Luminary", "Grace",
    13, 3533, 3445, 3356, 3445,  3533,
    "B", "Flash")

derieri_purity = character(
    "Derieri", "Purity Incarnate", "Purity Form",
    14, 3622, 3622, 3264, 3356,  3622,
    "B", "Combo Star")

monspeet_hellfire_master = character(
    "Monspeet", "Hellfire Master", "Reticence Form",
    15, 3264, 3533, 3622, 3264,  3533,
    "C", "Hellfire Bird")

sariel_skyward_guardian = character(
    "Sariel", "Skyward Guardian", "Tornado Form",
    16, 3356, 3622, 3356, 3264,  3533,
    "C", "Tempest Wing")

tarmiel_oceanic_protector = character(
    "Tarmiel", "Oceanic Protector", "Tornado Form",
    17, 3533, 3356, 3622, 3264,  3533,
    "B", "Ocean Seal")

king_fairy_king = character(
    "King", "Fairy King", "Fairy King Form",
    18, 3622, 3264, 3533, 3356,  3622,
    "B", "True Spirit Spear")

ban_immortal_thief = character(
    "Ban", "Immortal Thief", "Human Form",
    19, 3264, 3264, 3622, 3533,  3356,
    "C", "Snatch")

elaine_wind_wielder = character(
    "Elaine", "Wind Wielder", "Forest Guardian Form",
    20, 3445, 3445, 3264, 3264,  3445,
    "C", "Wind Manipulation")

galand_crimson_goliath = character(
    "Galand", "Crimson Goliath", "Colossal Form",
    21, 3078, 3264, 3078, 3264,  3264,
    "D", "Critical Over")

meliodas_berserk_form = character(
    "Meliodas", "Sealed Wrath", "Berserk Form",
    22, 3167, 3264, 3167, 3167,  3264,
    "D", "Puppeteer")

hawk_talking_sage = character(
    "Hawk", "The Talking Sage", "Talking Pig Form",
    23, 3078, 3078, 3264, 3167,  3167,
    "D", "Snort")

hawk_mama_huge_mother = character(
    "Hawk Mama", "The Huge Mother", "Huge Mother Form",
    24, 0, 5000, 5000, 5000,  5000,
    "U", "Mother Charge")

twigo_timid_fighter = character(
    "Twigo", "Timid Fighter", "Normal Form",
    25, 3167, 3167, 3078, 3167,  3078,
    "D", "Cower")

guila_explosive_warrior = character(
    "Guila", "Explosive Warrior", "Armored Form",
    26, 3264, 3078, 3078, 3167,  3264,
    "D", "Explosion Arrow")

griamore_fortress_keeper = character(
    "Griamore", "Fortress Keeper", "Increased Size Form",
    27, 3078, 3264, 3078, 3078,  3264,
    "D", "Wall")

elaine_aerial_huntress = character(
    "Elaine", "Aerial Huntress", "Aerial Huntress Form",
    28, 3167, 3167, 3078, 3167,  3167,
    "D", "Aerial Hunt")

gideon_earthshaker = character(
    "Gideon", "Earthshaker", "Giant Golem Form",
    29, 3264, 3078, 3264, 3078,  3078,
    "D", "Earthquake")

oslo_shadow_grabber = character(
    "Oslo", "Shadow Grabber", "Black Hound Form",
    30, 3167, 3167, 3167, 3078,  3167,
    "D", "Shadow Grab")

albion_demonic_behemoth = character(
    "Albion", "Demonic Behemoth", "Behemoth Form",
    31, 2890, 3078, 2890, 3078,  3078,
    "E", "Destruction Roar")

galand_crimson_demon = character(
    "Galand", "Crimson Demon", "Normal Form",
    32, 2981, 3078, 2981, 2981,  3078,
    "E", "Critical Over")

meliodas_huggable_hero = character(
    "Meliodas", "Huggable Hero", "Plush Toy Form",
    33, 3078, 2981, 3078, 3078,  2981,
    "E", "Puppeteer")

gustaf_fearless_guard = character(
    "Gustaf", "Fearless Guard", "Normal Form",
    34, 2981, 2981, 3078, 3078,  3078,
    "E", "Brave Shield")

nadja_kind_soul = character(
    "Nadja", "Kind Soul", "Normal Form",
    35, 2890, 2890, 3078, 3078,  2981,
    "E", "Warm Embrace")

jenna_fiery_maiden = character(
    "Jenna", "Fiery Maiden", "Normal Form",
    36, 2981, 3078, 2981, 2981,  3078,
    "E", "Flame Burst")

weinheidt_caring_smith = character(
    "Weinheidt", "Caring Smith", "Normal Form",
    37, 3078, 2981, 2981, 3078,  2981,
    "E", "Forge Master")

solaseed_floral_warrior = character(
    "Solaseed", "Floral Warrior", "Normal Form",
    38, 2981, 2981, 3078, 2981,  2981,
    "E", "Blossom Strike")

taizoo_roaring_lion = character(
    "Taizoo", "Roaring Lion", "Normal Form",
    39, 3078, 3078, 2981, 2981,  2981,
    "E", "Lion's Roar")

ban_the_outlaw = character(
    "Ban", "The Outlaw", "Human Form",
    40, 2981, 2890, 2890, 2981,  2981,
    "E", "Thief's Grin")

elaine_wind_sorceress = character(
    "Elaine", "Wind Sorceress", "Wind Sorceress Form",
    41, 2981, 2890, 2981,  2981,
    2890, "E", "Gale Manipulation")

golgius_silent_shadow = character(
    "Golgius", "Silent Shadow", "Normal Form",
    42, 2890, 2981, 2890, 2981,  2981,
    "E", "Stealth Strike")

guila_explosive_archer = character(
    "Guila", "Explosive Archer", "Armored Form",
    43, 3078, 2981, 2981, 2981,  2981,
    "E", "Explosive Arrow")

griamore_human_fortress = character(
    "Griamore", "Human Fortress", "Human Form",
    44, 3078, 2890, 2890, 2981,  2981,
    "E", "Shield of Valor")

veronica_valiant_princess = character(
    "Veronica Liones", "Valiant Princess", "Normal Form",
    45, 2981, 2981, 2890, 3078,  2890,
    "E", "Royal Grace")

gustaf_fearless_knight = character(
    "Gustaf", "Fearless Knight", "Normal Form",
    46, 2981, 2981, 2981, 3078,  2981,
    "E", "Brave Charge")

nadja_nurturing_spirit = character(
    "Nadja Liones", "Nurturing Spirit", "Normal Form",
    47, 3078, 3078, 2890, 2981,  2981,
    "E", "Guiding Light")

jenna_blazing_damsel = character(
    "Jenna", "Blazing Damsel", "Normal Form",
    48, 2981, 3078, 2981, 2981,  3078,
    "E", "Inferno Blaze")

weinheidt_master_forger = character(
    "Weinheidt", "Master Forger", "Normal Form",
    49, 3078, 2981, 2981, 3078,  2890,
    "E", "Craftsman's Touch")

solaseed_floral_artist = character(
    "Solaseed", "Floral Artist", "Normal Form",
    50, 2981, 2981, 2981, 2981,  3078,
    "E", "Petal Splash")

griamore_human_fortress = character(
    "Griamore", "Human Fortress", "Human Form",
    51, 3078, 2890, 2890, 2981,  2981,
    "E", "Shield of Valor")

veronica_noble_lady = character(
    "Veronica Liones", "Noble Lady", "Normal Form",
    52, 2890, 2981, 2981, 2981,  2890,
    "E", "Royal Elegance")
