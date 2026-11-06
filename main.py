"""Simulation du jeu de la vie de Conway.

Utilisation : python3 main.py --help
"""

import argparse
import random
import sys
from pathlib import Path

from lib import write_grid


class GameOfLifeError(Exception):
    """Erreur d'utilisation ou de données : message affiché sur STDERR."""


# --------------------------------------------------------------------------
# Arguments de la ligne de commande (Seynabou)
# --------------------------------------------------------------------------

def positive_int(value):
    """Convertir value en entier strictement positif (option --nb_cells)."""
    raise NotImplementedError("positive_int : tâche de Seynabou")


def non_negative_int(value):
    """Convertir value en entier positif ou nul (option --max_iterations)."""
    raise NotImplementedError("non_negative_int : tâche de Seynabou")


def parse_arguments(argv=None):
    """Lire les options -n, -m, -s, -o, -t et -p avec argparse."""
    raise NotImplementedError("parse_arguments : tâche de Seynabou")


# --------------------------------------------------------------------------
# Lecture de la grille sur STDIN (Nizar)
# --------------------------------------------------------------------------

def parse_grid(text):
    """Transformer le texte reçu sur STDIN en grille carrée de 0 et de 1."""
    lines = text.strip().splitlines()
    if not lines:
        raise GameOfLifeError("empty grid: nothing was read on standard input")

    size_text = lines[0].strip()
    try:
        size = int(size_text)
    except ValueError:
        raise GameOfLifeError(
            f"line 1: the grid size must be an integer, got '{size_text}'"
        )
    if size <= 0:
        raise GameOfLifeError(
            f"line 1: the grid size must be strictly positive, got {size}"
        )

    rows = lines[1:]
    if len(rows) != size:
        raise GameOfLifeError(
            f"malformed grid: expected {size} rows, got {len(rows)}"
        )

    grid = []
    for line_number, line in enumerate(rows, start=2):
        cells = line.split()
        if len(cells) != size:
            raise GameOfLifeError(
                f"line {line_number}: expected {size} cells, got {len(cells)}"
            )
        row = []
        for column, cell in enumerate(cells, start=1):
            if cell not in ("0", "1"):
                raise GameOfLifeError(
                    f"line {line_number}, column {column}: invalid cell "
                    f"'{cell}', only 0 and 1 are allowed"
                )
            row.append(int(cell))
        grid.append(row)
    return grid


def read_grid_from_stdin():
    """Lire tout STDIN et renvoyer la grille correspondante."""
    try:
        text = sys.stdin.read()
    except (OSError, UnicodeDecodeError) as error:
        raise GameOfLifeError(f"cannot read standard input: {error}")
    return parse_grid(text)


# --------------------------------------------------------------------------
# Grille aléatoire (Seynabou)
# --------------------------------------------------------------------------

def generate_random_grid(nb_cells, seed):
    """Créer une grille aléatoire reproductible de nb_cells x nb_cells."""
    raise NotImplementedError("generate_random_grid : tâche de Seynabou")


# --------------------------------------------------------------------------
# Calcul des générations (Aliou)
# --------------------------------------------------------------------------

def count_live_neighbors(grid, row, col, periodic):
    """Compter les voisines vivantes de la cellule (row, col)."""
    raise NotImplementedError("count_live_neighbors : tâche d'Aliou")


def next_generation(grid, periodic):
    """Calculer la génération suivante sans modifier grid."""
    raise NotImplementedError("next_generation : tâche d'Aliou")


def iterate_generations(grid, max_iterations, periodic):
    """Produire les couples (numéro, grille) de 0 à max_iterations."""
    raise NotImplementedError("iterate_generations : tâche d'Aliou")


# --------------------------------------------------------------------------
# Sortie texte (Seynabou)
# --------------------------------------------------------------------------

def format_grid(grid):
    """Écrire la grille en texte : cellules séparées par des espaces."""
    raise NotImplementedError("format_grid : tâche de Seynabou")


def write_text_output(generations):
    """Afficher sur STDOUT uniquement la dernière génération."""
    raise NotImplementedError("write_text_output : tâche de Seynabou")


# --------------------------------------------------------------------------
# Sortie images (El Amine)
# --------------------------------------------------------------------------

def write_image_outputs(generations, output_directory):
    """Écrire un fichier grid_XXXX.png par génération."""
    raise NotImplementedError("write_image_outputs : tâche d'El Amine")


# --------------------------------------------------------------------------
# Programme principal (Mariama)
# --------------------------------------------------------------------------

def load_initial_grid(args):
    """Lire la grille sur STDIN si elle est fournie, sinon la générer."""
    if sys.stdin.isatty():
        return generate_random_grid(args.nb_cells, args.seed)
    return read_grid_from_stdin()


def main():
    """Enchaîner lecture des options, grille initiale, calcul et sortie."""
    args = parse_arguments()
    try:
        grid = load_initial_grid(args)
        generations = iterate_generations(
            grid, args.max_iterations, args.periodic
        )
        if args.output_type == "text":
            write_text_output(generations)
        else:
            write_image_outputs(generations, args.output_directory)
    except GameOfLifeError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
