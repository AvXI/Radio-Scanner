import time
import rtl_sdr

# Define the frequency range to scan
start_freq = 100e6
stop_freq = 200e6
step_freq = 1e6

# Define the threshold for detecting a signal
threshold = 1000

# Define the sampling rate and gain for the RTL-SDR device
sampling_rate = 2.4e6
gain = 20

# Open the RTL-SDR device
sdr = rtl_sdr.RtlSdr()

# Configure the RTL-SDR device
sdr.sample_rate = sampling_rate
sdr.gain = gain

# Define a function to scan a given frequency
def scan_frequency(freq):
    # Tune to the specified frequency
    sdr.center_freq = freq

    # Read a small amount of data to warm up the device
    sdr.read_samples(1024)

    # Start scanning
    samples = sdr.read_samples(int(sampling_rate))
    peak = max(samples)
    if peak > threshold:
        print(f'Detected signal at {freq / 1e6:.2f} MHz')

# Scan the frequency range
for freq in range(int(start_freq), int(stop_freq), int(step_freq)):
    scan_frequency(freq)

# Close the RTL-SDR device
sdr.close()