import streamlit as st

def price(base_fare, modifier, fixed_fee, tax_rate):
    return base_fare + (base_fare * modifier) + fixed_fee + (base_fare * tax_rate)

# Pricing tables for different Uber services
pricing_tables = {
    'UBER X & Green & Comfort & WAV': [
        (1, 0.6, 0.6, 0.70, 3, 0.10),
        (2, 0.6, 0.5, 0.40, 3, 0.10),
        (3, 0.7, 0.7, 0.50, 3, 0.10),
        (4, 0.5, 0.5, 0.45, 3, 0.10),
        (5, 0.5, 0.8, 0.40, 3, 0.10),
        (6, 0.5, 0.5, 0.05, 3, 0.10),
        (7, 0.5, 0.8, 0.25, 3, 0.10),
        (8, 0.5, 0.6, 1.05, 3, 0.10),
        (9, 0.6, 0.8, 0.45, 3, 0.10),
        (10, 0.6, 0.8, 0.35, 3, 0.10),
        (11, 0.6, 0.8, 0.05, 3, 0.10),
        (15, 0.6, 0.8, 0.30, 3, 0.10),
        (16, 0.2, 0.5, 0.10, 3, 0.10),
        (20, 0.6, 0.8, 0.20, 3, 0.10),
        (25, 0.6, 0.8, 0.10, 3, 0.10),
        (40, 0.2, 0.5, 0.10, 3, 0.10)
    ],
    'UBER XL': [
        (1, 1, 1, 0.70, 4, 0.10),
        (2, 0.6, 0.5, 0.70, 4, 0.10),
        (3, 0.5, 0.5, 0.65, 4, 0.10),
        (4, 0.5, 0.5, 0.75, 4, 0.10),
        (5, 0.5, 0.8, 0.40, 4, 0.10),
        (6, 0.6, 0.5, 0.25, 4, 0.10),
        (7, 0.5, 0.8, 0.25, 4, 0.10),
        (8, 0.6, 0.7, 1.00, 4, 0.10),
        (9, 0.6, 0.8, 0.45, 4, 0.10),
        (10, 0.6, 0.8, 0.60, 4, 0.10),
        (11, 0.6, 0.8, 0.05, 4, 0.10),
        (15, 0.6, 0.8, 0.30, 4, 0.10),
        (16, 0.5, 0.5, 0.15, 4, 0.10),
        (20, 0.6, 0.8, 0.20, 4, 0.10),
        (25, 0.5, 0.5, 0.10, 4, 0.10),
        (40, 0.2, 0.5, 0.10, 4, 0.10),
        (50, 0.7, 1, 0.10, 10, 0.10)
    ],
    'UBER Black or Premier': [
        (1, 1.6, 1, 0.70, 10, 0.10),
        (2, 0.6, 0.5, 1.00, 10, 0.10),
        (3, 0.5, 0.5, 0.80, 10, 0.10),
        (4, 0.5, 0.5, 0.75, 10, 0.10),
        (5, 0.5, 0.8, 0.40, 10, 0.10),
        (6, 0.5, 0.5, 0.50, 10, 0.10),
        (7, 0.5, 0.8, 0.70, 10, 0.10),
        (8, 0.7, 0.2, 1.50, 10, 0.10),
        (9, 0.6, 0.8, 0.45, 10, 0.10),
        (10, 0.6, 0.8, 0.85, 10, 0.10),
        (11, 0.6, 0.8, 0.05, 10, 0.10),
        (15, 0.6, 0.8, 0.30, 10, 0.10),
        (16, 0.5, 0.5, 0.30, 10, 0.10),
        (20, 0.6, 0.8, 0.20, 10, 0.10),
        (25, 0.55, 1, 0.10, 10, 0.10),
        (40, 0.2, 1, 0.10, 10, 0.10),
        (50, 0.7, 1, 0.10, 10, 0.10)
    ]
}

def calculate_fare(service_type, minutes, miles):
    table = pricing_tables.get(service_type)
    if not table:
        return "Invalid service type"

    for max_mile, distance_factor, minute_rate, additional_pct, fixed_fee, sales_tax_pct in table:
        if miles <= max_mile:
            base_fare = (distance_factor * miles) + (minute_rate * minutes)
            return price(base_fare, additional_pct, fixed_fee, sales_tax_pct)

    # Use the last pricing tier if distance exceeds the maximum
    max_mile, distance_factor, minute_rate, additional_pct, fixed_fee, sales_tax_pct = table[-1]
    base_fare = (distance_factor * miles) + (minute_rate * minutes)
    return price(base_fare, additional_pct, fixed_fee, sales_tax_pct)

st.title('Uber Fare Calculator')

mins = st.number_input('Enter Minutes:', min_value=0.0, step=0.1)
miles = st.number_input('Enter Miles:', min_value=0.0, step=0.1)

ride_types = ['UBER X & Green & Comfort & WAV', 'UBER XL', 'UBER Black or Premier']

if st.button('Calculate Fare'):
    fare_x = calculate_fare('UBER X & Green & Comfort & WAV', mins, miles)
    fare_XL = calculate_fare('UBER XL', mins, miles)
    fare_Black = calculate_fare('UBER Black or Premier', mins, miles)
    st.write(f'The fare for UBER X & Green & Comfort & WAV is: ${fare_x}')
    st.write(f'The fare for UBER XL is: ${fare_XL}')
    st.write(f'The fare for UBER Black or Premier is: ${fare_Black}')
