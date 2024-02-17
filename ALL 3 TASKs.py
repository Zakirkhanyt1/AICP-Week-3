# Initializing an empty dictionary to store cow yields                             #TASK NO 1
cow_yields = {}

# Function to record milk yield for a cow
def record_yield():
    cow_code = input("Enter the 3-digit identity code of the cow: ")

    # Validating the input for a 3-digit identity code
    while not cow_code.isdigit() or len(cow_code) != 3:
        print("Invalid input. Please enter a 3-digit identity code.")
        cow_code = input("Enter the 3-digit identity code of the cow: ")

    # Checking if the cow has been recorded before
    if cow_code not in cow_yields:
        cow_yields[cow_code] = []

    # Recording the yield for the cow
    yield_value = float(input(f"Enter the yield for cow {cow_code} in liters: "))

    # Validating the input for a positive yield
    while yield_value < 0:
        print("Invalid input. Please enter a positive yield value.")
        yield_value = float(input(f"Enter the yield for cow {cow_code} in liters: "))

    # Appending the yield to the cow's record
    cow_yields[cow_code].append(yield_value)

# Loop to record yields for the week
for day in range(1,3):
    print(f"\nDay {day}:")
    while True:
        record_yield()
        more_entries = input("Do you want to record more yields for today? (yes/no): ").lower()
        if more_entries != 'yes':
            break

# Printing the recorded yields
print("\nRecorded Cow Yields:")
for cow_code, yields in cow_yields.items():
    print(f"Cow {cow_code}: {yields}")

# Function to calculate total and average yields for the herd
def calculate_statistics():                                                #TASK NO 2
    total_volume = 0
    total_cows = len(cow_yields)

    # Calculate total volume and display individual cow averages
    for cow_code, yields in cow_yields.items():
        total_volume += sum(yields)
        average_yield = sum(yields) / len(yields)
        print(f"Average yield for cow {cow_code}: {average_yield:.1f} liters")

    # Calculate and display total weekly volume and average yield per cow for the herd
    print("\nHerd Statistics:")
    print(f"Total Weekly Volume: {total_volume:.0f} liters")
    print(f"Average Yield per Cow: {total_volume / total_cows:.0f} liters")

# Call the function to calculate and display statistics
calculate_statistics()
                                                                                   #TASK NO 3
# Function to identify the most productive cow and cows with low milk volume
def identify_cows():
    most_productive_cow = max(cow_yields, key=lambda x: sum(cow_yields[x]))
    most_productive_yield = sum(cow_yields[most_productive_cow])

    low_yield_cows = [cow_code for cow_code, yields in cow_yields.items() if sum(yields) < 12 * 4]

    # Displaying the results
    print("\nIdentification Results:")
    print(f"Most Productive Cow - Cow {most_productive_cow}: {most_productive_yield:.0f} liters")
    if low_yield_cows:
        print("Cows with Low Milk Volume:")
        for cow_code in low_yield_cows:
            print(f"Cow {cow_code}")

# Call the function to identify and display cows
identify_cows()




