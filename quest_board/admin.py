from django.contrib import admin

from .models import Places, Quest

# Register your models here.
@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ["name", "region", "quest_number"]
    search_fields  = ["name"]

    prepopulated_fields = {"slug": ("name",)}

    @admin.display(description="Nombre de quêtes")
    def quest_number(self, places):
        return places.quests.count()

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "difficulty_level", "reward", "place", "is_completed", "created_at"]
    search_field  = ["name"]
    list_filter = ["place", "difficulty_level"]

    prepopulated_fields = {"slug": ("name",)}

    fieldsets = [
        (
            "Présentation de la quête",
            {"fields": ["name", "description", "slug", "place"]}
        ),
        (
            "Difficulté et récompense",
            {"fields": ["difficulty_level", "reward"]}
        ),
        (
            "Statut de la quête",
            {"fields": ["is_completed"]}
        )
    ]