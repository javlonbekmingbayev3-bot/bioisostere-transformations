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
