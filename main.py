from platform import system


def notification_text(appname, title, body=None):
    if title is None:
        print("No title or data provided. Closed.")
        exit(1)

    if 'Windows' in system():
        from src.windows.client import NotificationClass
        notifier = NotificationClass(appname)  # Add this as a function arg.
        # todo: Add appname to windows client.
        return notifier.toast(title, body)

    if 'Darwin' in system():
        from src.macos.client import notification_item_text
        return notification_item_text(appname, body, title, sound=False)

#    if 'Linux' in system():
#        from src.linux.client import ...


def notification_button(appname, title, body, button1, argument1, button2=None, argument2=None):
    if button1 is None or argument1 is None:
        print("No button or body data provided. Closed.")
        exit(1)

    if 'Windows' in system():
        from src.windows.client import NotificationClass
        buttons = [{'activationType': 'protocol', 'arguments': argument1, 'content': button1}]
        if button2 is not None and argument2 is not None:
            buttons.append({'activationType': 'protocol', 'arguments': argument2, 'content': button2})
        notifier = NotificationClass(appname)  # Add this as a function arg.
        # todo: Add appname to windows client.
        return notifier.toast(appname, title, body, buttons=buttons)

    if 'Darwin' in system():
        from src.macos.client import notification_item_button
        if button2 is not None and argument2 is not None:
            print("Second notification button is not currently supported by MacOS, defaulting to Cancel.")
            button2 = ""
            argument2 = ""
        return notification_item_button(appname, title, body, button1, argument1)

    # if 'Linux' in system():
    #     from src.linux.client import ...
