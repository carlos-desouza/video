import math

# Constants
R = 8.3144621  # Gas constant in J/(mol*K)

def calculate_activation_energy(kcat, temperature):
    # Constants
    h = 6.62607015e-34  # Planck's constant in J*s
    kB = 1.380649e-23  # Boltzmann constant in J/K

    # Calculate the activation energy in Joules
    Ea = -R * temperature * math.log(kcat * h / (kB * temperature))

    return Ea

def convert_joules_to_kjoules(energy_in_joules):
    return energy_in_joules / 1000

def convert_kjoules_to_kcal(energy_in_kjoules):
    return energy_in_kjoules / 4.184

# Example usage
kcat = 111.9
temperature = 313.15  # Example temperature in Kelvin

# Calculate activation energy in Joules
activation_energy_joules = calculate_activation_energy(kcat, temperature)
print("Activation Energy (Ea) in Joules: {:.2f} J/mol".format(activation_energy_joules))

# Convert activation energy from Joules to kilojoules
activation_energy_kjoules = convert_joules_to_kjoules(activation_energy_joules)
print("Activation Energy (Ea) in Kilojoules: {:.2f} kJ/mol".format(activation_energy_kjoules))

# Convert activation energy from kilojoules to kilocalories
activation_energy_kcal = convert_kjoules_to_kcal(activation_energy_kjoules)
print("Activation Energy (Ea) in Kilocalories: {:.2f} kcal/mol".format(activation_energy_kcal))

