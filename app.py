import openai_secret_manager
import openai
import streamlit as st

# Récupérer l'API key de OpenAI

openai.api_key = "API_KEY"

# Fonction pour generer un programme nutritionnel personnalise
def generer_programme_nutritionnel(sexe, age, taille, poids, niveau_activite, objectif):
    # Calcul du besoin calorique de base
    if sexe == "Homme":
        besoin_calorique_base = 88.36 + (13.4 * poids) + (4.8 * taille) - (5.7 * age)
    else:
        besoin_calorique_base = 447.6 + (9.2 * poids) + (3.1 * taille) - (4.3 * age)

    # Calcul du besoin calorique total en fonction du niveau d'activite physique
    if niveau_activite == "Sedentaire":
        besoin_calorique_total = besoin_calorique_base * 1.2
    elif niveau_activite == "Peu actif":
        besoin_calorique_total = besoin_calorique_base * 1.375
    elif niveau_activite == "Actif":
        besoin_calorique_total = besoin_calorique_base * 1.55
    else:
        besoin_calorique_total = besoin_calorique_base * 1.725

    # Si l'objectif est de perdre du poids, on reduit les calories de 500 par jour
    if objectif == "Perte de poids":
        besoin_calorique_total -= 500
    # Si l'objectif est de prendre du poids, on augmente les calories de 500 par jour
    elif objectif == "Prise de poids":
        besoin_calorique_total += 500
    # Sinon, on garde le même nombre de calories

    # Generer le programme nutritionnel
    prompt = (
        f"Je suis un Chatbot qui peut vous aider a etablir un programme nutritionnel et de gym personnalise en fonction de vos besoins.\n\n"
        f"Il s'agit d'un(e) {sexe.lower()} de {age} ans, mesurant {taille} cm pour un poids de {poids} kg, et qui a un niveau d'activite physique {niveau_activite.lower()}.\n\n"
        f"Son objectif est {objectif.lower()}.\n\n"
        f"Pour atteindre cet objectif, donne des repas recommandes et un programme de gym qui devrait l' aider :"
    )
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()

    return message

# Interface utilisateur avec Streamlit
st.set_page_config(page_title="Programme nutritionnel et de gym personnalise")

st.title("Programme nutritionnel et de gym personnalise")

sexe = st.radio("Sexe :", ["Homme", "Femme"])
age = st.slider("Age :", min_value=1, max_value=100, value=25, step=1)
taille = st.slider("Taille (en cm) :", min_value=100, max_value=250, value=175, step=1)
poids = st.slider("Poids (en kg) :", min_value=30, max_value=200, value=60, step=1)
niveau_activite = st.selectbox("Niveau d'activite physique :", ["Sedentaire", "Peu actif", "Actif", "Tres actif"])
objectif = st.selectbox("Objectif :", ["Perte de poids", "Maintenir son poids", "Prise de poids"])

if st.button("Generer programme nutritionnel/gym"):
    programme_nutritionnel = generer_programme_nutritionnel(sexe, age, taille, poids, niveau_activite, objectif)
    st.markdown(programme_nutritionnel)
