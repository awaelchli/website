from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from subscription.models import NewsletterSubscription


class NewsletterSubscriptionAdmin(ModelAdmin):
    model = NewsletterSubscription
    menu_label = 'Subscriptions'
    menu_icon = 'fa-users'
    menu_order = 301
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('email', 'created_at')
    search_fields = ('email', )


modeladmin_register(NewsletterSubscriptionAdmin)
