from django.contrib import admin
from django.utils.html import format_html
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'request_type', 'status', 'submission_date', 'expected_resolution_date', 'get_attachment')
    list_filter = ('status', 'request_type', 'submission_date')
    search_fields = ('customer__username', 'customer__email', 'details')
    readonly_fields = ('submission_date',)
    date_hierarchy = 'submission_date'
    list_per_page = 20
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('customer',)
        }),
        ('Request Details', {
            'fields': ('request_type', 'details', 'status', 'attachment')
        }),
        ('Dates', {
            'fields': ('submission_date', 'expected_resolution_date')
        }),
    )

    def get_attachment(self, obj):
        if obj.attachment:
            return format_html('<a href="{}" target="_blank">View Attachment</a>', obj.attachment.url)
        return "No attachment"
    get_attachment.short_description = 'Attachment'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('customer')
        return queryset

    def save_model(self, request, obj, form, change):
        if not change:  # If this is a new object
            obj.status = 'pending'  # Set default status
        super().save_model(request, obj, form, change)
