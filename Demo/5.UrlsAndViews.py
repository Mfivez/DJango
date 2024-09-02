# Nous allons créer une vue simple dans notre application books pour afficher une liste de livres fictifs, puis configurer les URLs pour que cette vue soit accessible via le navigateur.


""" 1. Création de la Vue :

    - Les vues en Django traitent les requêtes HTTP et renvoient des réponses HTTP. Nous allons créer une vue simple pour afficher une liste de livres fictifs.

    [
        from django.http import HttpResponse
        from django.shortcuts import render

        def book_list(request):
            books = [
                {'title':'DjangoDemo', 'author':'fredou'},
                {'title':'Python', 'author':'yannick'}
            ]

            return render(request, 'books/book_list.html', {'books': books})
    ]

    - La fonction render est utilisée pour rendre un template HTML avec les données fournies.

    - Du coup, créons ce template html.

"""

""" 2. Création du Template :

    - Les templates sont des fichiers HTML qui définissent la structure et le rendu des pages web. Nous allons créer un template pour afficher la liste des livres.

    Étapes :
    - Crée un répertoire templates dans le répertoire de ton application books.

    - Crée un fichier nommé book_list.html dans le répertoire books/templates et ajoute le code suivant :

    [
        <!-- books/templates/books/book_list.html -->
        <!DOCTYPE html>
        <html>
        <head>
            <title>Book List</title>
        </head>
        <body>
            <h1>Book List</h1>
            <ul>
                {% for book in books %}
                    <li>{{ book.title }} by {{ book.author }}</li>
                {% endfor %}
            </ul>
        </body>
        </html>
    ]

"""

""" Urls :

    - 1. Pour rendre la vue accessible via une URL, nous devons configurer les URLs dans l'application et le projet principal.

    a. Configuration des URLs dans l'application books
        - Créer un fichier urls.py dans notre application books afin d'y créer toutes les urls qui seront liées à notre application.

        [
            from django.urls import path
            from . import views

            urlpatterns = [
                path('books/', views.book_list, name='book_list'),
            ]
        ]

    b. Inclusion des URLs de l'application dans le projet principal
        [
            urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('books.urls'))
            ]
        ]

        -La ligne path('', include('books.urls')) inclut les URLs définies dans books/urls.py dans les URLs de votre projet principal.
        - Cela permet à Django de savoir que lorsqu'une requête correspond à /books/, elle doit être traitée par les URLs définies dans books/urls.py

"""

""" Settings :

    - Il faut aussi ajouter notre application dans la liste des applis dans settings afin de faire connaitre à notre projet principal l' application nommée book : 
    [
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'books'
        ]
    ]
"""

""" Vérifier le résultat.

    - Maintenant que nous avons fait tout ça, essayons de voir ce que ça donne en lançant le serveur :
        - python manage.py runserver

"""
