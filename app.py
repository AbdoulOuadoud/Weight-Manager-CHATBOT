import streamlit as st

from features.nutrition import ProgramGenerator

# Interface utilisateur avec Streamlit
st.set_page_config(page_title="Programme nutritionnel personnalisé")
st.title("Programme nutritionnel personnalisé")

# Déclaration du cache
cache = {}

sexe = st.radio("Sexe :", ["Homme", "Femme"])
age = st.slider("Age :", min_value=18, max_value=100, value=25, step=1)
taille = st.slider("Taille (en cm) :", min_value=100,
                   max_value=250, value=175, step=1)
poids = st.slider("Poids (en kg) :", min_value=30,
                  max_value=200, value=60, step=1)
niveau_activite = st.selectbox("Niveau d'activité physique :", [
                               "Sédentaire", "Peu actif", "Actif", "Très actif"])
objectif = st.selectbox(
    "Objectif :", ["Perte de poids", "Maintenir son poids", "Prise de poids"])

if st.button("Générer programme nutritionnel"):
    # Vérifier si toutes les informations nécessaires sont fournies
    if sexe and age and taille and poids and niveau_activite and objectif:
        program_generator = ProgramGenerator(age=age, niveau_activite=niveau_activite, objectif=objectif, poids=poids, sexe=sexe, taille=taille)
        nutritional_program = program_generator.process()
        st.markdown(nutritional_program)
    else:
        st.error(
            "Veuillez fournir toutes les informations nécessaires pour générer le programme nutritionnel.")
