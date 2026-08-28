from django.db import models

# Create your models here.
class Places(models.Model):
    name = models.CharField("Nom", max_length=100, unique=True)
    region = models.TextField("Région d'Hyrule")
    image_url = models.URLField("adresse complète", max_length=500, default="")
    slug = models.SlugField("identifiant url", max_length=100, unique=True)

    class Meta:
        verbose_name = "Lieu"
        verbose_name_plural = "Lieux"
        ordering  =["name"]

    def __str__(self):
        return self.name

class Quest(models.Model):
    name = models.CharField("Nom de la quête", max_length=200)
    description = models.TextField("Description")
    reward = models.PositiveIntegerField("Récompense")
    is_completed = models.BooleanField("État de la quête", default=False)
    place = models.ForeignKey(Places, verbose_name="Lieu de la quête", on_delete=models.PROTECT, related_name="quests")
    created_at = models.DateTimeField("Créée le", auto_now_add=True)

    class DifficultyLevel(models.TextChoices):
        EASY = "EASY", "Facile",
        MODERATE = "MODERATE", "Moyen",
        HARD = "HARD", "Difficile"

    difficulty_level = models.CharField(max_length=20, choices=DifficultyLevel.choices, default=DifficultyLevel.EASY)

    slug = models.SlugField("identifiant url", max_length=100, unique=True)

    class Meta:
        verbose_name = "Quête"
        verbose_name_plural = "Quêtes"
        ordering = ["name"]

    def __str__(self):
        return self.name