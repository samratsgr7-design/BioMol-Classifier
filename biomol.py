# 🧬 Project 4: Biomolecules AI Classifier 🧬
# 👨‍🔬 PU CET Biology + Stanford Bio-AI Prep

amino_acids = {
    "lysine": "🔵 Basic | ⭐ Essential | +ve charge",
    "arginine": "🔵 Basic | ⭐ Essential | +ve charge",
    "histidine": "🔵 Basic | ⭐ Essential | +ve charge",
    "aspartic acid": "🔴 Acidic | 💤 Non-essential | -ve charge",
    "glutamic acid": "🔴 Acidic | 💤 Non-essential | -ve charge",
    "valine": "⚪ Neutral | ⭐ Essential | non-polar 🧈",
    "leucine": "⚪ Neutral | ⭐ Essential | non-polar 🧈",
    "isoleucine": "⚪ Neutral | ⭐ Essential | non-polar 🧈",
    "alanine": "⚪ Neutral | 💤 Non-essential | non-polar",
    "glycine": "⚪ Neutral | 💤 Non-essential | non-polar",
    "serine": "🟡 Neutral | 💤 Non-essential | polar 💧",
    "cysteine": "🟡 Neutral | 💤 Non-essential | polar - has Sulphur ⚡"
}

def classify(aa_name):
    aa_name = aa_name.lower().strip()
    if aa_name in amino_acids:
        return f"✅ {aa_name.capitalize()} -> {amino_acids[aa_name]}"
    else:
        return f"❌ {aa_name} not in database. Add it! 🧬"

print("="*40)
print("🧬 BIOMOLECULES AI CLASSIFIER 🧬")
print("🚀 PU-CET 2027 | AI Drug Scientist")
print("="*40)
print(classify("lysine"))
print(classify("glutamic acid"))
print(classify("serine"))
print("\n" + "-"*40)
user_input = input("🔍 Enter amino acid name: ")
print(classify(user_input))
print("-"*40)
print("💚 Keep grinding! 19 commits done! 🔥")
