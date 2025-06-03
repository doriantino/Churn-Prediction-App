import os
import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Définir le chemin de base pour les ressources
# Cela pointe vers le dossier où se trouve app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chemins complets vers les fichiers du modèle et du seuil
# Les fichiers model_5_features.pkl et threshold_5_features.pkl doivent être directement dans le dossier Churn_App
MODEL_PATH = os.path.join(BASE_DIR, 'model_5_features.pkl')
THRESHOLD_PATH = os.path.join(BASE_DIR, 'threshold_5_features.pkl')

# Chargement du modèle et du seuil au démarrage de l'application
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(THRESHOLD_PATH, 'rb') as f:
        threshold = pickle.load(f)
    print("Modèle et seuil chargés avec succès.")
except FileNotFoundError as e:
    print(f"Erreur: Fichier introuvable. Assurez-vous que 'model_5_features.pkl' et 'threshold_5_features.pkl' sont dans le répertoire '{BASE_DIR}'. Détails: {e}")
    model = None
    threshold = None
except Exception as e:
    print(f"Erreur lors du chargement du modèle ou du seuil: {e}")
    model = None
    threshold = None

@app.route('/')
def home():
    """
    Route principale pour afficher la page HTML de l'application.
    Le fichier index.html doit se trouver dans le dossier 'templates' qui est un sous-dossier de Churn_App.
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Route pour gérer les requêtes de prédiction.
    Elle reçoit les données du formulaire HTML de l'interface de Churn.
    """
    if model is None or threshold is None:
        return jsonify({'prediction_result': "Erreur interne: Modèle ou seuil non chargés. Veuillez contacter l'administrateur."}), 500

    try:
        data = request.form

        # Extrait les 5 features utilisées par le modèle de CHURN
        # Assurez-vous que les noms des champs correspondent EXACTEMENT à ceux de votre formulaire HTML de CHURN
        monthly_minutes = float(data['MonthlyMinutes'])
        monthly_revenue = float(data['MonthlyRevenue'])
        current_equipment_days = float(data['CurrentEquipmentDays'])
        perc_change_minutes = float(data['PercChangeMinutes'])
        perc_change_revenues = float(data['PercChangeRevenues'])

        # Crée un tableau NumPy pour la prédiction
        features = np.array([[
            monthly_minutes,
            monthly_revenue,
            current_equipment_days,
            perc_change_minutes,
            perc_change_revenues
        ]])

        # Fait la prédiction de probabilité
        probability_of_churn = model.predict_proba(features)[:, 1][0]

        # Applique le seuil
        if probability_of_churn >= threshold:
            prediction_text = "forte probabilité de désabonnement (Churn)"
        else:
            prediction_text = "faible probabilité de désabonnement (Churn)"

        probability_percentage = round(probability_of_churn * 100, 2)

        return jsonify({
            'prediction_result': prediction_text,
            'probability': probability_percentage
        })

    except ValueError:
        return jsonify({'prediction_result': "Erreur: Veuillez entrer des valeurs numériques valides pour tous les champs."}), 400
    except KeyError as e:
        return jsonify({'prediction_result': f"Erreur: Champ manquant dans le formulaire de CHURN: {e}. Vérifiez les noms des champs HTML."}), 400
    except Exception as e:
        print(f"Erreur inattendue lors de la prédiction du churn: {e}")
        return jsonify({'prediction_result': f"Une erreur interne est survenue: {e}"}), 500

if __name__ == '__main__':
    # Utilisez debug=True en développement pour voir les erreurs
    # Passez à False pour la production
    app.run(host='0.0.0.0', port=5000, debug=False)