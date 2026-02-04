# Write Python code to read previous units, current units, and customer type, then calculate units consumed
# and the total bill based on the given rates.
def calculate_electricity_bill():
    previous_units = int(input("Enter previous meter reading (in units): "))
    current_units = int(input("Enter current meter reading (in units): "))
    customer_type = input("Enter customer type (residential/commercial): ").strip().lower()

    units_consumed = current_units - previous_units
    if units_consumed < 0:
        print("Error: Current units must be greater than or equal to previous units.")
        return

    if customer_type == 'residential':
        if units_consumed <= 100:
            rate = 0.5
        elif units_consumed <= 300:
            rate = 0.75
        else:
            rate = 1.0
    elif customer_type == 'commercial':
        if units_consumed <= 100:
            rate = 0.75
        elif units_consumed <= 300:
            rate = 1.0
        else:
            rate = 1.5
    else:
        print("Error: Invalid customer type. Please enter 'residential' or 'commercial'.")
        return

    total_bill = units_consumed * rate
    print(f"Units Consumed: {units_consumed} units")
    print(f"Total Bill: ${total_bill:.2f}")
if __name__ == "__main__":
    calculate_electricity_bill()

#task2
# Add if-else logic to calculate energy charges for domestic, commercial, and industrial users
def calculate_energy_charges():
    previous_units = int(input("Enter previous meter reading (in units): "))
    current_units = int(input("Enter current meter reading (in units): "))
    customer_type = input("Enter customer type (domestic/commercial/industrial): ").strip().lower()

    units_consumed = current_units - previous_units
    if units_consumed < 0:
        print("Error: Current units must be greater than or equal to previous units.")
        return

    if customer_type == 'domestic':
        if units_consumed <= 100:
            rate = 0.6
        elif units_consumed <= 300:
            rate = 0.8
        else:
            rate = 1.2
    elif customer_type == 'commercial':
        if units_consumed <= 100:
            rate = 0.9
        elif units_consumed <= 300:
            rate = 1.2
        else:
            rate = 1.8
    elif customer_type == 'industrial':
        if units_consumed <= 100:
            rate = 1.0
        elif units_consumed <= 300:
            rate = 1.5
        else:
            rate = 2.0
    else:
        print("Error: Invalid customer type. Please enter 'domestic', 'commercial', or 'industrial'.")
        return

    total_bill = units_consumed * rate
    print(f"Units Consumed: {units_consumed} units")
    print(f"Total Bill: ${total_bill:.2f}")
if __name__ == "__main__":
    calculate_energy_charges()

# Optimize tariff calculation using conditional statements
def optimized_tariff_calculation():
    previous_units = int(input("Enter previous meter reading (in units): "))
    current_units = int(input("Enter current meter reading (in units): "))
    customer_type = input("Enter customer type (residential/commercial/industrial): ").strip().lower()

    units_consumed = current_units - previous_units
    if units_consumed < 0:
        print("Error: Current units must be greater than or equal to previous units.")
        return

    rates = {
        'residential': [(100, 0.5), (300, 0.75), (float('inf'), 1.0)],
        'commercial': [(100, 0.75), (300, 1.0), (float('inf'), 1.5)],
        'industrial': [(100, 1.0), (300, 1.5), (float('inf'), 2.0)]
    }

    if customer_type not in rates:
        print("Error: Invalid customer type. Please enter 'residential', 'commercial', or 'industrial'.")
        return

    for limit, rate in rates[customer_type]:
        if units_consumed <= limit:
            total_bill = units_consumed * rate
            break

    print(f"Units Consumed: {units_consumed} units")
    print(f"Total Bill: ${total_bill:.2f}")
if __name__ == "__main__":
    optimized_tariff_calculation()
    
#task3
# Create Python functions to calculate energy charges and fixed charges
def calculate_energy_and_fixed_charges():
    previous_units = int(input("Enter previous meter reading (in units): "))
    current_units = int(input("Enter current meter reading (in units): "))
    customer_type = input("Enter customer type (residential/commercial/industrial): ").strip().lower()

    units_consumed = current_units - previous_units
    if units_consumed < 0:
        print("Error: Current units must be greater than or equal to previous units.")
        return

    energy_rates = {
        'residential': [(100, 0.5), (300, 0.75), (float('inf'), 1.0)],
        'commercial': [(100, 0.75), (300, 1.0), (float('inf'), 1.5)],
        'industrial': [(100, 1.0), (300, 1.5), (float('inf'), 2.0)]
    }

    fixed_charges = {
        'residential': 50,
        'commercial': 100,
        'industrial': 150
    }

    if customer_type not in energy_rates or customer_type not in fixed_charges:
        print("Error: Invalid customer type. Please enter 'residential', 'commercial', or 'industrial'.")
        return

    for limit, rate in energy_rates[customer_type]:
        if units_consumed <= limit:
            energy_charge = units_consumed * rate
            break

    total_bill = energy_charge + fixed_charges[customer_type]

    print(f"Units Consumed: {units_consumed} units")
    print(f"Energy Charge: ${energy_charge:.2f}")
    print(f"Fixed Charge: ${fixed_charges[customer_type]:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
if __name__ == "__main__":
    calculate_energy_and_fixed_charges()

# Write reusable billing functions with comments
def calculate_energy_and_fixed_charges():
    """
    Calculate the energy charges and fixed charges based on customer type and units consumed.
    """
    previous_units = int(input("Enter previous meter reading (in units): "))
    current_units = int(input("Enter current meter reading (in units): "))
    customer_type = input("Enter customer type (residential/commercial/industrial): ").strip().lower()

    units_consumed = current_units - previous_units
    if units_consumed < 0:
        print("Error: Current units must be greater than or equal to previous units.")
        return

    energy_rates = {
        'residential': [(100, 0.5), (300, 0.75), (float('inf'), 1.0)],
        'commercial': [(100, 0.75), (300, 1.0), (float('inf'), 1.5)],
        'industrial': [(100, 1.0), (300, 1.5), (float('inf'), 2.0)]
    }

    fixed_charges = {
        'residential': 50,
        'commercial': 100,
        'industrial': 150
    }

    if customer_type not in energy_rates or customer_type not in fixed_charges:
        print("Error: Invalid customer type. Please enter 'residential', 'commercial', or 'industrial'.")
        return

    for limit, rate in energy_rates[customer_type]:
        if units_consumed <= limit:
            energy_charge = units_consumed * rate
            break

    total_bill = energy_charge + fixed_charges[customer_type]

    print(f"Units Consumed: {units_consumed} units")
    print(f"Energy Charge: ${energy_charge:.2f}")
    print(f"Fixed Charge: ${fixed_charges[customer_type]:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
if __name__ == "__main__":
    calculate_energy_and_fixed_charges()

#task4
# Add fixed charges, customer charges, and electricity duty calculation
def calculate_detailed_electricity_bill():
    previous_units = int(input("Enter previous meter reading (in units): "))
    current_units = int(input("Enter current meter reading (in units): "))
    customer_type = input("Enter customer type (residential/commercial/industrial): ").strip().lower()

    units_consumed = current_units - previous_units
    if units_consumed < 0:
        print("Error: Current units must be greater than or equal to previous units.")
        return

    energy_rates = {
        'residential': [(100, 0.5), (300, 0.75), (float('inf'), 1.0)],
        'commercial': [(100, 0.75), (300, 1.0), (float('inf'), 1.5)],
        'industrial': [(100, 1.0), (300, 1.5), (float('inf'), 2.0)]
    }

    fixed_charges = {
        'residential': 50,
        'commercial': 100,
        'industrial': 150
    }

    customer_charges = {
        'residential': 20,
        'commercial': 40,
        'industrial': 60
    }

    electricity_duty_rate = 0.05  # 5% electricity duty

    if customer_type not in energy_rates or customer_type not in fixed_charges or customer_type not in customer_charges:
        print("Error: Invalid customer type. Please enter 'residential', 'commercial', or 'industrial'.")
        return

    for limit, rate in energy_rates[customer_type]:
        if units_consumed <= limit:
            energy_charge = units_consumed * rate
            break

    fixed_charge = fixed_charges[customer_type]
    customer_charge = customer_charges[customer_type]
    electricity_duty = (energy_charge + fixed_charge + customer_charge) * electricity_duty_rate

    total_bill = energy_charge + fixed_charge + customer_charge + electricity_duty

    print(f"Units Consumed: {units_consumed} units")
    print(f"Energy Charge: ${energy_charge:.2f}")
    print(f"Fixed Charge: ${fixed_charge:.2f}")
    print(f"Customer Charge: ${customer_charge:.2f}")
    print(f"Electricity Duty: ${electricity_duty:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
if __name__ == "__main__":
    calculate_detailed_electricity_bill()

# Improve billing accuracy by including additional charges
def calculate_comprehensive_electricity_bill():
    """
    Calculate a comprehensive electricity bill including energy charges, fixed charges,
    customer charges, and electricity duty based on customer type and units consumed.
    """
    previous_units = int(input("Enter previous meter reading (in units): "))
    current_units = int(input("Enter current meter reading (in units): "))
    customer_type = input("Enter customer type (residential/commercial/industrial): ").strip().lower()

    units_consumed = current_units - previous_units
    if units_consumed < 0:
        print("Error: Current units must be greater than or equal to previous units.")
        return

    energy_rates = {
        'residential': [(100, 0.5), (300, 0.75), (float('inf'), 1.0)],
        'commercial': [(100, 0.75), (300, 1.0), (float('inf'), 1.5)],
        'industrial': [(100, 1.0), (300, 1.5), (float('inf'), 2.0)]
    }

    fixed_charges = {
        'residential': 50,
        'commercial': 100,
        'industrial': 150
    }

    customer_charges = {
        'residential': 20,
        'commercial': 40,
        'industrial': 60
    }

    electricity_duty_rate = 0.05  # 5% electricity duty

    if customer_type not in energy_rates or customer_type not in fixed_charges or customer_type not in customer_charges:
        print("Error: Invalid customer type. Please enter 'residential', 'commercial', or 'industrial'.")
        return

    for limit, rate in energy_rates[customer_type]:
        if units_consumed <= limit:
            energy_charge = units_consumed * rate
            break

    fixed_charge = fixed_charges[customer_type]
    customer_charge = customer_charges[customer_type]
    electricity_duty = (energy_charge + fixed_charge + customer_charge) * electricity_duty_rate

    total_bill = energy_charge + fixed_charge + customer_charge + electricity_duty

    print(f"Units Consumed: {units_consumed} units")
    print(f"Energy Charge: ${energy_charge:.2f}")
    print(f"Fixed Charge: ${fixed_charge:.2f}")
    print(f"Additional Customer Charge: ${customer_charge:.2f}")    
    print(f"Customer Charge: ${customer_charge:.2f}")
    print(f"Electricity Duty: ${electricity_duty:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
if __name__ == "__main__":
    calculate_comprehensive_electricity_bill()

#task5
# Generate formatted electricity bill output with total amount
def generate_electricity_bill():
    previous_units = int(input("Enter previous meter reading (in units): "))
    current_units = int(input("Enter current meter reading (in units): "))
    customer_type = input("Enter customer type (residential/commercial/industrial): ").strip().lower()

    units_consumed = current_units - previous_units
    if units_consumed < 0:
        print("Error: Current units must be greater than or equal to previous units.")
        return

    energy_rates = {
        'residential': [(100, 0.5), (300, 0.75), (float('inf'), 1.0)],
        'commercial': [(100, 0.75), (300, 1.0), (float('inf'), 1.5)],
        'industrial': [(100, 1.0), (300, 1.5), (float('inf'), 2.0)]
    }

    fixed_charges = {
        'residential': 50,
        'commercial': 100,
        'industrial': 150
    }

    customer_charges = {
        'residential': 20,
        'commercial': 40,
        'industrial': 60
    }

    electricity_duty_rate = 0.05  # 5% electricity duty

    if customer_type not in energy_rates or customer_type not in fixed_charges or customer_type not in customer_charges:
        print("Error: Invalid customer type. Please enter 'residential', 'commercial', or 'industrial'.")
        return

    for limit, rate in energy_rates[customer_type]:
        if units_consumed <= limit:
            energy_charge = units_consumed * rate
            break

    fixed_charge = fixed_charges[customer_type]
    customer_charge = customer_charges[customer_type]
    electricity_duty = (energy_charge + fixed_charge + customer_charge) * electricity_duty_rate

    total_bill = energy_charge + fixed_charge + customer_charge + electricity_duty

    print("\n----- Electricity Bill -----")
    print(f"Customer Type       : {customer_type.capitalize()}")
    print(f"Previous Reading    : {previous_units} units")
    print(f"Current Reading     : {current_units} units")
    print(f"Units Consumed      : {units_consumed} units")
    print(f"Energy Charge       : ${energy_charge:.2f}")
    print(f"Fixed Charge        : ${fixed_charge:.2f}")
    print(f"Customer Charge     : ${customer_charge:.2f}")
    print(f"Electricity Duty    : ${electricity_duty:.2f}")
    print(f"Total Amount Payable: ${total_bill:.2f}")
    print("----------------------------")
if __name__ == "__main__":
    generate_electricity_bill()
# Display EC, FC, CC, ED, and total bill neatly
def display_detailed_electricity_bill():
    """
    Display a detailed electricity bill including energy charges, fixed charges,
    customer charges, electricity duty, and total amount payable.
    """
    previous_units = int(input("Enter previous meter reading (in units): "))
    current_units = int(input("Enter current meter reading (in units): "))
    customer_type = input("Enter customer type (residential/commercial/industrial): ").strip().lower()

    units_consumed = current_units - previous_units
    if units_consumed < 0:
        print("Error: Current units must be greater than or equal to previous units.")
        return

    energy_rates = {
        'residential': [(100, 0.5), (300, 0.75), (float('inf'), 1.0)],
        'commercial': [(100, 0.75), (300, 1.0), (float('inf'), 1.5)],
        'industrial': [(100, 1.0), (300, 1.5), (float('inf'), 2.0)]
    }

    fixed_charges = {
        'residential': 50,
        'commercial': 100,
        'industrial': 150
    }

    customer_charges = {
        'residential': 20,
        'commercial': 40,
        'industrial': 60
    }

    electricity_duty_rate = 0.05  # 5% electricity duty

    if customer_type not in energy_rates or customer_type not in fixed_charges or customer_type not in customer_charges:
        print("Error: Invalid customer type. Please enter 'residential', 'commercial', or 'industrial'.")
        return

    for limit, rate in energy_rates[customer_type]:
        if units_consumed <= limit:
            energy_charge = units_consumed * rate
            break

    fixed_charge = fixed_charges[customer_type]
    customer_charge = customer_charges[customer_type]
    electricity_duty = (energy_charge + fixed_charge + customer_charge) * electricity_duty_rate

    total_bill = energy_charge + fixed_charge + customer_charge + electricity_duty

    print("\n----- Detailed Electricity Bill -----")
    print(f"Customer Type       : {customer_type.capitalize()}")
    print(f"Previous Reading    : {previous_units} units")
    print(f"Current Reading     : {current_units} units")
    print(f"Units Consumed      : {units_consumed} units")
    print(f"Energy Charge (EC)  : ${energy_charge:.2f}")
    print(f"Fixed Charge (FC)   : ${fixed_charge:.2f}")
    print(f"Customer Charge (CC): ${customer_charge:.2f}")
    print(f"Electricity Duty (ED): ${electricity_duty:.2f}")
    print(f"Total Amount Payable: ${total_bill:.2f}")
    print("-------------------------------------")
if __name__ == "__main__":
    display_detailed_electricity_bill()
    
