import streamlit as st
import pandas as pd

formatted_text = st.markdown('<h1 style="color: pink; border-bottom: 2px solid lightpink;">Einheiten Umrechnen</h1>', unsafe_allow_html=True)
def main():
    import streamlit as st

def main():
    st.title('Einheiten Umrechner')

    category = st.sidebar.selectbox('Wähle Kategorie:', ['Chemie', 'Physik', 'Mathematik'])

    if category == 'Chemie':
        unit_conversion_chemistry()
    elif category == 'Physik':
        unit_conversion_physics()
    elif category == 'Mathematik':
        unit_conversion_mathematics()

def unit_conversion_chemistry():
    st.header('Chemie Einheiten Umrechner')

    input_unit = st.selectbox('Wähle Eingabeeinheit:', ['Mol', 'Liter', 'Gramm'])
    input_value = st.number_input(f'Gib den Wert in {input_unit} ein:')

    unit_factors = {
        'Mol': 1,
        'Liter': 1,
        'Gramm': 1
    }

    output_unit = st.selectbox('Wähle Ziel Einheit:', ['Mol', 'Liter', 'Gramm'])

    output_value = input_value * (unit_factors[input_unit] / unit_factors[output_unit])

    st.write(f'Das Ergebnis ist {output_value} {output_unit}.')

def unit_conversion_physics():
    st.header('Physik Einheiten Umrechner')

    input_unit = st.selectbox('Wähle Eingabeeinheit:', ['Meter', 'Kilogramm', 'Newton'])
    input_value = st.number_input(f'Gib den Wert in {input_unit} ein:')

    unit_factors = {
        'Meter': 1,
        'Kilogramm': 1,
        'Newton': 1
    }

    output_unit = st.selectbox('Wähle Ziel Einheit:', ['Meter', 'Kilogramm', 'Newton'])

    output_value = input_value * (unit_factors[input_unit] / unit_factors[output_unit])

    st.write(f'Das Ergebnis ist {output_value} {output_unit}.')

def unit_conversion_mathematics():
    st.header('Mathematik Einheiten Umrechner')

    input_unit = st.selectbox('Wähle Eingabeeinheit:', ['Meter', 'Quadratmeter', 'Kubikmeter'])
    input_value = st.number_input(f'Gib den Wert in {input_unit} ein:')

    unit_factors = {
        'Meter': 1,
        'Quadratmeter': 1,
        'Kubikmeter': 1
    }

    output_unit = st.selectbox('Wähle Ziel Einheit:', ['Meter', 'Quadratmeter', 'Kubikmeter'])

    output_value = input_value * (unit_factors[input_unit] / unit_factors[output_unit])

    st.write(f'Das Ergebnis ist {output_value} {output_unit}.')

if __name__ == '__main__':
    main()


   








