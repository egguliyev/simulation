import time
import random
import numpy as np
import matplotlib.pyplot as plt

def simulate_event():
    """Simulate an event with a random time of occurrence."""
    return random.uniform(0, 1)  # Random time between 0 and 1 second


def is_coincident(event1_time, event2_time, twindow):
    """
    Determine if two events are coincident.

    :param event1_time: Time of event in pixel 1
    :param event2_time: Time of event in pixel 2
    :param twindow: Defined time window for coincidence
    :return: True if events are coincident, False otherwise
    """
    return abs(event1_time - event2_time) <= twindow


# Define the timing window (Twindow) in seconds
twindow = 0.5  #Twindow described in T DS

# Simulate events in two adjacent pixels
event1_time = simulate_event()
time.sleep(0.05)  # Simulate a short delay between events
event2_time = simulate_event()

# Check if the events are coincident
coincident = is_coincident(event1_time, event2_time, twindow)

# Function to generate random events over time for a pixel
def generate_events(duration, frequency):
    """
    Generate random event times for a pixel.

    :param duration: Total duration to simulate
    :param frequency: Average number of events per second
    :return: Array of event times
    """
    num_events = int(duration * frequency)
    return np.sort(np.random.uniform(0, duration, num_events))


# Simulation parameters
duration = 10  # Total time duration of 10 seconds
frequency = 0.5  # Average number of events per second for each pixel

# Generate events for two pixels
events_pixel1 = generate_events(duration, frequency)
events_pixel2 = generate_events(duration, frequency)

# Determine coincidences
coincidences = []
for event1 in events_pixel1:
    for event2 in events_pixel2:
        if is_coincident(event1, event2, twindow):
            coincidences.append((event1, event2))

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(10, 8))

# Plot events for Pixel 1
axs[0].eventplot(events_pixel1, color='blue')
axs[0].set_title('Events in Pixel 1')
axs[0].set_ylabel('Event Number')
axs[0].set_xlim(0, duration)

# Plot events for Pixel 2
axs[1].eventplot(events_pixel2, color='green')
axs[1].set_title('Events in Pixel 2')
axs[1].set_ylabel('Event Number')
axs[1].set_xlim(0, duration)

# Plot coincidences
for event1, event2 in coincidences:
    axs[2].plot([event1], [1], 'sr')
axs[2].set_title('Coincidences between Pixels')
axs[2].set_xlabel('Time (s)')
axs[2].set_xlim(0, duration)

plt.tight_layout()
plt.show()
