# bioisostere-transformations

**The project**
A toolkit for performing common bioisosteric transformations used in medicinal chemistry built in Python.

**⚙️ Functions included**
methyl_swapping → replaces methyl groups
carb_acid_to_tetrazole → classic bioisostere transformation
halogen_scan → H → F substitution 

**🧠 Why it matters**
Bioisosteres are used in drug design to improve stability, potency, and pharmacokinetics, without making a huge change to chemical properties of drugs.

**Example input**
smiles = "CC(=O)O"
print(carb_acid_to_tetrazole(smiles))

**Output**
<img width="516" height="90" alt="image" src="https://github.com/user-attachments/assets/eb267e08-e4a9-4afa-b5dc-33b9e08f2a43" />
<img width="944" height="337" alt="image" src="https://github.com/user-attachments/assets/8c86871f-d9d9-4f1d-a646-860d686dd893" />
<img width="879" height="340" alt="image" src="https://github.com/user-attachments/assets/2e602044-fc2e-4620-9bd8-cd1e82398a70" />


**Tools**
- RDKit
- Python
