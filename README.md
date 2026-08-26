# Bioisostere Transformations

A Python/RDKit toolkit for exploring common structural transformations used in medicinal chemistry.

The project applies predefined molecular transformations to SMILES structures and generates modified molecular structures that can be inspected computationally.

## ⚙️ Functions

### `methyl_swapping`
Substitutes methyl groups with chlorine atoms.

### `carb_acid_to_tetrazole`
Replaces a carboxylic acid group with a tetrazole ring, representing a commonly studied bioisosteric transformation in medicinal chemistry.

### `halogen_scan`
Performs hydrogen → fluorine substitution to explore halogen-based molecular modifications.

## 🧠 Why Bioisosteric Transformations?

Bioisosteric replacement is a strategy used in medicinal chemistry to modify molecular structures while attempting to preserve or improve desirable biological and physicochemical properties.

Depending on the transformation, these modifications can influence properties such as:

- Potency
- Selectivity
- Metabolic stability
- Solubility
- Pharmacokinetics

The actual effect of a transformation depends on the molecular context and cannot be determined from structural similarity alone.

## Example

```python
smiles = "CC(=O)O"

print(carb_acid_to_tetrazole(smiles))

**Visual Examples**
<img width="516" height="90" alt="image" src="https://github.com/user-attachments/assets/45bdc4d0-35ac-471a-bdd6-10aba410d607" />
<img width="944" height="337" alt="image" src="https://github.com/user-attachments/assets/aba85e1f-3330-4a48-b64c-53613b26dca8" />
<img width="879" height="340" alt="image" src="https://github.com/user-attachments/assets/2b8a810a-90b6-4b06-92ad-20c7f96d15fc" />

🛠️ Tools
Python
RDKit
SMILES / SMARTS
Molecular substructure matching
What I Learned

This project helped me understand how chemical structures can be manipulated programmatically using substructure patterns.

In particular, it introduced me to:

SMILES molecular representations
SMARTS pattern matching
RDKit substructure operations
Programmatic molecular transformations
The computational side of bioisosteric design
Limitations

The transformations are predefined structural operations rather than predictions of biological activity.

A successful structural transformation does not imply that the resulting molecule will have improved potency, safety, pharmacokinetics, or clinical performance.
