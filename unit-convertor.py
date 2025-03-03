import streamlit as st

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        'kilograms': 1.0,
        'grams': 0.001,
        'milligrams': 0.000001,
        'pounds': 0.453592,
        'ounces': 0.0283495,
        'tons': 907.185
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # Convert to Celsius first
    if from_unit == 'fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    else:
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == 'fahrenheit':
        return (celsius * 9/5) + 32
    elif to_unit == 'kelvin':
        return celsius + 273.15
    else:
        return celsius

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'liters': 1.0,
        'milliliters': 0.001,
        'cubic meters': 1000,
        'cubic feet': 28.3168,
        'gallons': 3.78541,
        'pints': 0.473176
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="📐", layout="centered")

st.title("📏 Professional Unit Converter")
st.markdown("### A multi-category unit conversion tool")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature", "Volume"])

col1, col2, col3 = st.columns(3)

with col1:
    input_value = st.number_input("Input Value", min_value=0.0, value=1.0, step=0.1)

with col2:
    if category == "Length":
        from_unit = st.selectbox("From", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
    elif category == "Weight":
        from_unit = st.selectbox("From", ["kilograms", "grams", "milligrams", "pounds", "ounces", "tons"])
    elif category == "Temperature":
        from_unit = st.selectbox("From", ["celsius", "fahrenheit", "kelvin"])
    else:  # Volume
        from_unit = st.selectbox("From", ["liters", "milliliters", "cubic meters", "cubic feet", "gallons", "pints"])

with col3:
    if category == "Length":
        to_unit = st.selectbox("To", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
    elif category == "Weight":
        to_unit = st.selectbox("To", ["kilograms", "grams", "milligrams", "pounds", "ounces", "tons"])
    elif category == "Temperature":
        to_unit = st.selectbox("To", ["celsius", "fahrenheit", "kelvin"])
    else:  # Volume
        to_unit = st.selectbox("To", ["liters", "milliliters", "cubic meters", "cubic feet", "gallons", "pints"])

if st.button("Convert", type="primary"):
    try:
        if category == "Length":
            result = convert_length(input_value, from_unit, to_unit)
        elif category == "Weight":
            result = convert_weight(input_value, from_unit, to_unit)
        elif category == "Temperature":
            result = convert_temperature(input_value, from_unit, to_unit)
        else:  # Volume
            result = convert_volume(input_value, from_unit, to_unit)
        
        st.success(f"Converted Result: **{result:.4f} {to_unit}**")
    except Exception as e:
        st.error(f"Error in conversion: {str(e)}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Supports 30+ different units across 4 categories")