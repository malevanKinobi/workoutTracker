from django.contrib import admin

# Register your models here.
from .models import TrainingProgram, TrainingDay, TrainingExercise, Exercise, Set

# admin.site.register(TrainingExercise)
# admin.site.register(Exercise)
# admin.site.register(Set)

@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'is_active', 'user']
    list_display_links = ['name']
    search_fields = ['user__username']
    raw_id_fields = ['user']


@admin.register(TrainingDay)
class TrainingDayAdmin(admin.ModelAdmin):
    pass

@admin.register(TrainingExercise)
class TrainingExerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    pass