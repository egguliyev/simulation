import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
sigma = 8
def simulate_pileup(energies, count_rates, dead_time, simulation_time):
     # Convert count rates to probabilities
    probabilities = count_rates / count_rates.sum()
    # Average interval between photons
    average_interval =  5e-7
    # Initialize time and energy list
    time = 0
    simulated_energies = []

    # Start simulation
    while time < simulation_time:
        # Determine the time to the next photon event
        time_to_next = np.random.exponential(average_interval)
        time += time_to_next

        if time >= simulation_time:
            break

        # If the time to next photon is less than the detector dead time, we have pile-up
        if time_to_next < dead_time:
            # Simulate the energies of the two photons arriving at the same time
            energy1 = np.random.choice(energies, p=probabilities)
            energy2 = np.random.choice(energies, p=probabilities)
            # Sum the energies due to pile-up and store it
            piled_up_energy = energy1 + energy2
            simulated_energies.append(piled_up_energy)
        else:
            # No pile-up, store the energy of the single photon
            energy = np.random.choice(energies, p=probabilities)
            simulated_energies.append(energy)

    # Create histogram of simulated energies to get the new count rates
    simulated_energies = np.array(simulated_energies)
    new_energies, new_counts = np.unique(simulated_energies, return_counts=True)

    # Return the new energies and count rates
    return new_energies, new_counts


# Parameters for the simulation
dead_time = 16e-7  #seconds
simulation_time = 1  #seconds

energies = np.array([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
    59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
    78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
    97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
    112, 113, 114, 115, 116, 117, 118, 119, 120
])

# Constructing the numpy array for Count as provided


count_rates = np.array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 19.14396887, 69.41634241, 176.5727626, 355.4287938,
    837.8412451, 1498.342412, 3051.081712, 4935.844358, 6410.568093, 8119.953307, 9938.319066,
    11951.68872, 14158.36576, 16522.80156, 18566.22568, 20537.89883, 22151.43969, 23766.84825,
    25109.72763, 26486.07004, 27339.76654, 28170.7393, 28764.04669, 29358.91051, 29601.71206,
    29760.31128, 29759.22179, 29716.73152, 29622.56809, 29529.64981, 29226.61479, 28896.18677,
    28536.49805, 28198.44358, 27712.68482, 27171.51751, 26826.45914, 26474.0856, 25789.41634,
    25095.71984, 24534.78599, 23959.22179, 23390.97276, 22812.14008, 22407.47082, 21998.75486,
    29693.85214, 37430.03891, 43957.50973, 50468.94942, 36000.15564, 21430.97276, 19364.35798,
    17280, 16776.03113, 16220.70039, 21091.82879, 25972.29572, 21217.43191, 16336.80934,
    13871.43969, 11408.37354, 10873.6965, 10296.01556, 10115.1751, 9962.474708, 9654.412451,
    9302.63035, 9073.027237, 8716.762646, 8473.307393, 8081.649805, 8024.980545, 7740.171206,
    7434.92607, 7127.22179, 6960.529183, 6798.085603, 6503.439689, 6206.241245, 5970.101167,
    5727.579767, 5471.486381, 5193.805447, 4972.933852, 4753.354086, 4576.326848, 4401.463035,
    4186.490272, 3971.40856, 3790.941634, 3603.782101, 3391.019455, 3150.770428, 2959.657588,
    2771.984436, 2551.315175, 2335.237354, 2147.642023, 1948.871595, 1743.11284, 1543.559533,
    1394.140078, 1257.403891, 1055.649805, 837.7120623, 675.629572, 507.444358, 341.9315175
])

count_rates = gaussian_filter1d(count_rates,sigma)

# Simulate the pile-up
new_energies, new_counts = simulate_pileup(energies, count_rates, dead_time, simulation_time)

# Plot the original and new spectra
plt.figure(figsize=(10, 5))

# Original spectrum
# plt.subplot(1, 1, 1)
# plt.plot(energies, count_rates, 'k.')
# plt.title("Original Spectrum")
# plt.xlabel("Energy (keV)")
# plt.ylabel("Counts")

# Simulated spectrum with pile-up
plt.subplot(1, 1, 1)
plt.plot(new_energies, new_counts, 'k.--')
plt.title("Simulated Spectrum with Pile-Up")
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")

plt.tight_layout()
plt.show()
