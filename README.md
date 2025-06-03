Votre Assistant de Prédiction de Désabonnement Client
C'est quoi ce projet ?
Imaginez que vous puissiez savoir à l'avance quels clients risquent de vous quitter. Ce projet, c'est exactement ça ! C'est une petite application web qui vous aide à prédire le désabonnement (ou "churn") de vos clients.

En gros, vous entrez quelques informations sur un client, et l'application utilise une intelligence artificielle pour estimer s'il y a un risque qu'il parte. L'idée est de vous donner une "boule de cristal" pour agir avant qu'il ne soit trop tard !

Qu'est-ce que ça fait concrètement ?
Facile à utiliser : Une page simple avec un formulaire où vous remplissez les infos du client.

Prédiction Intelligente : Derrière, un modèle d'intelligence artificielle (IA) analyse les données.

Résultat Clair : Une petite fenêtre apparaît avec un message simple : "forte probabilité de désabonnement" (en rouge) ou "faible probabilité" (en vert), avec un pourcentage pour mieux comprendre.

Joli Design : L'application est conçue pour être agréable à regarder et facile à naviguer.

Comment ça marche (pour les curieux) ?
L'application est comme un petit site web sur votre ordinateur. Elle est composée de :

app.py : C'est le "cerveau" en Python qui fait les calculs et gère la page.

templates/index.html : C'est la page web que vous voyez, avec le formulaire et la pop-up.

model_5_features.pkl et threshold_5_features.pkl : Ce sont les "connaissances" de l'IA, des fichiers spéciaux qui contiennent le modèle entraîné à prédire le churn.

Les outils utilisés (la "boîte à outils")
Ce projet a été créé avec :

Python : Le langage de programmation principal.

Flask : Un outil Python pour créer facilement des applications web.

Scikit-learn & LightGBM : Des bibliothèques Python pour l'intelligence artificielle et la création du modèle de prédiction.

HTML, CSS, JavaScript : Les langages pour créer l'interface web que vous utilisez.

PyInstaller : Un outil magique pour transformer l'application en un fichier .exe que vous pouvez lancer sans installer Python.

Git & GitHub : Pour gérer le code et le partager en ligne.

Comment l'utiliser sur votre ordinateur (pour les débutants)
Ce qu'il vous faut (les "ingrédients")
Python 3.12 : Installez-le depuis python.org et assurez-vous de cocher "Add Python to PATH" pendant l'installation.

Git : Installez-le depuis git-scm.com/downloads.

1. Téléchargez le projet
Ouvrez votre terminal (recherchez "PowerShell" dans Windows) et tapez :

git clone https://github.com/doriantino/Churn-Prediction-App.git
cd Churn-Prediction-App

(Si vous avez renommé le dossier localement, adaptez cd Churn-Prediction-App en cd NomDeVotreDossier)

2. Préparez l'environnement (votre "espace de travail" Python)
C'est important pour que l'application ait tous ses outils.

# Crée l'espace de travail virtuel
python -m venv .venv

# Active cet espace de travail (pour PowerShell)
. .\.venv\Scripts\Activate.ps1

Votre terminal devrait maintenant afficher (.venv) au début de chaque ligne.

3. Installez les outils nécessaires
Avec l'espace de travail activé, installez les outils de l'IA :

pip install Flask numpy scikit-learn lightgbm

4. Lancez l'application !
Assurez-vous d'être dans le dossier Churn-Prediction-App (là où se trouve app.py) et que (.venv) est toujours affiché.

# Dites à Python où est l'application principale
$env:FLASK_APP = "app.py"

# Lancez l'application
flask run

Une adresse web (comme http://127.0.0.1:5000/) apparaîtra. Copiez-la et collez-la dans votre navigateur web.

Comment ça marche (l'application)
Ouvrez l'adresse web dans votre navigateur.

Remplissez les quelques champs du formulaire avec les informations du client.

Cliquez sur "Prédire le Désabonnement".

Une petite fenêtre apparaîtra avec la prédiction de l'IA !

Le Cœur de l'IA (pour ceux qui veulent en savoir plus)
L'intelligence artificielle utilisée est un modèle appelé LightGBM. C'est un type de modèle très efficace pour trouver des tendances dans les données. Il a été "entraîné" pour comprendre ce qui fait qu'un client reste ou part, en se basant sur des données historiques.

Créer une version pour Windows (.exe) (Optionnel)
Si vous voulez une version de l'application que vous pouvez lancer comme n'importe quel programme sur Windows (sans installer Python), vous pouvez créer un fichier .exe :

Assurez-vous d'avoir installé PyInstaller dans votre espace de travail (pip install pyinstaller).

Dans votre terminal (toujours dans le dossier Churn-Prediction-App et avec (.venv) activé), tapez cette commande (sur une seule ligne) :

pyinstaller app.py --name "ChurnPredictorApp" --onefile --add-data "templates;templates" --add-data "model_5_features.pkl;." --add-data "threshold_5_features.pkl;." --add-binary "C:\Users\DORIAN\Desktop\Projets\Churn\.venv\DLLs\pyexpat.pyd;." --collect-all flask --collect-all numpy --collect-all lightgbm --collect-all scikit-learn --hidden-import "sklearn.neighbors._typedefs" --hidden-import "scipy.sparse.csgraph._validation" --hidden-import "scipy.special.cython_special" --hidden-import "xml.etree.ElementTree" --hidden-import "xml.dom.minidom" --windowed

(Important : Vérifiez bien le chemin de pyexpat.pyd dans la commande ci-dessus. Il doit correspondre à l'emplacement réel sur votre PC.)

Un fichier ChurnPredictorApp.exe sera créé dans un dossier nommé dist/ à l'intérieur de votre projet.

Contribuer au projet
Vous avez des idées pour améliorer cet assistant ? Super ! N'hésitez pas à proposer vos changements.

Licence
Ce projet est sous licence MIT.

Contact
Pour toute question ou suggestion, n'hésitez pas à me contacter :

Nom : Dorian DIKOUME

GitHub : doriantino

Email : dikoume383@gmail.com