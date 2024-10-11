#!/bin/bash

# Check if the venv directory exists
if [ -d "venv" ]; then
    echo "The virtual environment already exists"
    echo "Do you want to recreate the virtual environment? (yes/no) Note: this will remove the current virtual environment directory"
    read recreate

    if [ "$recreate" = "yes" ]; then
        echo "Removing the virtual environment"
        rm -rf venv
    else
        echo "Exiting..."
        exit 0
    fi
fi

declare -A START_VIR_ENVS
START_VIR_ENVS=(
    ["cmd"]=".\\venv\\Scripts\\activate"
    ["powershell"]=".\\venv\\Scripts\\Activate"
    ["bash"]="source venv/bin/activate"
    ["zsh"]="source venv/bin/activate"
    ["git-bash"]="source venv/Scripts/activate"
)

# Specify the allowed terminals
ALLOWED_TERMINALS=("bash" "zsh" "cmd" "powershell", "git-bash")

# Ask the user about their current terminal
echo "What is your current terminal? (${ALLOWED_TERMINALS[@]})"
read terminal

# Convert the terminal to lowercase and trim whitespaces
terminal=$(echo "$terminal" | tr '[:upper:]' '[:lower:]' | xargs)

# Check if the terminal is allowed
if [[ ! " ${ALLOWED_TERMINALS[@]} " =~ " ${terminal} " ]]; then
    echo "The terminal $terminal is not allowed"
    echo "Allowed terminals are: ${ALLOWED_TERMINALS[@]}"
    exit 1
fi

echo "Creating virtual environment"
python -m venv venv

echo "Activating virtual environment"
eval "${START_VIR_ENVS[$terminal]}"

echo "Installing dependencies"
pip install -r requirements.txt
pip install -e .
