# Nous allons travailler dans le cadre de ce cours avec le framework Django. Mais avant d'attaquer le cours posons nous la question qu'est-ce qu'un framework, puis qu'est-ce que Django ?

""" 1. Qu'est-ce qu'un framework :
- Si nous le traduisons littéralement, framework signifie cadre de travail.

- Un framework vise à apporter aux développeurs des outils visant à simplifier le développement de programmes comme, par exemple, des sites webs.

- Comment ?
    Et bien, lorsqu'on développe des applications, il y a (presque) toujours des choses qui sont communes à la majorité des programmes. Les frameworks font donc tous leur possible pour offrir ces bases aux développeurs afin qu'ils puissent se concentrer sur les particularités de leur projet en leur faisant gagner énormément de temps.

- Niveau avantages ?
    - Un framework instaure en quelque sorte une « ligne de conduite ». 
    - Tous les développeurs Django codent de façon assez homogène (leurs codes ont le même fonctionnement et applique les mêmes principes). 
    - De ce fait, lorsqu'un développeur rejoint un projet utilisant un framework qu'il connaît déjà, il comprendra très vite ce projet et pourra se mettre rapidement au travail
"""

# Maintenant que nous savons ce qu'est un framework et ce que sont ses objectifs, qu'en est-il du framework Django ?


""" Du coup, Django c'est quoi ?
    - Un framework python destiné au web.
    
    - Django vit le jour en 2003, dans une agence de presse qui visait à développer des sites webs plutôt complets. Il fût ensuite publié en 2005 et trouva très rapidement succès et communauté  grâce à sa robustesse ou encore sa gestion de la sécurité le menant à être très utilisé même par des géants de ce monde telles qu'Instagram, Pinterest ou même encore la Nasa.

    - Pourquoi ce succès ?
        - Django applique avec excellence le principe nommé "don't repeat yourself". En django ce que l'on fait, on ne le fait qu'une fois !
        - De plus comme dit précédemment, le framework possède une large communauté l'aidant à se développer continuellement et une documentation très très complète.
"""

# Et si on parlait du paradigme du MVC ? 

""" C'est quoi un paradigme ?
    - Un paradigme en programmation est une approche ou un style de programmation basé sur un ensemble de concepts et de principes. Il détermine la manière dont les développeurs structurent et écrivent leur code, par exemple, la programmation orientée objet.
"""

""" Et du coup, c'est quoi le MVC :

    - Dans un premier temps décomposons cet acronyme :
    - M : Modèle.
    - V : Vue.
    - C : Contrôleur.
"""

""" Le Modèle : 
    1. Rôle :
        - Il représente les données de l'application et les règles de gestions associées.

        - Il est chargé de gérer l'accès à la base de données, d'effectuer les requêtes et de renvoyer les données sous un format exploitable.

    2. Exemple : 
        - Tu développes un site de gestion de bibliothèque. 
        Le modèle serait la partie qui définit ce qu'est un "Livre" (titre, auteur,...), comment les livres sont stockés dans la base de données, et comment les récupérer ou les modifier.
"""

""" La Vue : 
    1. Rôle :
        - Elle est responsable de l'affichage des données à l'utilisateur. 

        - Elle prend les données du modèle et les présente sous forme d'interface utilisateur (UI), que ce soit sous forme de pages HTML, de JSON, ou autre.

    2. Exemple : 
        - Dans notre site de gestion de bibliothèque, une vue pourrait être une page qui affiche la liste des livres disponibles. Elle reçoit les données du modèle et les affiche dans une liste lisible pour l'utilisateur.
"""

""" Le Contrôler: 
    1. Rôle :
        - Il agit comme un intermédiaire entre le modèle et la vue. 
        
        - Il reçoit les entrées utilisateur (par exemple, via des formulaires ou des URL), interagit avec le modèle pour traiter ces données, et décide quelle vue renvoyer à l'utilisateur.

    2. Exemple : 
        -  Si un utilisateur recherche un livre particulier, le contrôleur va recevoir cette requête, demander au modèle de récupérer les livres correspondant à la recherche, puis passer ces informations à la vue qui les affichera.
"""

""" Petit schéma :

- [User] intéragit avec [Une vue 🖥️] (une page internet)

- [La vue] envoie la requête au [Contrôler].

- Le [Contrôler] demande au [Modèle] ce dont il a besoin dans la db.

- La[DB] envoie les données au [Contrôler]

- Le [Contrôler] renvoie une nouvelle vue avec les données traitées à l'utilisateur.

"""

# Ok, mais Django dans tout ça ? Le MVT.

"""  Django et le MVT ?

    - Django applique un modèle très similaire au MVC, mais avec une légère variation. 
    Le concept reste le même, mais la terminologie et le rôle de certains composants sont un peu ajustés.

"""

""" Décomposons l'acronyme MVT :
    M : Modèle
    V : Vue
    T : Template
"""

""" Le Modèle :

    - Identique au MVC : 
        Le modèle en Django est exactement ce que nous avons décrit pour le MVC. Il gère les données, la logique de l'application, et les interactions avec la base de données.

    - Exemple : 
        Dans Django, tu définirais un modèle "Book" qui spécifie comment un livre est représenté dans la base de données.

"""

""" La vue :

    - Rôle légèrement différent : 
        Dans Django, la vue n'est pas responsable de l'affichage comme dans le MVC. 
    
        Au lieu de cela, la vue en Django est un contrôleur qui gère la logique métier. 
    
        Elle traite les requêtes HTTP, interagit avec le modèle pour obtenir les données nécessaires, et sélectionne le template approprié pour générer la réponse.

    - Exemple : 
        Une vue Django pourrait traiter une requête pour afficher tous les livres disponibles. Elle récupère la liste des livres du modèle et les transmet à un template pour affichage.

"""

""" Le Template :

    - Remplace la Vue du MVC : 
        Le template dans Django est responsable de l'affichage. 
        
        C'est un fichier HTML avec des balises spécifiques de Django pour intégrer dynamiquement les données transmises par la vue.

    - Exemple : 
        Le template pourrait être un fichier HTML qui reçoit la liste des livres et les affiche sous forme de tableau ou de liste, avec un design défini par le développeur.

"""