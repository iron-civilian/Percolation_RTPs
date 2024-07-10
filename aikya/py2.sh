#!/bin/bash

# List of commands to run (replace with your commands)
commands=(
	"python3 rtps1.py 10 0.15 0.0232 0.5"
	"python3 rtps1.py 10 0.15 0.0233 0.5"
	"python3 rtps1.py 10 0.15 0.0234 0.5"
	"python3 rtps1.py 10 0.15 0.0235 0.5"
	"python3 rtps1.py 10 0.15 0.0236 0.5"
	"python3 rtps1.py 10 0.15 0.0237 0.5"
	"python3 rtps1.py 10 0.15 0.0238 0.5"
	"python3 rtps1.py 16 0.15 0.0232 0.5"
	"python3 rtps1.py 16 0.15 0.0233 0.5"
	"python3 rtps1.py 16 0.15 0.0234 0.5"
	"python3 rtps1.py 16 0.15 0.0235 0.5"
	"python3 rtps1.py 16 0.15 0.0236 0.5"
	"python3 rtps1.py 16 0.15 0.0237 0.5"
	"python3 rtps1.py 16 0.15 0.0238 0.5"
	"python3 rtps1.py 20 0.15 0.0232 0.5"
	"python3 rtps1.py 20 0.15 0.0233 0.5"
	"python3 rtps1.py 20 0.15 0.0234 0.5"
	"python3 rtps1.py 20 0.15 0.0235 0.5"
	"python3 rtps1.py 20 0.15 0.0236 0.5"
	"python3 rtps1.py 20 0.15 0.0237 0.5"
	"python3 rtps1.py 20 0.15 0.0238 0.5"
	"python3 rtps1.py 32 0.15 0.0232 0.5"
	"python3 rtps1.py 32 0.15 0.0233 0.5"
	"python3 rtps1.py 32 0.15 0.0234 0.5"
	"python3 rtps1.py 32 0.15 0.0235 0.5"
	"python3 rtps1.py 32 0.15 0.0236 0.5"
	"python3 rtps1.py 32 0.15 0.0237 0.5"
	"python3 rtps1.py 32 0.15 0.0238 0.5"
	"python3 rtps1.py 50 0.15 0.0232 0.5"
	"python3 rtps1.py 50 0.15 0.0233 0.5"
	"python3 rtps1.py 50 0.15 0.0234 0.5"
	"python3 rtps1.py 50 0.15 0.0235 0.5"
	"python3 rtps1.py 50 0.15 0.0236 0.5"
	"python3 rtps1.py 50 0.15 0.0237 0.5"
	"python3 rtps1.py 50 0.15 0.0238 0.5"
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

