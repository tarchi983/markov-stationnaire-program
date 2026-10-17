# Calcul de la distribution stationnaire d'une chaîne de Markov

Ce mini-projet calcule la distribution stationnaire d'une chaîne de Markov à
partir de sa matrice de transition.

La fonction principale résout le système :

```text
Pᵀπ = π
Σπᵢ = 1
```

où `P` est la matrice de transition et `π` la distribution stationnaire.

## Prérequis

- Python 3.8 ou supérieur
- NumPy

## Installation

Clonez le dépôt puis installez la dépendance :

```bash
git clone https://github.com/<votre-utilisateur>/<votre-depot>.git
cd markov_stationnaire_program
python -m pip install numpy
```

Pour isoler les dépendances dans un environnement virtuel :

```bash
python -m venv .venv
```

Sous Windows :

```bash
.venv\Scripts\activate
```

Sous macOS/Linux :

```bash
source .venv/bin/activate
```

Puis :

```bash
python -m pip install numpy
```

## Utilisation

### Exécuter l'exemple intégré

```bash
python markov_stationnaire.py
```

Le programme affiche la matrice de transition ainsi que la distribution
stationnaire calculée.

### Utiliser la fonction dans un autre script

```python
from markov_stationnaire import calculer_pi

P = [
    [0.7, 0.2, 0.1],
    [0.4, 0.5, 0.1],
    [0.2, 0.3, 0.5],
]

pi = calculer_pi(P)
print(pi)
```

## Validation effectuée

La fonction vérifie que :

- chaque ligne de `P` a une somme égale à `1` ;
- la solution obtenue contient des probabilités comprises entre `0` et `1`.

Une `ValueError` est levée lorsque ces conditions ne sont pas respectées.

## Structure du projet

```text
markov_stationnaire_program/
├── markov_stationnaire.py
└── README.md
```

## Licence

Ce projet est fourni à des fins pédagogiques. Ajoutez une licence adaptée
avant une éventuelle redistribution publique.
