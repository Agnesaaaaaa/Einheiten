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

import streamlit as st

def main():
    st.title('Antibiotika Dosierung Rechner')

    weight = st.number_input('Gib das Gewicht des Patienten in kg ein:')

    if weight > 0:
        dosage = calculate_dosage(weight)
        st.write(f'Die empfohlene Dosierung für den Patienten beträgt {dosage} mg pro Tag.')

def calculate_dosage(weight):
    if weight <= 5:
        return '250–500 mg pro Tag (3–4 Dosen zu je 100 mg)'
    elif 6 <= weight <= 7:
        return '350–700 mg pro Tag (4 Dosen zu je 100 mg oder 3 Dosen zu je 200 mg)'
    elif 8 <= weight <= 10:
        return '500–1000 mg pro Tag (3–4 Dosen zu je 200 mg)'
    elif 11 <= weight <= 15:
        return '750–1500 mg pro Tag (4 Dosen zu je 200 mg oder 3 Dosen zu je 400 mg)'
    elif 16 <= weight <= 20:
        return '1000–2000 mg pro Tag (3–4 Dosen zu je 400 mg)'
    elif 21 <= weight <= 25:
        return '1250–2000 mg pro Tag (3–4 Dosen zu je 400 mg)'
    elif 26 <= weight <= 30:
        return '1500–2000 mg pro Tag (4 Dosen zu je 400 mg)'
    elif 31 <= weight <= 40:
        return '2000 mg pro Tag (4 Dosen zu je 400 mg)'
    else:
        return 'Keine Dosierungsinformationen verfügbar für das angegebene Gewicht.'

if __name__ == '__main__':
    main()

import streamlit as st

def main():
    st.title('Einheiten Umrechner')

    category = st.sidebar.selectbox('Wähle Kategorie:', ['Gewicht', 'Volumen', 'Zeit', 'Temperatur', 'Blutdruck', 'Blutzucker', 'Herzfrequenz', 'Atemfrequenz', 'Dosierung', 'Flüssigkeitsstrom'])

    if category == 'Gewicht':
        unit_conversion_weight()
    elif category == 'Volumen':
        unit_conversion_volume()
    elif category == 'Zeit':
        unit_conversion_time()
    elif category == 'Temperatur':
        unit_conversion_temperature()
    elif category == 'Blutdruck':
        unit_conversion_blood_pressure()
    elif category == 'Blutzucker':
        unit_conversion_blood_sugar()
    elif category == 'Herzfrequenz':
        unit_conversion_heart_rate()
    elif category == 'Atemfrequenz':
        unit_conversion_respiratory_rate()
    elif category == 'Dosierung':
        unit_conversion_dosage()
    elif category == 'Flüssigkeitsstrom':
        unit_conversion_fluid_flow()

def unit_conversion_weight():
    st.header('Gewichtsumrechner')

    # Gewichtseinheiten: Kilogramm, Gramm, Milligramm
    # Hier kann der Benutzer ein Gewicht in einer Einheit eingeben und es in andere Einheiten umrechnen
    # Beispielcode für die Gewichtsumrechnung

def unit_conversion_volume():
    st.header('Volumenumrechner')

    # Volumeneinheiten: Liter, Milliliter, Mikroliter
    # Hier kann der Benutzer ein Volumen in einer Einheit eingeben un


   








