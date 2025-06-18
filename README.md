
# Projet de Développement en Machine Learning

## Description du projet

Ce projet a pour objectif d'appliquer un workflow de Machine Learning pour la classification binaire sur deux jeux de données : 
1. [Banknote Authentication Dataset](https://archive.ics.uci.edu/ml/datasets/banknote+authentication)
2. [Chronic Kidney Disease Dataset](https://www.kaggle.com/mansoordaku/ckdisease)

Le projet est réalisé dans un environnement collaboratif et utilise des outils de versioning tels que Git pour gérer les contributions et maintenir des bonnes pratiques de programmation.

## Objectifs
- **Développement collaboratif** : travailler en groupe (3 à 4 personnes) pour développer des modèles de classification binaire.
- **Pratiques de programmation** : adopter des bonnes pratiques et des outils standards pour la gestion et la documentation du code.
- **Application Machine Learning** : appliquer un workflow ML comprenant pré-traitement, sélection de caractéristiques, entraînement et évaluation de modèles.

## Contenu du dépôt
Ce dépôt contient :
1. Un fichier Python principal (`functions.py`) avec les fonctions suivantes :
   - Prétraitement des données.
   - Préparation des données pour l'entraînement.
   - Entraînement de modèles (jusqu'à 5 méthodes de classification binaire).
   - Visualisation et comparaison des résultats.
2. Un fichier Jupyter Notebook (`main.ipynb`) :
   - Applique les fonctions du fichier Python sur les deux jeux de données.
   - Présente et commente les résultats.
   - Compare les méthodes et discute des bonnes pratiques de programmation.
3. Un fichier de tests unitaires (si nécessaire).
4. Les datasets nécessaires (intégrés ou mentionnés via un lien).
5. Documentation sur le projet.

## Instructions
1. **Installation** :
   - Clonez le dépôt :
     ```bash
     git clone <url_du_depot>
     ```
   - Installez les dépendances nécessaires (listées dans `requirements.txt`).
     ```bash
     pip install -r requirements.txt
     ```
2. **Utilisation** :
   - Modifiez et exécutez le notebook `main.ipynb` pour analyser les résultats des deux datasets.
   - Ajoutez de nouveaux modèles ou méthodes si nécessaire dans `functions.py`.
3. **Tests** :
   - Exécutez les tests unitaires (si présents) pour valider les fonctions.
     ```bash
     python -m unittest discover
     ```

## Livrable
- Un fichier `.py` contenant toutes les fonctions.
- Un fichier `.ipynb` démontrant l'utilisation des fonctions et les résultats.
- Code et fichiers hébergés dans un dépôt Git privé (GitLab recommandé).

## Bonnes pratiques
- Suivez [ces conseils sur les bonnes pratiques en programmation](https://mikecroucher.github.io/reproducible_ML/).
- Respectez une structure claire dans votre code et utilisez des commentaires pour documenter vos choix.

## Soumission
Envoyez le lien vers votre dépôt Git avant le **20 novembre, 23h** à [elsa.dupraz@imt-atlantique.fr](mailto:elsa.dupraz@imt-atlantique.fr). Assurez-vous que le dépôt est accessible avec les droits nécessaires.

## Ressources utiles
- [Tutoriel Git - OpenClassrooms](https://openclassrooms.com/fr/courses/1233741-gerez-vos-codes-source-avec-git)
- [Visualisation Git - Git Purr](https://github.com/girliemac/a-picture-is-worth-a-1000-words/tree/main/git-purr)
- [Oh My Git!](https://ohmygit.org/)

## Auteurs
- **Encadrante** : Elsa Dupraz ([elsa.dupraz@imt-atlantique.fr](mailto:elsa.dupraz@imt-atlantique.fr))
- **Équipe projet** : [Noms des membres du groupe]
