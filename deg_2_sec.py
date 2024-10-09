#Dihedral angle to secondary structure converter

def second_struc(phi,psi):
    if phi is None or psi is None: 
        return 'None'
    elif (-60 <= phi <= -40 and -70 <= psi <= -50):
        return "Right-handed Alpha-helix"
    elif (40 <= phi <= 70 and 30 <= psi <= 60):
        return "Left-handed Alpha-helix"
    elif (-150 <= phi <= 30 and 120 <= psi <= 140):
        return "Beta-sheet"
    else:
        return "Other"

def convert_degs_to_sec(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    convert_coords = []

    for line in lines:
        parts = line.strip().split(' ')
        residue_name = parts[0]
        phi = float(parts[1]) if parts[1].upper().lower() != 'none' else None
        psi = float(parts[2]) if parts[2].upper().lower() != 'none' else None
 
        converted_coords = [second_struc(phi, psi)]

        converted_line = ' '.join([residue_name] + converted_coords)
        
        convert_coords.append(converted_line)

    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(convert_coords))

input_file_path = r"C:\Users\Tania\Documents\rad_2_deg.txt"
output_file_path = r"C:\Users\Tania\Documents\4n6n_sec_struc.txt"
convert_degs_to_sec(input_file_path, output_file_path)
