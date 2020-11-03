from django.contrib import admin
from .models import *


@admin.register(Pansouq)
class PansouqAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'running')
    list_display_links = ('title', 'description', 'running')
    search_fields = ('title', 'description')


class InlineChallenge(admin.TabularInline):
    model = Challenge
    autocomplete_fields = ('creator',)


@admin.register(Souq)
class SouqAdmin(admin.ModelAdmin):
    inlines = [InlineChallenge]
    list_filter = ('related_pansouq',)
    list_display = ('title', 'start_date', 'end_date', 'running')
    list_display_links = ('title', 'start_date', 'end_date', 'running')
    search_fields = ('title',)
    autocomplete_fields = ('related_pansouq',)


class InlineTransaction(admin.TabularInline):
    model = Transaction
    autocomplete_fields = ('participant',)
    extra = 15


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    inlines = [InlineTransaction]
    list_filter = ('related_souq',)
    list_display = ('title', 'creator', 'file')
    list_display_links = ('title', 'creator', 'file')
    search_fields = ('title',)
    autocomplete_fields = ('related_souq', 'creator')


class InlineParticipant(admin.TabularInline):
    model = Participant
    autocomplete_fields = ('user', 'challenging_in')
    extra = 5


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [InlineParticipant]
    list_filter = ('related_pansouq',)
    list_display = ('title', 'related_pansouq', 'score')
    list_display_links = ('title', 'related_pansouq', 'score')
    search_fields = ('title',)
    autocomplete_fields = ('related_pansouq',)


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_filter = ('challenging_in',)
    list_display = ('user', 'team', 'challenging_in')
    list_display_links = ('user', 'team', 'challenging_in')
    search_fields = ('user__first_name', 'user__last_name', 'user__username')
    autocomplete_fields = ('user', 'team', 'challenging_in')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_filter = ('challenge', 'time_received')
    list_display = ('participant', 'challenge', 'time_received')
    list_display_links = ('participant', 'challenge', 'time_received')
    search_fields = ('participant__user__first_name', 'participant__user__last_name', 'participant__user__username')
    autocomplete_fields = ('participant', 'challenge')
# search_fields = ('title',)
# list_editable =
# list_filter =
# def testing(self, obj):
#     return "{},{}".format(obj.x, obj.y)
