Votre Assistant de Prédiction de Désabonnement Client
C'est quoi ce projet ?
Imaginez pouvoir anticiper quels clients risquent de ne plus utiliser vos services. Ce projet, c'est exactement ça ! C'est une petite application web conçue pour vous aider à prédire le désabonnement (ou "churn") de vos clients.

En clair, vous entrez quelques informations clés sur un client, et notre intelligence artificielle (IA) estime la probabilité qu'il vous quitte. C'est votre "boule de cristal" pour agir avant qu'il ne soit trop tard !

Qu'est-ce que ça fait concrètement ?
Interface Simple et Claire : Une page web intuitive avec un formulaire facile à remplir.

Prédiction Intelligente : Un modèle d'IA puissant analyse les données que vous fournissez.

Résultat Immédiat et Visuel : Une fenêtre pop-up apparaît avec un message clair (par exemple, "forte probabilité de désabonnement") et un pourcentage précis.

Design Agréable : L'application est conçue pour être visuellement plaisante et facile à utiliser.

Comment ça marche (pour les curieux) ?
Votre application fonctionne comme un mini-site web sur votre ordinateur. Elle est composée de :

app.py : C'est le cerveau en Python qui gère toute la logique et les calculs.

templates/index.html : C'est la page web que vous voyez et avec laquelle vous interagissez.

model_5_features.pkl et threshold_5_features.pkl : Ce sont les "connaissances" de l'IA, des fichiers spéciaux qui contiennent le modèle entraîné à prédire le churn.

Les outils utilisés (la "boîte à outils" du projet)
Ce projet a été développé avec :

Python : Le langage de programmation principal.

Flask : Un micro-framework web qui sert de "colle" entre l'IA et l'interface.

Scikit-learn & LightGBM : Des bibliothèques Python essentielles pour l'entraînement et l'utilisation de l'intelligence artificielle.

HTML, CSS, JavaScript : Les langages standards pour créer l'interface web (structure, style, interactivité).

PyInstaller : Un outil génial pour transformer l'application en un fichier .exe autonome.

Git & GitHub : Pour gérer les versions du code et le partager en ligne.

Comment l'utiliser sur votre ordinateur (Guide rapide pour débutants)
Ce qu'il vous faut (les "ingrédients" de base)
Python 3.12 : Téléchargez-le depuis python.org. Important : Cochez bien "Add Python to PATH" pendant l'installation.

Git : Installez-le depuis git-scm.com/downloads.

1. Téléchargez le projet
Ouvrez votre terminal (recherchez "PowerShell" dans Windows) et tapez :

git clone https://github.com/doriantino/Churn-Prediction-App.git
cd Churn-Prediction-App

(Si vous avez renommé le dossier localement, adaptez cd Churn-Prediction-App en cd NomDeVotreDossier)

2. Préparez l'environnement (votre "espace de travail" Python)
C'est une étape cruciale pour que l'application ait tous ses outils, sans interférer avec d'autres projets Python.

# Crée l'espace de travail virtuel
python -m venv .venv

# Active cet espace de travail (pour PowerShell)
. .\.venv\Scripts\Activate.ps1

Votre terminal devrait maintenant afficher (.venv) au début de chaque ligne, confirmant que l'environnement est actif.

3. Installez les outils nécessaires
Avec l'espace de travail activé, installez toutes les bibliothèques Python requises :

pip install Flask numpy scikit-learn lightgbm

4. Lancez l'application !
Assurez-vous d'être dans le dossier Churn-Prediction-App (là où se trouve app.py) et que (.venv) est toujours affiché dans votre terminal.

# Dites à Python où est l'application principale
$env:FLASK_APP = "app.py"

# Lancez l'application
flask run

Une adresse web (comme http://127.0.0.1:5000/) apparaîtra dans votre terminal. Copiez-la et collez-la dans votre navigateur web préféré.

Comment ça marche (l'application en action)
Ouvrez l'adresse web dans votre navigateur.

Remplissez les quelques champs du formulaire avec les informations du client que vous souhaitez analyser.

Cliquez sur le bouton "Prédire le Désabonnement".

Une petite fenêtre (pop-up) apparaîtra avec la prédiction de l'IA !

Le Cœur de l'IA (pour ceux qui veulent en savoir plus)
L'intelligence artificielle au centre de ce projet est un modèle appelé LightGBM. C'est un type de modèle très performant, capable d'identifier des schémas complexes dans les données. Il a été "entraîné" sur un ensemble de données historiques pour apprendre ce qui caractérise un client qui reste ou un client qui part.

Créer une version pour Windows (.exe) (Optionnel)
Si vous souhaitez distribuer cette application comme un programme Windows standard (sans que les utilisateurs n'aient à installer Python), vous pouvez créer un fichier .exe :

Assurez-vous d'avoir installé PyInstaller dans votre espace de travail (pip install pyinstaller).

Dans votre terminal (toujours dans le dossier Churn-Prediction-App et avec (.venv) activé), tapez cette commande (sur une seule ligne) :

pyinstaller app.py --name "ChurnPredictorApp" --onefile --add-data "templates;templates" --add-data "model_5_features.pkl;." --add-data "threshold_5_features.pkl;." --add-binary "C:\Users\DORIAN\Desktop\Projets\Churn\.venv\DLLs\pyexpat.pyd;." --collect-all flask --collect-all numpy --collect-all lightgbm --collect-all scikit-learn --hidden-import "sklearn.neighbors._typedefs" --hidden-import "scipy.sparse.csgraph._validation" --hidden-import "scipy.special.cython_special" --hidden-import "xml.etree.ElementTree" --hidden-import "xml.dom.minidom" --windowed

(Important : Vérifiez bien le chemin de pyexpat.pyd dans la commande ci-dessus. Il doit correspondre à l'emplacement réel sur votre PC.)

Un fichier ChurnPredictorApp.exe sera créé dans un dossier nommé dist/ à l'intérieur de votre projet, prêt à être exécuté !

Contribuer au projet
Vous avez des idées pour améliorer cet assistant, ou vous souhaitez corriger un bug ? C'est super ! N'hésitez pas à proposer vos changements.

Licence
Ce projet est sous licence MIT.

Contact
Pour toute question ou suggestion, n'hésitez pas à me contacter :

Nom : Dorian DIKOUME

GitHub : doriantino

Email : dikoume383@gmail.com