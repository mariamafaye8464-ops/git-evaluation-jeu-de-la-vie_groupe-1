#!/bin/sh

# Check that main.py rejects invalid grids and invalid options:
# exit code different from 0, a message on STDERR and nothing on STDOUT.

python_script="${1:-main.py}"

[ -f "$python_script" ] || { echo "Error: $python_script not found" >&2; exit 2; }

temporary_directory="$(mktemp -d)" || exit 2
trap 'rm -rf -- "$temporary_directory"' 0

nb_success=0
nb_failed=0
nb_total_test=0

# expect_error DESCRIPTION GRID_TEXT [OPTIONS...]
# Sends GRID_TEXT on STDIN and checks that the program fails cleanly.
expect_error() {
    description="$1"
    grid_text="$2"
    shift 2

    nb_total_test=$((nb_total_test + 1))
    printf '[%d] %s ... ' "$nb_total_test" "$description"

    printf '%b' "$grid_text" | python3 "$python_script" "$@" \
        >"$temporary_directory/stdout.txt" 2>"$temporary_directory/stderr.txt"
    exit_code=$?

    if [ "$exit_code" -ne 0 ] &&
        [ -s "$temporary_directory/stderr.txt" ] &&
        [ ! -s "$temporary_directory/stdout.txt" ] &&
        ! grep -q "Traceback" "$temporary_directory/stderr.txt"; then
        echo "OK"
        nb_success=$((nb_success + 1))
    else
        echo "FAILED (exit code $exit_code)"
        nb_failed=$((nb_failed + 1))
    fi
}

valid_grid='3\n1 0 1\n0 0 1\n1 0 1\n'

expect_error "grille vide" '' -m 1 -t text
expect_error "taille non entière" 'trois\n1 0 1\n0 0 1\n1 0 1\n' -m 1 -t text
expect_error "taille nulle" '0\n' -m 1 -t text
expect_error "taille négative" '-2\n1 0\n0 1\n' -m 1 -t text
expect_error "lignes manquantes" '3\n1 0 1\n0 0 1\n' -m 1 -t text
expect_error "lignes en trop" '2\n1 0\n0 1\n1 1\n' -m 1 -t text
expect_error "colonne manquante" '3\n1 0 1\n0 0\n1 0 1\n' -m 1 -t text
expect_error "cellule égale à 2" '3\n1 0 1\n0 2 1\n1 0 1\n' -m 1 -t text
expect_error "cellule non numérique" '3\n1 0 1\n0 a 1\n1 0 1\n' -m 1 -t text
expect_error "itération négative" "$valid_grid" -m -1 -t text
expect_error "itération non entière" "$valid_grid" -m deux -t text
expect_error "nb_cells nul" "$valid_grid" -n 0 -t text
expect_error "nb_cells négatif" "$valid_grid" -n -4 -t text
expect_error "seed non entière" "$valid_grid" -s abc -t text
expect_error "type de sortie inconnu" "$valid_grid" -t video
expect_error "option inconnue" "$valid_grid" --vitesse 2

echo
echo "Nb test success: $nb_success / $nb_total_test"

if [ "$nb_failed" -gt 0 ]; then
    exit 1
fi
