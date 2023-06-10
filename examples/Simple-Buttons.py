from src.windows.client import NotificationClass
# todo: change the above to reflect a pypi name.
# The following follows the current WIP library codebase, and will be updated to reflect the final library.


def notification_button(title, body, button1, argument1, button2=None, argument2=None):
    if button1 is None or argument1 is None:
        print("No button or body data provided. Closed.")
        exit(1)

    buttons = [{'activationType': 'protocol', 'arguments': argument1, 'content': button1}]

    if button2 is not None and argument2 is not None:
        buttons.append({'activationType': 'protocol', 'arguments': argument2, 'content': button2})

    notifier = NotificationClass('Your App Name Here')  # Pass 'Everlast App' as app_id
    return notifier.toast(title, body, buttons=buttons)


# Simple text notification:
notification_button("Notification query.", "This demonstration prompts the user to make a choice between two buttons. You can intercept user selection by interpreting exit data.", "Cancel", "NULL", "Update Now", "https://google.com.au")
