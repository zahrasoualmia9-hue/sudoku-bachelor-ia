
Presentation (nom: Fatima Zohra Soualmia)

Bonjour,
Je m'appelle Fatima Zohra Soualmia. Je suis candidate pour la 2ème année de Bachelor IA.
Je m'intéresse particulièrement à l'intelligence artificielle parce que j'aime résoudre des problèmes logiques, comprendre les algorithmes et construire des outils qui automatisent des tâches complexes. Le Sudoku est un excellent exercice de raisonnement logique; ce projet m'a permis d'implémenter un algorithme classique (backtracking) et d'organiser le code en programmation orientée objet.

Contenu du dépôt:
- backtracking.py : classe SudokuBacktracker (méthode backtracking)
- main.py : script pour lire une grille depuis un fichier et afficher la solution en terminal
- exemple de fichiers grille: example_pdf.txt, example_easy.txt, example_medium.txt
- run_results.txt : sortie de test exécutée localement ici

Lien GitHub (à créer et coller ici): https://github.com/<ton-username>/sudoku-bachelor-ia

Explication technique (courte):
- La classe initialise la grille à partir d'une liste de 9 lignes.
- La méthode 'is_valid' vérifie la validité d'un chiffre sur une position (ligne, colonne, 3x3).
- La méthode 'solve' applique le backtracking récursif.
- L'affichage distingue les valeurs d'origine des valeurs remplies par l'algorithme (les nouvelles valeurs sont entre crochets).

Résultats des tests: voir run_results.txt dans le dépôt.
