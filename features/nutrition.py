import openai
from utils.settings import API_KEY

openai.api_key = API_KEY


class ProgramGenerator:
    """
    This class is an interface of a nutrition program for a user
    """

    def __init__(self, age: int, niveau_activite: str, objectif: str, poids: float,  sexe: str,  taille: float) -> None:
        """
        Class instancing:

        attrs:
            age: 
            niveau_activite: 
            objectif: 
            poids: 
            sexe: 
            taille:

        """
        self.age = age
        self.sexe = sexe
        self.poids = poids
        self.taille = taille
        self.objectif = objectif
        self.niveau_activite = niveau_activite

        self._basic_caloric_need = None
        self._total_caloric_need = None

        self._cache = None
        self._cache_key = None

    def initialize(self):
        """
        Initialize default cache and cache key and other util default self attrs.

        """
        self._cache = {}
        self._cache_key = (self.sexe, self.age, self.taille, self.poids,
                           self.niveau_activite, self.objectif)
    
    def get_cache(self):
        
        """
        Return the data saved in cache
        """

    def get_basic_caloric_need(self):
        """
        Return the value of the user's basic_caloric_need

        """
        return self._basic_caloric_need

    def get_total_caloric_need(self):
        """
        Return the value of the user's total_caloric_need

        """
        return self._total_caloric_need

    def find_basic_caloric_need(self) -> float:
        """

        Determine the basic caloric need of the user based on his sex, his weight, 
        his tail, his age

        """
        if self.sexe == "Homme":
            besoin_calorique_base = 88.36 + \
                (13.4 * self.poids) + (4.8 * self.taille) - (5.7 * self.age)
        else:
            besoin_calorique_base = 447.6 + \
                (9.2 * self.poids) + (3.1 * self.taille) - (4.3 * self.age)

        self._basic_caloric_need = besoin_calorique_base

    def find_total_caloric_need(self) -> float:
        """
        Determine the total caloric need of the user based on his basic caloric need
        and his physical activity level

        """
        # Calcul du besoin calorique total en fonction du niveau d'activité physique
        if self.niveau_activite == "Sédentaire":
            besoin_calorique_total = self._basic_caloric_need * 1.2
        elif self.niveau_activite == "Peu actif":
            besoin_calorique_total = self._basic_caloric_need * 1.375
        elif self.niveau_activite == "Actif":
            besoin_calorique_total = self._basic_caloric_need * 1.55
        else:
            besoin_calorique_total = self._basic_caloric_need * 1.725

        self._total_caloric_need = besoin_calorique_total

    def update_total_caloric_need(self):

        # Si l'objectif est de perdre du poids, on réduit les calories de 500 par jour
        if self.objectif == "Perte de poids":
            self._total_caloric_need -= 500
        # Si l'objectif est de prendre du poids, on augmente les calories de 500 par jour
        elif self.objectif == "Prise de poids":
            self._total_caloric_need += 500
        # Sinon, on garde le même nombre de calories

    def check_result_existence_in_cache(self) -> bool:
        """
        Check whenever a nutrititional program have been generated and store in the cache
        for a user with same needs with the current.

        """
        return self._cache_key in self._cache

    def generate_result(self, prompt: tuple):
        """
        Generate nutrititional program for the user

        args:
            prompt:  tuple of str to pass to openai to generate program

        """
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return completions.choices[0].text.strip()

    def process(self):
        """
        Process the generation of nutrititonal program

        """
        self.initialize()

        self.get_basic_caloric_need()
        self.get_total_caloric_need()

        if self.check_result_existence_in_cache():
            message = self.cache[self.cache_key]
        else:
            prompt = (
                f"Je suis un Chatbot qui peut vous aider à établir un programme nutritionnel personnalisé en fonction de vos besoins.\n\n"
                f"Il s'agit d'un(e) {self.sexe.lower()} de {self.age} ans, mesurant {self.taille} cm pour un poids de {self.poids} kg, et qui a un niveau d'activité physique {self.niveau_activite.lower()}.\n\n"
                f"Son objectif est {self.objectif.lower()}.\n\n"
                f"Pour atteindre cet objectif, voici un programme nutritionnel et un programme de gym qui devrait l'aider:"
            )
            message = self.generate_result(prompt=prompt)

        return message
