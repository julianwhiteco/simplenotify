# Don't import modules here. Only do it in the OS fire-off functions.
from platform import system


def notification_text(title, body=None):
    if title is None:
        print("No title or data provided. Closed.")
        exit(1)

    if 'Windows' in system():
        from src.windows.client import NotificationClass
        notifier = NotificationClass('Your App Name Here')  # Add this as a function arg.
        return notifier.toast(title, body)

    if 'Darwin' in system():
        from src.macos.client import MacOSNotification
        toast = MacOSNotification('Hello', 'Subtitle', body, sound=False)
        toast.send()

#    if 'Linux' in system():
#        from src.linux.client import ...


def notification_button(title, body, button1, argument1, button2=None, argument2=None):
    if button1 is None or argument1 is None:
        print("No button or body data provided. Closed.")
        exit(1)

    if 'Windows' in system():
        from src.windows.client import NotificationClass
        buttons = [{'activationType': 'protocol', 'arguments': argument1, 'content': button1}]
        if button2 is not None and argument2 is not None:
            buttons.append({'activationType': 'protocol', 'arguments': argument2, 'content': button2})
        notifier = NotificationClass('Your App Name Here')  # Add this as a function arg.
        return notifier.toast(title, body, buttons=buttons)

    if 'Darwin' in system():
        from src.macos.client import MacOSNotification
        if button2 is not None and argument2 is not None:
            print("Second notification button is not currently supported by MacOS, ignored.")
        interactive = MacOSNotification('Hello', 'Subtitle', 'This is an interactive notification', sound=False, action_button_text='View More')
        interactive.send()

    # if 'Linux' in system():
    #     from src.linux.client import ...
