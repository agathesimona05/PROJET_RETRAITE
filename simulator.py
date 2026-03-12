"""
simulator.py
============
Module principal du simulateur d'épargne long terme.

Contient :
  - SimulationParams  : classe de paramètres (validation à l'init)
  - SimulationResult  : classe de résultats avec propriétés calculées
  - simulate_savings  : fonction de simulation déterministe
  - monte_carlo       : fonction de simulation stochastique

Auteurs : Rivière Clément, Poezevara Clarisse, Simona Agathe
Cours   : Python — Projet final, Dauphine
"""

from __future__ import annotations

import math
import random