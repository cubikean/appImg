# Image Compressor

Une application GUI Python pour compresser et convertir des images en lot avec de nombreuses options de personnalisation.

## Fonctionnalités

- **Compression d'images en lot** : Traite automatiquement tous les fichiers d'un dossier
- **Conversion de format** : Support pour JPG, WEBP, PNG
- **Redimensionnement intelligent** : Ratio de taille personnalisable ou dimensions fixes
- **Uniformisation 16:9** : Option pour redimensionner toutes les images au format 16:9
- **Correction d'orientation EXIF** : Correction automatique de l'orientation des images
- **Interface graphique intuitive** : Interface simple et conviviale avec tkinter
- **Conversion AVIF** : Bouton dédié pour la conversion en format AVIF (nécessite npx avif)

## Prérequis

- Python 3.x
- tkinter (inclus avec Python)
- Pillow (PIL) : `pip install Pillow`
- Pour la conversion AVIF : Node.js avec le package `avif` installé

## Installation

1. Clonez le repository :
```bash
git clone https://github.com/cubikean/appImg.git
cd appImg
```

2. Installez les dépendances :
```bash
pip install Pillow
```

3. Pour la conversion AVIF (optionnel) :
```bash
npm install -g avif
```

## Utilisation

### Lancement de l'application

```bash
python appImg.py
```

### Interface utilisateur

L'application se compose de trois sections principales :

#### 1. Dossiers (Folders)
- **Folder To Convert** : Sélectionnez le dossier contenant les images à traiter
- **Destination Folder** : Sélectionnez le dossier où sauvegarder les images compressées

#### 2. Format de sortie (Output extension)
- **JPG** : Conversion en format JPEG
- **WEBP** : Conversion en format WebP (recommandé pour le web)
- **PNG** : Conversion en format PNG

⚠️ **Important** : Une seule option de format doit être sélectionnée à la fois.

#### 3. Options (Options)
- **Ratio %** : Pourcentage de redimensionnement (0-100%). Par défaut : 90%
- **Quality %** : Qualité de compression (0-100%). Par défaut : 75%
- **Uniformiser la taille (16/9)** : Redimensionne toutes les images au format 16:9
- **Largeur cible** : Largeur en pixels pour le redimensionnement (défaut : 1920)
- **Hauteur cible** : Hauteur en pixels pour le redimensionnement (défaut : 1080)

### Boutons d'action

- **Create The Survey** : Lance la compression/conversion des images
- **Convertir en AVIF** : Lance la conversion AVIF des fichiers WebP (nécessite npx avif)

## Fonctionnalités détaillées

### Compression intelligente
- Les images sont redimensionnées uniquement si elles sont plus grandes que la taille cible
- Correction automatique de l'orientation EXIF
- Optimisation automatique lors de la sauvegarde

### Gestion des formats
- Support de tous les formats d'image courants (JPG, PNG, WebP, etc.)
- Exclusion automatique des fichiers SVG
- Conversion automatique en RGB si nécessaire

### Redimensionnement
- **Mode ratio** : Redimensionne selon un pourcentage de la taille originale
- **Mode dimensions fixes** : Redimensionne aux dimensions spécifiées
- **Mode uniformisation 16:9** : Redimensionne toutes les images au format 16:9

## Structure des fichiers

```
appImg/
├── appImg.py          # Interface graphique principale
├── util.py           # Fonctions utilitaires de compression
└── README.md         # Ce fichier
```

## Exemples d'utilisation

### Compression simple
1. Sélectionnez le dossier source
2. Sélectionnez le dossier de destination
3. Choisissez WEBP comme format de sortie
4. Laissez les options par défaut (Ratio: 90%, Quality: 75%)
5. Cliquez sur "Create The Survey"

### Redimensionnement au format 16:9
1. Configurez les dossiers source et destination
2. Choisissez le format de sortie souhaité
3. Cochez "Uniformiser la taille (16/9)"
4. Ajustez la largeur et hauteur cibles si nécessaire
5. Lancez la conversion

## Conversion AVIF

Pour utiliser la conversion AVIF :
1. Assurez-vous d'avoir Node.js installé
2. Installez le package avif : `npm install -g avif`
3. Convertissez d'abord vos images en WebP
4. Utilisez le bouton "Convertir en AVIF"

## Dependencies

- **Pillow (PIL)** : Manipulation d'images
- **tkinter** : Interface graphique (inclus avec Python)
- **os** : Gestion des fichiers et dossiers (inclus avec Python)

## Remerciement

Un grand merci à [Alois Goeury](https://github.com/AloisGoeury) pour son aide au projet !



