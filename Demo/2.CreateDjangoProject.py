# Lorsqu'on développe un projet, il est important d'isoler les dépendances liés à celui-ci afin d'éviter de possibles problèmes de conflit et de garder son environnement propre. Pour se faire nous allons créer un environnement virtuel dédié au projet que nous développons.

""" Etapes :
    1. Ouvrez le terminal depuis Vs Code
    2. Exécuter la commande :
    3. py -m venv EnvDjango
        a. EnvDjango étant le nom de votre environnement virtuel.
    4. Exécuter la commande suivante pour activer votre environnement :
        - Windows : .\EnvDjango\Scripts\activate
        - Linux/Mac : source env/bin/activate
"""
#Oh My posh => styliser terminal

# Une fois notre environnement virtuel créé et activé, nous allons commencer à installer toutes les choses qui seront nécessaires au bon développement de notre application. (Pour le moment juste Django) :

""" Etapes :
    1. Effectuer, dans le terminal où  notre environnement est activé la commande :
        - pip install django 
    2. Afin de vérifier que tout s'est bien déroulé, nous pouvons ensuite effectuée la commande :
        - django-admin --version

"""

# Nous sommes enfin prêt à créer notre 1 er projet Django :

""" Etapes :
    1. Pour se faire, exécuter la commande :
        - Django-admin startproject firstProject
"""