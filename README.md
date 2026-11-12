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

_À compléter par Nizar (PR 11)._

## Vidéos

### Simulation du jeu de la vie

_À compléter par Aliou (PR 12)._

### Historique du dépôt avec Gource

_À compléter par Nizar (PR 14)._

## Intégration continue

_À compléter par Mariama (PR 13)._

## Auteurs

_À compléter par Mariama (PR 13)._

## Liens utiles

_À compléter par Mariama (PR 13)._
