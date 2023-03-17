from django.urls import path
from apps.views import(
    apps_calendar_view,
    apps_chat_view,
    apps_mailbox_view,
    apps_basicaction_view,
    apps_invoiceaction_view,
    
    apps_projects_list_view,
    apps_projects_overview_view,
    apps_projects_create_view,
    apps_tasks_kanban_view,
    apps_tasks_list_view,
    apps_tasks_details_view,
    
    apps_crypto_transactions_view,
    apps_crypto_buy_sell_view,
    apps_crypto_orders_view,
    apps_crypto_wallet_view,
    apps_crypto_ico_view,
    apps_crypto_kyc_view,
    apps_invoices_list_view,
    apps_invoices_details_view,
    apps_invoices_create_view,
    

    apps_file_manager_view,
    apps_todo_view,
    apps_api_key_view
)
app_name = "apps"

urlpatterns = [
    # Calendar
    path("calendar", view=apps_calendar_view, name="calendar"),
    # Chat
    path("chat", view=apps_chat_view, name="chat"),
    path("mailbox", view=apps_mailbox_view, name="mailbox"),
    path("basicaction", view=apps_basicaction_view, name="basicaction"),
    path("invoiceaction", view=apps_invoiceaction_view, name="invoiceaction"),

    # Projects
    path("projects/list", view=apps_projects_list_view, name="projects.list"),
    path("projects/overview", view=apps_projects_overview_view, name="projects.overview"),
    path("projects/create", view=apps_projects_create_view, name="projects.create"),
    # Tasks
    path("tasks/kanban", view=apps_tasks_kanban_view, name="tasks.kanban"),
    path("tasks/list", view=apps_tasks_list_view, name="tasks.list"),
    path("tasks/details", view=apps_tasks_details_view, name="tasks.details"),
   
    
    # Invoices
    path("invoices/list", view=apps_invoices_list_view, name="invoices.list"),
    path("invoices/details", view=apps_invoices_details_view, name="invoices.details"),
    path("invoices/create", view=apps_invoices_create_view, name="invoices.create"),
    # Support Tickets
    # path("support-tickets/list", view=apps_tickets_list_view, name="tickets.list"),
    # path("support-tickets/update-list/<int:pk>", view=apps_tickets_update_list_view, name="tickets.update_list"),
    # path("support-tickets/delete-list/<int:pk>", view=apps_tickets_delete_list_view, name="tickets.delete_list"),
    # path("support-tickets/details", view=apps_tickets_details_view, name="tickets.details"),

   

    #File Manager
    path("filemanager", view=apps_file_manager_view, name="filemanager"),

    #ToDO
    path("todo", view=apps_todo_view, name="todo"),
    path("api-key", view=apps_api_key_view, name="api_key"),
]
