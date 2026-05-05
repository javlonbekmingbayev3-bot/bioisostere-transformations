from utils import methyl_swapping, carb_acid_to_tetrazole, halogen_scan
from rdkit import Chem

def main():
    print("-- Welcome to Bioisostere Swapper App.")
    while True:
        molecule = input("Enter a molecule in SMILES format: ")
        mol = Chem.MolFromSmiles(molecule)
        if mol is not None:
            break
        else:
            print("Invalid SMILES format input. Try again.")
    print("Menu:")
    print("1. Methyl Swapping")  
    print("2. Substituting carboxylic acid group with a tetrazole ring.")
    print("3. Halogen scan (H -> F) that has minimum TPSA")
    decision = int(input(": "))
    match decision:
        case 1:
            methyl_swapping(molecule)
        case 2:
            carb_acid_to_tetrazole(molecule)
        case 3: 
            halogen_scan(molecule)



if __name__ == "__main__":
    main()
