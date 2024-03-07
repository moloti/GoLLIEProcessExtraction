#!/bin/bash

ROOT_DIR=$(pwd)
# The directory to check
DIRECTORY="${ROOT_DIR}/results/GoLLIE+-34b_CodeLLaMA"

check_directory() {
    if [ -d "$DIRECTORY" ]; then
        echo "Directory exists: $DIRECTORY"
        
        # Checking write permission
        if [ -w "$DIRECTORY" ]; then
            echo "Write permission is granted on $DIRECTORY"
        else
            echo "Error: Write permission is denied on $DIRECTORY"
            exit 1
        fi
        
        # Checking read permission
        if [ -r "$DIRECTORY" ]; then
            echo "Read permission is granted on $DIRECTORY"
        else
            echo "Error: Read permission is denied on $DIRECTORY"
            exit 1
        fi
        
        # Checking execute permission
        if [ -x "$DIRECTORY" ]; then
            echo "Execute permission is granted on $DIRECTORY"
            return 0
        else
            echo "Error: Execute permission is denied on $DIRECTORY"
            exit 1
        fi
    else
        echo "Error: Directory does not exist: $DIRECTORY"
        exit 1
    fi
}

check_directory