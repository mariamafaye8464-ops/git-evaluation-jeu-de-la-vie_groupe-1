# Jeu de la vie – Groupe 1

Simulation en Python du [jeu de la vie de Conway](https://fr.wikipedia.org/wiki/Jeu_de_la_vie), réalisée pour l'évaluation du module outils de développement logiciel.

## Installation

Le programme n'a besoin que de **Python 3.8 ou plus récent** et de sa bibliothèque standard : aucun paquet `pip` n'est à installer. Les scripts de test s'exécutent avec `sh` dans un terminal Unix. Pour produire les vidéos, il faut aussi `ffmpeg` (vidéo de simulation) et Gource (vidéo de l'historique du dépôt).

### Ubuntu ou Debian

```sh
sudo apt update
sudo apt install python3 git ffmpeg gource
```

### macOS

Avec [Homebrew](https://brew.sh/) :

```sh
brew install python git ffmpeg gource
```

### Windows

Dans PowerShell, avec [winget](https://learn.microsoft.com/fr-fr/windows/package-manager/winget/) :

```powershell
winget install --id Git.Git -e
winget install 9NQ7512CXL7T
winget install --id Gyan.FFmpeg -e
winget install --id acaudwell.Gource -e
```

`Git.Git` installe Git et **Git Bash**, le terminal qui fournit `sh` pour les scripts de test. `9NQ7512CXL7T` est le gestionnaire d'installation officiel de Python. Fermez puis rouvrez le terminal, et lancez la suite des commandes dans **Git Bash**. Si `python3` n'est pas trouvé, lancez `py install --configure` et acceptez l'ajout au `PATH`.

Dans Git Bash, une grille aléatoire (sans grille envoyée sur l'entrée standard) se lance avec `winpty` : `winpty python3 main.py -n 20 -m 5`.

Autre possibilité : installer [WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install) avec `wsl --install` dans PowerShell ouvert en administrateur, redémarrer l'ordinateur, puis suivre la partie [Ubuntu ou Debian](#ubuntu-ou-debian) dans Ubuntu.

### Récupérer le projet

```sh
git clone https://github.com/mariamafaye8464-ops/git-evaluation-jeu-de-la-vie_groupe-1.git
cd git-evaluation-jeu-de-la-vie_groupe-1
```

### Vérifier l'installation

```sh
python3 --version              # Python 3.8 ou plus récent
ffmpeg -version
gource --version
sh check_script_options.sh     # Nb test success: 6 / 6
sh check_tests.sh              # Nb test success: 74 / 74
sh check_errors.sh             # Nb test success: 16 / 16
```


## Exécution

Toutes les commandes se lancent depuis la racine du dépôt.

### Sans option : 21 images dans `outputs`

```bash
$ python3 main.py
Generation of 21 images in directory outputs
```

### Grille lue sur l'entrée standard

```bash
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -t text
iteration: 1
0 1 0
0 0 1
0 1 0
```

### Bords périodiques

```bash
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -p -t text
iteration: 1
0 0 0
0 0 0
0 0 0
```

### Grille invalide

```bash
$ printf '2\n1 0\n0 2\n' | python3 main.py -t text
Error: line 3, column 2: invalid cell '2', only 0 and 1 are allowed
```

## Arguments

Le programme se règle avec les options ci-dessous. Chaque option existe sous une forme courte et une forme longue, qui font exactement la même chose. La commande `python3 main.py --help` affiche ce résumé dans le terminal.

| Option courte | Option longue | Rôle | Valeur par défaut |
|---|---|---|---|
| `-n N` | `--nb_cells N` | taille de la grille aléatoire (N cellules par côté) | `10` |
| `-m N` | `--max_iterations N` | numéro de la dernière génération calculée | `20` |
| `-s N` | `--seed N` | graine du générateur aléatoire | `42` |
| `-o DOSSIER` | `--output_directory DOSSIER` | dossier où sont écrites les images (créé s'il n'existe pas) | `outputs` |
| `-t TYPE` | `--output_type TYPE` | `image` : un fichier PNG par génération ; `text` : la dernière génération sur la sortie standard | `image` |
| `-p` | `--periodic` | bords périodiques : la grille se referme sur elle-même, comme un tore | désactivée |
| `-h` | `--help` | affiche l'aide et quitte | — |

Valeurs acceptées :

- `-n` : un entier strictement positif (`-n 0` ou `-n abc` sont refusés).
- `-m` : un entier positif ou nul. La génération initiale porte le numéro `0` : avec `-m 20`, le programme produit 21 générations, de `0` à `20`.
- `-s` : n'importe quel entier, négatif, nul ou positif. La même graine avec la même taille donne toujours la même grille.
- `-t` : uniquement `image` ou `text`.
- `-n` et `-s` ne servent qu'à la grille aléatoire : quand une grille est envoyée sur l'entrée standard, ils n'ont aucun effet.

Une option invalide affiche l'usage du programme et un message d'erreur sur la sortie d'erreur, puis le programme s'arrête avec le code de sortie `2` (voir les exemples de la section Exécution).

Les formes longues rendent une commande plus lisible :

```bash
$ python3 main.py --nb_cells 4 --seed 3 --max_iterations 2 --output_type text --periodic
iteration: 2
0 0 1 0
0 0 0 0
0 0 1 0
0 0 0 0
```

La commande courte équivalente est `python3 main.py -n 4 -s 3 -m 2 -t text -p`.

## Vidéos

### Simulation du jeu de la vie

Vidéo sur YouTube : [Simulation du jeu de la vie, graine 4200](https://www.youtube.com/watch?v=KoEg7bJJm7Q)

La vidéo montre l'évolution d'une grille aléatoire de 50 cellules par côté, créée avec la graine `4200`, de la génération `0` à la génération `2000`, avec des bords fixes (sans l'option `-p`). Avec la même graine, `main.py` produit exactement les mêmes images à chaque exécution.

Commandes utilisées, depuis la racine du dépôt :

```bash
mkdir -p outputs/video-seed-4200
python3 main.py --nb_cells 50 --max_iterations 2000 --seed 4200 \
  --output_type image --output_directory outputs/video-seed-4200
ffmpeg -y -framerate 20 -start_number 0 \
  -i outputs/video-seed-4200/grid_%04d.png -frames:v 2001 \
  -vf "scale=1080:1080:flags=neighbor,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
  -c:v libx264 -pix_fmt yuv420p -movflags +faststart \
  outputs/video-seed-4200/game-of-life.mp4
```

- `main.py` écrit 2001 images, de `grid_0000.png` à `grid_2000.png`, et affiche `Generation of 2001 images in directory outputs/video-seed-4200`.
- `ffmpeg` assemble ces images dans l'ordre, à 20 images par seconde : la vidéo dure 1 minute et 40 secondes.
- L'option `-vf` agrandit chaque image deux fois sans flou, puis ajoute des bandes noires sur les côtés. La vidéo est ainsi au format 16:9 (1920 × 1080), et YouTube la publie comme une vidéo classique plutôt que comme un Short.
- Les images et la vidéo restent dans `outputs/`, qui n'est pas suivi par Git (voir `.gitignore`).
- Sous Windows, ces commandes fonctionnent telles quelles dans Git Bash. Si `python3 main.py` attend sans rien afficher, appuyez sur Ctrl+C et relancez la commande avec `winpty` devant.

### Historique du dépôt avec Gource

_À compléter par Nizar (PR 14)._

## Intégration continue

Les scripts de test du projet sont lancés automatiquement par GitHub Actions, à chaque `push` et à chaque Pull Request. Le workflow est décrit dans le fichier [`.github/workflows/tests.yml`](.github/workflows/tests.yml).

[![Tests](https://github.com/mariamafaye8464-ops/git-evaluation-jeu-de-la-vie_groupe-1/actions/workflows/tests.yml/badge.svg)](https://github.com/mariamafaye8464-ops/git-evaluation-jeu-de-la-vie_groupe-1/actions/workflows/tests.yml)

Le workflow s'exécute sous Ubuntu avec Python 3.12. Il récupère le contenu du dépôt, puis lance depuis sa racine :

- `sh check_script_options.sh` : vérifie les options du programme (6 tests) ;
- `sh check_tests.sh` : compare la sortie texte du programme aux générations attendues du dossier `tests/`, avec des bords fixes et périodiques (74 tests) ;
- `sh check_errors.sh` : vérifie que les entrées invalides sont refusées avec un message d'erreur (16 tests).

Si l'un des scripts se termine avec un code de sortie différent de `0`, le job `tests` échoue. Comme la branche `main` est protégée, GitHub refuse alors de fusionner la Pull Request.

Exécution réussie des scripts : [Tests sur `main` après la fusion de la PR #15](https://github.com/mariamafaye8464-ops/git-evaluation-jeu-de-la-vie_groupe-1/actions/runs/43579095118).

## Auteurs

_À compléter par Mariama (PR 13)._

## Liens utiles

_À compléter par Mariama (PR 13)._
