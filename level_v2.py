import math

# Input from the user
minutes = float(input("How many minutes have you programmed this year?\n"))

level = 10  # Initial level requirement
rank = 1  # Initial rank

while True:
    # Increase the level by 10% of the current level, rounded up
    level += math.ceil(level / 10)
    
    # Increase the rank for the next iteration
    rank += 1

    # Break the loop if the level requirement exceeds the total minutes programmed or reaches the maximum level
    if level > minutes or level >= 100000000:
        break

# Calculate the final rank
final_rank = rank - 1

# Generate the asterisks representation for the final rank
asterisks = '*' * final_rank

# Print the final status, including the asterisks representation on a new line
if level >= 100000000:
    print(f"You have programmed for {minutes} minutes this year, reaching the maximum level cap at rank {final_rank}.\nLevel display: {asterisks}")
else:
    print(f"You have programmed for {minutes} minutes this year, reaching level {final_rank}.\nLevel display: {asterisks}")
