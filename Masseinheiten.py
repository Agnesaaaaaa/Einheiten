import streamlit as st
import pandas as pd

formatted_text = st.markdown('<h1 style="color: blue; border-bottom: 2px solid lightpink;">Masseinheiten</h1>', unsafe_allow_html=True)
def main():
    st.title('Einheiten Umrechner')

    # Eingabefeld für Benutzer
    input_unit = st.selectbox('Wähle Eingabeeinheit:', ['Meter', 'Kilometer', 'Liter', 'Gramm'])

    # Umrechnungsfaktoren
    unit_factors = {
        'Meter': 1,
        'Kilometer': 1000,
        'Liter': 1,
        'Gramm': 1
    }

 
    input_value = st.number_input(f'Gib den Wert in {input_unit} ein:')


    output_unit = st.selectbox('Wähle Ziel Einheit:', ['Meter', 'Kilometer', 'Liter', 'Gramm'])

    
    output_value = input_value * (unit_factors[input_unit] / unit_factors[output_unit])

    
    st.write(f'Das Ergebnis ist {output_value} {output_unit}.')

if __name__ == '__main__':
    main()







