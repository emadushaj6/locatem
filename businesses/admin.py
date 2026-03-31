from django.contrib import admin
from .models import Category, Plan, Business, BusinessRequest


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'category', 'plan',
                    'city', 'is_active', 'is_featured')
    list_filter = ('category', 'plan', 'is_active', 'is_featured')
    search_fields = ('name', 'owner__username', 'city', 'phone', 'email')
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Owner & Status', {
            'fields': ('owner', 'is_active', 'is_featured')
        }),
        ('Business Info', {
            'fields': ('name', 'slug', 'category', 'plan', 'description', 'image', 'external_link')
        }),
        ('Contact & Location', {
            'fields': ('phone', 'email', 'address', 'city')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(BusinessRequest)
class BusinessRequestAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'name', 'email', 'phone', 'created_at')
    search_fields = ('business_name', 'name', 'email', 'phone')
    readonly_fields = ('created_at',)
