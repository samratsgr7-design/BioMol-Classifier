# Project 4: Biomolecules AI Classifier
# PU CET + Stanford Bio-AI prep

amino_acids = {
    "lysine": "Basic, Essential, +ve charge",
    "arginine": "Basic, Essential, +ve charge",
    "histidine": "Basic, Essential, +ve charge",
    "aspartic acid": "Acidic, Non-essential, -ve charge",
    "glutamic acid": "Acidic, Non-essential, -ve charge",
    "valine": "Neutral, Essential, non-polar",
    "leucine": "Neutral, Essential, non-polar",
    "isoleucine": "Neutral, Essential, non-polar",
    "alanine": "Neutral, Non-essential, non-polar",
    "glycine": "Neutral, Non-essential, non-polar",
    "serine": "Neutral, Non-essential, polar",
    "cysteine": "Neutral, Non-essential, polar - has Sulphur"
}

def classify(aa_name):
    aa_name = aa_name.lower().strip()
    if aa_name in amino_acids:
        return f"{aa_name.capitalize()} -> {amino_acids[aa_name]}"
    else:
        return f"{aa_name} not in database. Add it!"

print("--- Biomolecules AI Classifier ---")
print(classify("lysine"))
print(classify("glutamic acid"))
print(classify("serine"))

user_input = input("\nEnter amino acid name: ")
print(classify(user_input))
