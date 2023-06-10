from src.windows.client import NotificationClass
# todo: change the above to reflect a pypi name.
# The following follows the current WIP library codebase, and will be updated to reflect the final library.


def notification_text(title, body=None):
    notifier = NotificationClass('Your App Name Here')  # Set this to whatever application name you'd like.
    return notifier.toast(title, body)


# Simple text notification:
notification_text("Notification title.", "We weren't able to securely connect you. This may be due to a network issue.")
