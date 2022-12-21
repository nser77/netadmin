from django.contrib import admin

class MyModelAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    empty_value_display = "-empty-"
    list_max_show_all = 100
    list_per_page = 25
    save_as_continue = False
    save_on_top = False
