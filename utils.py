from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem, Draw

def methyl_swapping(molecule):
    """Swaps the methyl group of the molecule to a chlorine atom."""

    mol = Chem.MolFromSmiles(molecule)

    LogP = Descriptors.MolLogP(mol)
    M_w = Descriptors.MolWt(mol)

    print("\n--Original Molecule--")
    print("Molecule in SMILES: "+str(molecule))
    print("Molecular weight: " + str(M_w)) 
    print("LogP: " + str(LogP))
    img = Draw.MolToImage(mol)
    img.save("original_molecule.png")
    print("Image saved as original_molecule.png")

    methyl_smiles = Chem.MolFromSmarts("[CH3]")
    chlorine_smiles = Chem.MolFromSmarts("[Cl]")

    new_mol = AllChem.ReplaceSubstructs(mol, methyl_smiles, chlorine_smiles)  # returns a tuple of all possible versions of swap. 

    if new_mol: 
        one_molecule = new_mol[0] 
        one_molecule.UpdatePropertyCache()
        Changed_LogP = Descriptors.MolLogP(one_molecule)
        Changed_M_w = Descriptors.MolWt(one_molecule)


    print("\n--Changed Molecule--")
    print("Molecule in SMILES: "+ str(Chem.MolToSmiles(one_molecule)))
    print("Molecular weight: "+str(Changed_M_w))
    print("LogP: "+str(Changed_LogP))
    img2 = Draw.MolToImage(one_molecule)
    img2.save("changed_molecule.png")
    print("Changed molecules is saved as changed_molecule.png")
    

    print("\n--Overall Change--")
    print("Molecular weight change: " + str(abs(M_w-Changed_M_w)))
    print("LogP change: " + str(abs(LogP-Changed_LogP)))


def carb_acid_to_tetrazole(molecule):
    """Replaces carboxylic acid group with a tetrazole ring."""
    car_acid_pattern = Chem.MolFromSmarts("C(=O)[OH]")
    mol = Chem.MolFromSmiles(molecule)
    tetrazole_ring = Chem.MolFromSmarts("c1nnn[nH]1")

    new_mols = AllChem.ReplaceSubstructs(mol, car_acid_pattern, tetrazole_ring)

    if new_mols:
        new_mol = new_mols[0]
        new_mol.UpdatePropertyCache()

        image_mol = Draw.MolToImage(mol)
        image_mol.save("original_molecule.png")
        print("Image saved as original_molecule_carboxylic_acid.png")

        image_new_mol = Draw.MolToImage(new_mol)
        image_new_mol.save("new_molecule.png")
        print("Image saved as new_molecule.png")


def halogen_scan(molecule):
    """Replaces a hydrogen molecule with a flouring atom in a position that results in minimum TPSA value change."""
    mol = Chem.MolFromSmiles(molecule)
    mol_with_hs = Chem.AddHs(mol)

    hydrogen_pattern  = Chem.MolFromSmarts("[H]")

    flourine_pattern =  Chem.MolFromSmarts("[F]")
    
    new_mols = AllChem.ReplaceSubstructs(mol_with_hs, hydrogen_pattern, flourine_pattern)
    
    d = {}

    for mol in new_mols:
        Chem.SanitizeMol(mol)
        tpsa = Descriptors.TPSA(mol)
        d[tpsa] = mol

    min_tpsa = min(d.keys())


    new_mol = d[min_tpsa]
    new_mol.UpdatePropertyCache()

    image_mol = Draw.MolToImage(mol_with_hs)
    image_mol.save("original_molecule.png")
    print("Image saved as original_molecule_carboxylic_acid.png")

    image_new_mol = Draw.MolToImage(new_mol)
    image_new_mol.save("new_molecule.png")
    print("Image saved as new_molecule.png")
    
    
