# Évaluation modulaire
## Hyrule Quest Board

Application Django permettant de consulter les quêtes et les lieux du royaume d'Hyrule, avec un chatbot thématique (ZeldaBot). Projet réalisé dans le cadre de l'évaluation modulaire du même nom.

## Administration

Interface accessible sur `/admin/`.

```
login : Zelda
pass  : mysuperpassword
```
## Architecture du projet

```
hyrule_quest_board/   configuration du projet (settings, urls racine)
pages/                page d'accueil
quest_board/          quêtes et lieux
bot/                  ZeldaBot, le chatbot
templates/global/     template de base commun (base.html, _header.html, _footer.html)
static/               CSS commun et assets (icônes SVG, illustrations de région)
```

## Modèles de données

**Places**
- `name` — nom du lieu
- `region` — région d'Hyrule
- `image_url` — illustration du lieu
- `slug`

**Quest**
- `name`, `description`
- `reward` — récompense en rubis
- `is_completed`
- `place` — `ForeignKey` vers `Places` (`related_name="quests"`)
- `difficulty_level` — choix `EASY` / `MODERATE` / `HARD`
- `slug`, `created_at`

Une quête appartient à un seul lieu ; un lieu peut avoir plusieurs quêtes.

## Fonctionnalités

- Page d'accueil : statistiques calculées depuis la base (nombre de quêtes, disponibles, terminées)
- Liste des quêtes, filtrable (Toutes / Disponibles / Terminées) via un paramètre GET
- Détail d'une quête
- Liste des lieux, avec nombre de quêtes par lieu (calculé via `annotate(Count(...))`)
- Détail d'un lieu, listant ses quêtes
- ZeldaBot : chatbot répondant aux questions sur l'univers de Zelda

## Le chatbot ZeldaBot

- Modèle exécuté en local via Ollama (`gemma3:4b`)
- Prompt système cadrant le rôle du bot (ton d'un sage d'Hyrule) et limitant les réponses à l'univers de Zelda

Prérequis pour le faire fonctionner : Ollama installé et lancé localement, avec le modèle récupéré au préalable (`ollama pull gemma3:4b`).

## Décisions techniques

- **Une seule app pour les quêtes et les lieux** (`quest_board`), plutôt que deux apps séparées : les modèles `Quest` et `Places` sont étroitement liés (`ForeignKey`, recherche croisée), une séparation aurait surtout ajouté de la friction sans bénéfice réel.
- **ZeldaBot dans sa propre app** (`bot`) : aucune dépendance aux modèles de `quest_board`, fonctionnement autonome.
- **Un template de base commun** (`global/base.html`), avec header et footer inclus séparément, pour éviter de répéter la structure HTML sur chaque page.
- **Une seule feuille de style** (`static/css/styles.css`) partagée par toutes les pages.
- **Design inspiré de l'identité visuelle de Zelda** (parchemin, bois, dorures), sans reprise d'éléments protégés (logos, personnages) — le thème s'appuie sur des motifs génériques d'univers fantastique plutôt que sur des visuels du jeu.
