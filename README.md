# EET Files Exporter

## Description

**EET Files Exporter** est une application Python avec une interface graphique simple permettant de copier automatiquement des fichiers `.esp` et `.esm` (fichiers de mods de jeux) qui possèdent une sauvegarde (suffixe `.OLD000`). Ce programme va :
- Copier les fichiers trouvés du dossier source vers le dossier de destination
- Renommer les sauvegardes `.OLD000` pour conserver le nom original

L'interface graphique permet à l'utilisateur de sélectionner facilement les dossiers source et de destination, et d'exécuter le traitement en quelques clics.

## Fonctionnalités

- **Interface graphique conviviale** pour sélectionner les dossiers et lancer le traitement.
- **Sélection de dossiers source et destination** via une interface intuitive.
- **Traitement automatique** : copie, suppression et renommage de fichiers spécifiques.
- **Notifications et alertes** pour confirmer les actions et indiquer les erreurs.

## Prérequis

Pour utiliser le programme sans installer Python, un exécutable `.exe` a été créé avec PyInstaller. Cependant, si vous souhaitez exécuter le programme directement à partir du script Python, vous aurez besoin de :

- Python 3.x installé sur votre machine
- Les bibliothèques suivantes (incluses par défaut dans Python) :
  - `tkinter` : Pour l'interface graphique
  - `os` : Pour les interactions avec le système de fichiers
  - `shutil` : Pour les opérations de copie et de suppression de fichiers

## Installation et utilisation

### Utilisation avec l'exécutable (.exe)

1. **Téléchargez l'exécutable** : Téléchargez le fichier `EET_Files_Exporter.exe` fourni, qui est autonome.
2. **Exécutez le fichier** : Double-cliquez sur `EET_Files_Exporter.exe` pour lancer le programme.
3. **Suivez les étapes suivantes** pour utiliser l'application.

### Notes supplémentaires

- Le dossier source idéal est le dossier `./mods/`, qui contient tous les sous-dossiers des mods.
  Le programme recherchera récursivement tous les fichiers compatibles qu'il y trouvera.
