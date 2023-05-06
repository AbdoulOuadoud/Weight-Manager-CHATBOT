# Weight-Manager-CHATBOT

Ce code est un programme qui génère un programme nutritionnel et de gym personnalisé en fonction des besoins d'une personne. Il utilise l'API OpenAI pour générer des recommandations en se basant sur les informations fournies.

# Installation
Pour exécuter ce code, vous devez installer les bibliothèques Python suivantes :

  openai
  streamlit

Vous pouvez les installer en utilisant pip :

  pip install openai
  pip install streamlit

# Configuration de l'API

Avant d'exécuter le code, vous devez récupérer votre clé API OpenAI et la configurer dans le code. Assurez-vous d'avoir une clé valide pour pouvoir accéder aux fonctionnalités de génération de texte de l'API.

  openai.api_key = "VOTRE_CLÉ_API_OPENAI"

#Utilisation

Une fois que vous avez configuré votre clé API, vous pouvez exécuter le code en utilisant la commande suivante :

  streamlit run nom_du_fichier.py

Une interface utilisateur Streamlit s'ouvrira dans votre navigateur. Vous devrez fournir les informations nécessaires, telles que le sexe, l'âge, la taille, le poids, le niveau d'activité physique et l'objectif. En cliquant sur le bouton "Générer programme nutritionnel/gym", le programme utilisera les informations fournies pour générer un programme personnalisé.

# Limitations

Il est important de noter que ce programme utilise des modèles de génération de texte basés sur l'IA. Bien que les recommandations générées puissent être utiles, elles ne doivent pas être considérées comme des conseils médicaux professionnels. Il est toujours préférable de consulter un professionnel de la santé ou un nutritionniste avant de suivre un programme nutritionnel ou de gym.

De plus, veuillez faire attention à ne pas partager votre clé API OpenAI avec d'autres personnes, car cela pourrait compromettre la sécurité de votre compte et de vos données.

# Contributions

Les contributions à l'amélioration de ce programme sont les bienvenues. Si vous trouvez des problèmes ou souhaitez ajouter de nouvelles fonctionnalités, n'hésitez pas à ouvrir une demande d'extraction sur GitHub.

# Avertissement

Ce code utilise des bibliothèques tierces et dépend de services externes. Assurez-vous de comprendre les conditions d'utilisation de ces bibliothèques et services, ainsi que les implications potentielles pour votre application.
