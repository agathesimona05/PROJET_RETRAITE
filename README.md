# Simulateur d'Épargne Long Terme

Projet Python — Dauphine  
Simulation de capitalisation composée avec Monte Carlo.

## Structure du projet

```
simulateur_epargne/
├── simulator.py          # Logique métier (classes + fonctions)
├── app.py                # Serveur Flask (routes API)
├── requirements.txt      # Dépendances
├── templates/
│   └── index.html        # Interface utilisateur
└── tests/
    └── test_simulator.py # Tests unitaires (pytest)
```

## Installation

```bash
# Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## Lancer l'application

```bash
python app.py
# → http://localhost:5000
```

## Lancer les tests

```bash
python -m pytest tests/ -v
```

## Workflow Git recommandé

```bash
# Branche principale : code propre et validé
git checkout main

# Développement sur une branche séparée
git checkout -b feature/ma-fonctionnalite

# ... commits sur la branche ...
git add .
git commit -m "feat: description claire"

# Merge vers main quand c'est prêt
git checkout main
git merge feature/ma-fonctionnalite
```

### Convention de commits

| Préfixe    | Usage                          |
|------------|-------------------------------|
| `feat:`    | Nouvelle fonctionnalité        |
| `fix:`     | Correction de bug              |
| `docs:`    | Documentation                  |
| `refactor:`| Refacto sans changement fonct. |
| `test:`    | Ajout ou modification de tests |

## Concepts Python mobilisés

- **Classes** : `SimulationParams`, `SimulationResult`, `MonteCarloResult`
- **Méthodes spéciales** : `__init__`, `__repr__`, `__str__`, `__len__`
- **Properties** : `@property` pour les valeurs dérivées
- **Type hints** : annotations sur toutes les fonctions et méthodes
- **Gestion d'erreurs** : `ValidationError` (exception personnalisée), `try/except`
- **Docstrings** : format Google sur toutes les fonctions publiques
- **Modularité** : séparation logique métier (`simulator.py`) / serveur (`app.py`)
