#!/bin/bash

# List of commands to run (replace with your commands)
commands=(
	"python3 rtps.py 20 0.15 0.002 0.5"
	"python3 rtps.py 20 0.15 0.004 0.5"
	"python3 rtps.py 20 0.15 0.006 0.5"
	"python3 rtps.py 20 0.15 0.008 0.5"
	"python3 rtps.py 20 0.15 0.010 0.5"
	"python3 rtps.py 20 0.15 0.012 0.5"
	"python3 rtps.py 20 0.15 0.014 0.5"
	"python3 rtps.py 20 0.15 0.016 0.5"
	"python3 rtps.py 20 0.15 0.018 0.5"
	"python3 rtps.py 20 0.15 0.020 0.5"
	"python3 rtps.py 20 0.15 0.022 0.5"
	"python3 rtps.py 20 0.15 0.024 0.5"
	"python3 rtps.py 20 0.15 0.026 0.5"
	"python3 rtps.py 20 0.15 0.028 0.5"
	"python3 rtps.py 20 0.15 0.030 0.5"
	"python3 rtps.py 20 0.15 0.032 0.5"
	"python3 rtps.py 20 0.15 0.034 0.5"
	"python3 rtps.py 20 0.15 0.036 0.5"
	"python3 rtps.py 20 0.15 0.038 0.5"
	"python3 rtps.py 20 0.15 0.040 0.5"
 )

# Function to run a command in the background
run_command() {
    local cmd="$1"
    eval "$cmd"
    echo "$cmd is done"
}

# Number of CPU cores available
cores=15

# Maximum number of concurrent commands
max_concurrent=15  # Adjust this as needed

# Loop through the commands
for cmd in "${commands[@]}"; do
    # Check the number of background processes
    while [[ $(jobs -p | wc -l) -ge $max_concurrent ]]; do
        sleep 1  # Wait for a slot to open up
    done

    # Run the command in the background
    run_command "$cmd" &
done

# Wait for all background processes to finish
wait

echo "All commands are done"

