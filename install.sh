
# Specify the allowed terminals
ALLOWED_TERMINALS=("bash" "zsh" "cmd" "powershell")

# Ask the user about their current terminal
echo "What is your current terminal? ${ALLOWED_TERMINALS[@]})"
read terminal

# Convert the terminal to lowercase
terminal=$(echo $terminal | tr '[:upper:]' '[:lower:]')

# Check if the terminal is allowed
if [[ ! " ${ALLOWED_TERMINALS[@]} " =~ " ${terminal} " ]]; then
    echo "The terminal $terminal is not allowed"
    echo "Allowed terminals are: ${ALLOWED_TERMINALS[@]}"
    exit 1
fi

# Check if the terminal is cmd
if [ $terminal = "cmd" ]; then
    echo "You are using cmd"
fi

# Check if the terminal is powershell
if [ $terminal = "powershell" ]; then
    echo "You are using powershell"
fi

# Check if the terminal is bash or zsh
if [ $terminal = "bash" ] || [ $terminal = "zsh" ]; then
    echo "You are using bash or zsh"
fi