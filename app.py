import openai
import streamlit as st

# Récupérer l'API key de OpenAI
openai.api_key = "api_key"

# Fonction pour générer un programme nutritionnel personnalisé
def generer_programme_nutritionnel(sexe, age, taille, poids, niveau_activite, objectif):
    # Calcul du besoin calorique de base
    if sexe == "Homme":
        besoin_calorique_base = 88.36 + (13.4 * poids) + (4.8 * taille) - (5.7 * age)
    else:
        besoin_calorique_base = 447.6 + (9.2 * poids) + (3.1 * taille) - (4.3 * age)

    # Calcul du besoin calorique total en fonction du niveau d'activité physique
    if niveau_activite == "Sédentaire":
        besoin_calorique_total = besoin_calorique_base * 1.2
    elif niveau_activite == "Peu actif":
        besoin_calorique_total = besoin_calorique_base * 1.375
    elif niveau_activite == "Actif":
        besoin_calorique_total = besoin_calorique_base * 1.55
    else:
        besoin_calorique_total = besoin_calorique_base * 1.725

    # Si l'objectif est de perdre du poids, on réduit les calories de 500 par jour
    if objectif == "Perte de poids":
        besoin_calorique_total -= 500
    # Si l'objectif est de prendre du poids, on augmente les calories de 500 par jour
    elif objectif == "Prise de poids":
        besoin_calorique_total += 500
    # Sinon, on garde le même nombre de calories

    # Générer le programme nutritionnel
    prompt = (
        f"Je suis un Chatbot qui peut vous aider à établir un programme nutritionnel personnalisé en fonction de vos besoins.\n\n"
        f"Il s'agit d'un(e) {sexe.lower()} de {age} ans, mesurant {taille} cm pour un poids de {poids} kg, et qui a un niveau d'activité physique {niveau_activite.lower()}.\n\n"
        f"Son objectif est {objectif.lower()}.\n\n"
        f"Pour atteindre cet objectif, voici un programme nutritionnel et un programme de gym qui devrait l'aider:"
    )

    # Vérifier si le résultat est présent dans le cache
    cache_key = (sexe, age, taille, poids, niveau_activite, objectif)
    if cache_key in cache:
        message = cache[cache_key]
    else:
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = completions.choices[0].text.strip()
        # Ajouter le résultat au cache
        cache[cache_key] = message

    return message

# Interface utilisateur avec Streamlit
st.set_page_config(page_title="Programme nutritionnel personnalisé")
st.title("Programme nutritionnel personnalisé")

# Déclaration du cache
cache = {}

sexe = st.radio("Sexe :", ["Homme", "Femme"])
age = st.slider("Age :", min_value=18, max_value=100, value=25, step=1)
taille = st.slider("Taille (en cm) :", min_value=100, max_value=250, value=175, step=1)
poids = st.slider("Poids (en kg) :", min_value=30, max_value=200, value=60, step=1)
niveau_activite = st.selectbox("Niveau d'activité physique :", ["Sédentaire", "Peu actif", "Actif", "Très actif"])
objectif = st.selectbox("Objectif :", ["Perte de poids", "Maintenir son poids", "Prise de poids"])

if st.button("Générer programme nutritionnel"):
    # Vérifier si toutes les informations nécessaires sont fournies
    if sexe and age and taille and poids and niveau_activite and objectif:
        programme_nutritionnel = generer_programme_nutritionnel(sexe, age, taille, poids, niveau_activite, objectif)
        st.markdown(programme_nutritionnel)
    else:
        st.error("Veuillez fournir toutes les informations nécessaires pour générer le programme nutritionnel.")

