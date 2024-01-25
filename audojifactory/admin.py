from django.contrib import admin

from audojifactory.models import AudioFile, AudioSegment


class AudioFileAdmin(admin.ModelAdmin):
    list_display = ("artiste", "title", "owner", "terms_condition", "upload_date")
    search_fields = ("artiste", "title", "user__name", "upload_date")
    list_filter = ("upload_date",)


class AudioSegmentAdmin(admin.ModelAdmin):
    list_display = ("transcription", "start_time", "end_time", "duration")
    search_fields = ("audio_file__title", "transcription")
    list_filter = ("audio_file",)

    def duration(self, obj):
        return obj.calculate_duration

    duration.short_description = "Duration (seconds)"


admin.site.register(AudioSegment, AudioSegmentAdmin)
admin.site.register(AudioFile, AudioFileAdmin)