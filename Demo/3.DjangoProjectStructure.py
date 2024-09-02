# Après avoir exécuté la commande pour créer un nouveau projet Django, un nouveau dossier avec une structure spécifique a été généré. Analysons ce dossier et ses composants.

""" A quoi sert-il ?

    - Ce dossier contient la structure de base pour organiser les fichiers et les dossiers nécessaires au développement de notre application Django. 
    
    - Il facilite la gestion du projet et assure que tous les éléments nécessaires sont correctement configurés et disponibles.

"""

""" 1. Le dossier Racine du Projet :

    - Description :
         C'est le dossier racine du projet Django. 
         
         Il contient la configuration principale du projet ainsi que des sous-dossiers et fichiers nécessaires au fonctionnement du projet.

    - Contenu typique : 
        Ce dossier contient le sous-dossier du projet (nommé de la même manière que le dossier racine) et le fichier manage.py.
        
        De plus, il pourrait à l'avenir, comporter des fichiers de configuration ou encore d'initialisation.
"""

""" 2. Le Fichier manage.py :

    - Description :
          manage.py est un script de ligne de commande qui permet de gérer diverses tâches liées au projet Django. 
          
          Il est utilisé pour lancer le serveur de développement, appliquer des migrations, créer des applications, et plus encore.

    - Commandes : 
        Nous verrons un peu plus tard, quelles sont les commandes nous permettant de gérer notre projet grâce à ce fameux script manage.py.
"""

""" 3. Le sous-dossier firstProject :

    - Description :
        Ce sous-dossier porte le nom de ton projet et contient les fichiers de configuration principaux pour ton projet Django.

    - Contenu :
        
        1. __init__.py :
            Ce fichier indique à Python que ce répertoire doit être traité comme un package Python. Il est généralement vide.

        2. settings.py :
            Ce fichier contient les paramètres de configuration du projet Django. 
            
            Tu y définis des paramètres importants comme les configurations de base de données, les paramètres de sécurité, les applications installées, ect.

        3. urls.py :
            Ce fichier définit les routes URL de ton projet. 
            
            Il est utilisé pour mapper les URLs des requêtes entrantes vers les vues appropriées.

## Nous ne nous attarderons par sur le point 4 et 5 pour le moment. ##

        4. wsgi.py : 
            Ce fichier est utilisé pour déployer le projet sur un serveur web compatible WSGI (Web Server Gateway Interface). 
            
            Il est essentiel pour la configuration du serveur en production.

        5. asgi.py (optionnel selon la version) :
            Semblable à wsgi.py, mais pour les serveurs ASGI (Asynchronous Server Gateway Interface), qui sont capables de gérer des connexions asynchrones et des WebSockets.

"""