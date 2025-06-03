# 📈 Guide des Étapes du Projet : Prédiction de Désabonnement Client (Churn)

Ce document retrace les étapes clés ayant mené à la création et au déploiement de l'application web de prédiction du désabonnement client, depuis l'acquisition des données brutes jusqu'à la mise en ligne sur GitHub.

## 1. Acquisition et Compréhension des Données (Data Acquisition & Understanding)

* **Source des Données :** Les données proviennent d'un fichier CSV (par exemple, `telecom_churn_data.csv`), contenant des informations sur le comportement et les caractéristiques des clients d'une entreprise de télécommunications.
* **Volume des Données :** Analyse des dimensions du jeu de données (nombre d'enregistrements et de colonnes) pour une compréhension initiale de sa taille et de sa structure.
* **Type de Données :** Identification des types de variables (numériques, catégorielles, binaires) et exploration de leurs natures (ex: `MonthlyMinutes`, `MonthlyRevenue`, `CurrentEquipmentDays`, `Churn`).
* **Objectif de la Prédiction :** Définition claire de la variable cible : `Churn` (client désabonné/client non désabonné), qui est une variable binaire.

## 2. Exploration et Nettoyage des Données (EDA & Data Cleaning)

* **Analyse Exploratoire des Données (EDA) :**
    * Examen des statistiques descriptives (`.describe()`, `.info()`) pour chaque variable.
    * Visualisation des distributions des variables (histogrammes, boîtes à moustaches) pour identifier la symétrie, les valeurs aberrantes et les tendances.
    * Analyse des corrélations entre les variables pour comprendre les relations mutuelles et l'impact sur la variable cible.
    * Visualisation des relations entre les caractéristiques clés et la variable `Churn`.
* **Gestion des Valeurs Manquantes :**
    * Identification des colonnes et des lignes contenant des valeurs manquantes.
    * Stratégie appliquée : Imputation des valeurs manquantes (ex: par la médiane pour les variables numériques, par le mode pour les catégorielles) ou suppression des lignes/colonnes si le volume est trop important et pertinent.
* **Gestion des Valeurs Aberrantes (Outliers) :**
    * Détection des valeurs extrêmes qui pourraient fausser l'analyse et la modélisation.
    * Traitement des outliers (ex: winsorisation, transformation logarithmique pour les distributions asymétriques).
* **Gestion des Doublons :** Vérification de l'existence de doublons dans le jeu de données et suppression des enregistrements dupliqués pour assurer l'intégrité des données.

## 3. Ingénierie des Caractéristiques (Feature Engineering)

* **Création de Nouvelles Caractéristiques :**
    * `PercChangeMinutes` : Calcul du pourcentage de changement des minutes d'utilisation mensuelles par rapport au mois précédent, pour capturer la dynamique d'utilisation.
    * `PercChangeRevenues` : Calcul du pourcentage de changement des revenus mensuels par rapport au mois précédent, pour évaluer l'évolution financière du client.
* **Sélection des Caractéristiques Finales :** Identification et sélection rigoureuse des 5 caractéristiques les plus pertinentes pour la modélisation : `MonthlyMinutes`, `MonthlyRevenue`, `CurrentEquipmentDays`, `PercChangeMinutes`, `PercChangeRevenues`. Ces caractéristiques ont été jugées les plus impactantes pour la prédiction du churn.
* **Transformation des Variables :**
    * **Standardisation :** Application de `StandardScaler` sur les caractéristiques numériques sélectionnées. Cette étape est cruciale pour que le modèle traite toutes les caractéristiques sur une échelle comparable, évitant ainsi qu'une variable avec de grandes valeurs n'ait un poids disproportionné.

## 4. Modélisation Prédictive (Predictive Modeling)

* **Sélection du Modèle :**
    * Choix de l'algorithme de classification : **LightGBM (LGBMClassifier)**.
    * Justification du choix : LightGBM a été choisi pour sa grande efficacité, sa rapidité d'entraînement sur de grands ensembles de données, et sa capacité à gérer des relations complexes, en faisant un excellent candidat pour les problèmes de classification.
* **Découpage des Données :**
    * Division du jeu de données final en ensembles d'entraînement (80%) et de test (20%) à l'aide de `sklearn.model_selection.train_test_split`. La stratification sur la variable cible (`Churn`) a été appliquée pour s'assurer que la proportion de clients désabonnés/non désabonnés est la même dans les deux ensembles.
* **Entraînement du Modèle :**
    * Le modèle LightGBM a été entraîné sur l'ensemble de données d'entraînement mis à l'échelle. Des hyperparamètres spécifiques (ex: `n_estimators`, `learning_rate`, `num_leaves`) ont été ajustés pour optimiser la performance.
* **Évaluation du Modèle :**
    * **Métriques utilisées :** La performance du modèle a été mesurée sur l'ensemble de test en utilisant :
        * **AUC-ROC (Area Under the Receiver Operating Characteristic Curve) :** Pour évaluer la capacité du modèle à distinguer les classes de désabonnement.
        * **Précision (Accuracy) :** Pour le pourcentage de prédictions correctes.
        * **Rappel (Recall) :** Pour la capacité du modèle à identifier correctement tous les clients désabonnés.
        * **Précision (Precision) :** Pour la proportion de vrais positifs parmi toutes les prédictions positives.
        * **F1-Score :** Moyenne harmonique de la précision et du rappel.
    * Interprétation des résultats et discussion des compromis (par exemple, équilibre entre rappel et précision pour la détection du churn).
* **Détermination du Seuil Optimal :**
    * Analyse de la courbe Précision-Rappel pour identifier le seuil de probabilité optimal. Ce seuil est utilisé pour convertir les probabilités continues de churn en une décision binaire (0 ou 1), maximisant une métrique spécifique (par exemple, le F1-Score).
* **Sauvegarde du Modèle et du Seuil :**
    * Sérialisation du modèle LightGBM entraîné à l'aide de la bibliothèque `pickle` dans le fichier `model_5_features.pkl`.
    * Sauvegarde du seuil optimal dans le fichier `threshold_5_features.pkl`.

## 5. Développement de l'Application Web (Web Application Development)

* **Framework :** Utilisation de **Flask**, un micro-framework web Python, pour construire l'application.
* **Interface Utilisateur (Frontend) :**
    * Développement de `templates/index.html` : Création d'un formulaire HTML intuitif pour la saisie des 5 caractéristiques client nécessaires à la prédiction.
    * **Styling CSS :** Application de styles CSS pour rendre l'interface utilisateur moderne, esthétique et responsive.
    * **Interactivité JavaScript :** Implémentation de scripts JavaScript pour gérer la soumission asynchrone du formulaire (sans recharger la page) via l'API `fetch`. Les résultats de la prédiction sont ensuite affichés dans une pop-up modale conviviale.
* **Backend (Python/Flask) :**
    * `app.py` : Fichier principal de l'application.
    * **Chargement du Modèle :** Le modèle sérialisé (`model_5_features.pkl`) et le seuil (`threshold_5_features.pkl`) sont chargés en mémoire au démarrage de l'application Flask.
    * **Endpoint de Prédiction :** Création d'une route `/predict` (méthode POST) qui reçoit les données du formulaire, effectue le prétraitement nécessaire (conversion en float, mise en forme NumPy), utilise le modèle chargé pour générer une probabilité de churn, applique le seuil et renvoie une décision (ex: "forte probabilité de désabonnement") sous forme de réponse JSON.
    * **Gestion des Erreurs :** Implémentation de la gestion des erreurs pour les entrées non valides (non numériques, champs manquants) afin d'assurer la robustesse de l'application.
* **Gestion des Dépendances :** Création d'un environnement virtuel Python et installation de toutes les bibliothèques nécessaires (`Flask`, `numpy`, `scikit-learn`, `lightgbm`) via `pip`, avec possibilité de générer un fichier `requirements.txt` pour faciliter le déploiement.

## 6. Versionnement et Déploiement sur GitHub (Version Control & Deployment)

* **Initialisation du Dépôt Git :** Transformation du dossier de projet local en un dépôt Git (`git init`) pour suivre les modifications du code.
* **Configuration du `.gitignore` :** Création d'un fichier `.gitignore` pour spécifier les fichiers et dossiers à exclure du suivi de version (ex: `.venv/`, `__pycache__/`, `build/`, `dist/`, `.idea/`, fichiers de données brutes).
* **Historique des Commits :** Enregistrement régulier des modifications du code via des commits Git, avec des messages clairs et concis décrivant les changements effectués.
* **Création du Dépôt GitHub :** Mise en place d'un dépôt distant sur GitHub (ex: `https://github.com/doriantino/Churn-Prediction-App.git`) pour héberger le code source et faciliter la collaboration.
* **Liaison et Push :** Connexion du dépôt Git local au dépôt distant GitHub (`git remote add origin ...`) et envoi des commits (`git push`) pour synchroniser le code en ligne. L'authentification a été gérée via le navigateur ou un Personal Access Token (PAT).
* **Documentation du Projet :** Rédaction d'un fichier `README.md` détaillé et axé sur les compétences. Ce document sert de point d'entrée pour les recruteurs et les autres développeurs, expliquant le projet, son installation et son utilisation.
* **Intégration du Notebook Colab :** Le fichier `.ipynb` du notebook Google Colab (contenant les étapes de l'EDA, de la modélisation, etc.) a été téléchargé depuis Colab, ajouté au dépôt Git local et poussé sur GitHub. Cela permet aux recruteurs de visualiser directement le notebook rendu sur la plateforme GitHub.

---

**Comment intégrer ce document dans VS Code :**

1.  **Copiez tout le contenu** qui se trouve à l'intérieur de ce bloc de code.
2.  Dans VS Code, ouvrez votre dossier de projet (le dossier `Churn`).
3.  Créez un nouveau fichier dans ce dossier et **nommez-le `PROJECT_STEPS.md`**.
4.  **Collez le contenu copié** dans ce fichier et enregistrez-le.

VS Code reconnaîtra automatiquement le format Markdown et affichera le texte avec les titres, listes et blocs de code mis en forme. Vous pouvez utiliser la fonctionnalité de prévisualisation de Markdown de VS Code (clic droit sur le fichier `PROJECT_STEPS.md` > "Open Preview") pour voir à quoi il ressemblera.

Une fois le fichier créé, n'oubliez pas de l'ajouter à votre dépôt Git et de le pousser sur GitHub :

```bash
git add PROJECT_STEPS.md
git commit -m "docs: Add PROJECT_STEPS.md detailing the project lifecycle"
git push origin master # ou main, selon votre branche principale