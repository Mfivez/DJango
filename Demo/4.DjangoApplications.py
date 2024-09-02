# Avant de commencer à créer nos programmes Django, essayons de comprendre comment Django organise et gère un projet, et ce, grâce à ce qu'on appelle des "Applications".

""" Qu'est-ce qu'une application Django ?

    -  C'est une composante modulaire qui encapsule un ensemble spécifique de fonctionnalités ou de services, tels qu'un blog ou un système de gestion d'utilisateurs. 
    
    - Chaque application est un paquet autonome avec ses propres modèles, vues, et templates, permettant une organisation claire et réutilisable du code.

    Exemple gestion bibliothèque :
     
      -  vous pourriez créer une application nommée catalogue qui pourrait inclure :

        - Des modèles : Définissant des entités comme Livre, Auteur, et Genre.
        
        - Vues : Gérant la logique pour afficher la liste des livres, les détails d'un livre, et les fonctionnalités de recherche.

        - Templates : Rendant les pages web pour consulter les livres disponibles, ajouter de nouveaux livres, et visualiser les détails des ouvrages.
"""

# D'accord, c'est bien beau, mais pourquoi, c'est quoi l'objectif derrière tout ça :

""" A quoi ça sert les applications ?

    - A vous qui êtes développeur, quelle est la chose qui composera la majorité de votre temps de travail ?

    - La maintenance. Mais quel est le lien avec les applications ? Regardons cela de plus près.

    - Mise en contexte :

        - Vous développez un nouveau site web.
        Le monde est beau, tout est facile, il y a peu de features, peu de code et la complexité du projet est moindre.

        - Cependant, cette situation est temporaire. Avec le temps, votre projet va croître, les fonctionnalités vont se multiplier, et la complexité va exploser.

        - Si vous n'êtes pas préparé à affronter cette complexité, vous risqueriez de perdre beaucoup de temps et d'énergie.

        - Ca, tous les développeurs ayant déjà eu l'occasion de travailler sur des projets assez conséquents le savent, et c'est pour ça qu'ils mettent au point des stratégies pour organiser et maintenir leur code afin de faire face à ces défis.

        - Les applications Django en sont un parfait exemple. Elles visent à rendre le code modulable et facilement maintenable, en assurant une indépendance maximale entre les différentes parties du projet.

"""

# Créons notre 1 ère application.

""" Etapes :
    1. Tout d'abord, rendons-nous dans le terminal à l'intérieur de notre projet Django :
        - cd firstProject.
    1. Pour créer une application, il faut exécuter la commande :
        - python manage.py startapp books
"""

# On peut constater qu'une nouvelle application a bien été crée à l'intérieur de la structure de notre projet. Décomposons et expliquons chaque partie de celle-ci afin de comprendre à quoi servent ces fichiers et dossiers au sein de l'application.

""" Structure :
    
    1. migrations
    2. __init__.py
    3. admin.py
    4. apps.py
    5. models.py
    6. tests.py
    7. views.py 
"""

""" 1. apps.py

    - Description :
        - Il contient la configuration de l'application. 
        
        Il est utilisé pour définir des paramètres spécifiques pour l'application.

    - Composition par défaut : 
        - default_auto_field :
            il définit le type des champs automatiquement générées dans nos applications :

            BigAutoField génère un BigInt qui s'incrémente automatiquement à chaque nouvel enregistrement.

        - Pourquoi : 
            Lorsqu'on crée un modèle dans Django, chaque instance du modèle a généralement un identifiant unique. Par défaut, Django crée ce champ automatiquement pour vous.
"""

""" 2. Le dossier migrations

    - Description :
        Il contient Les fichiers de migration de votre application.
        
        - Les migrations sont des scripts qui permettent de gérer les changements dans la structure de votre base de données. 
        
        - Par exemple, si vous ajoutez un nouveau modèle ou modifiez un modèle existant, vous devrez créer une migration pour appliquer ces changements à la base de données.

        - Pour le moment ce dossier est presque vide puisque nous n'avons pas encore créer de modèles.

"""

""" 3. __init__.py

    - Description :
         - Indicateur pour Python précisant que ce répertoire doit être traité comme un package Python. 
         
         - Il peut être vide, mais sa présence permet d'importer les modules du répertoire books dans d'autres parties du projet.

"""

""" 4. admin.py

    - Description :
         - Ce fichier est utilisé pour configurer l'interface d'administration de Django pour votre application. 
         
         - Vous y définissez comment les modèles de votre application apparaîtront dans l'interface d'administration de Django.

"""

""" 5. models.py

    - Description :
         - il est l'endroit où vous définissez les modèles de données pour votre application. 
         
         - Les modèles sont des classes qui définissent la structure des données et la manière dont elles interagiront avec la base de données.

"""

""" 6. tests.py

    - Description :
         - il est destiné à contenir les tests unitaires pour votre application. 
         
         - Vous y écrivez des tests pour vérifier que vos modèles, vues, et autres composants fonctionnent correctement.

"""

""" 7. views.py

    - Description :
         - Il est l'endroit où vous définissez les vues pour votre application. 
         
         - Celles-ci sont responsables de la logique métier et de la gestion des requêtes HTTP, et elles retournent généralement des réponses HTTP.

"""