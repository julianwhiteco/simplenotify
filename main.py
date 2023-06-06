# Don't import modules here. Only do it in the OS fire-off functions.
from platform import system

# todo: Use https://developer.apple.com/documentation/usernotifications for macos



# define main function,
# define icon as none, button1/button2 as none, if an input is provided in the function (icon=/path/to/icon etc), use it.
# determine platform
# import its /src/platform dir
# Then send code to platform code


# def run_windows(title, subtitle):
#     from src.windows.client import toast
#     # Specify the buttons, icon etc here...
#     toast('Hello Python🐍')
#
#
# def run_macos():
#     from src.macos import client
#     # Specify the buttons, icon etc here...
#
#
# def run_linux():
#     from src.linux import client
#     # Specify the buttons, icon etc here...

def notification_text(title, body=None):
    if 'Windows' in system():
        from src.windows.client import toast
        return toast(title, body)


def notification_button(title, body, button1, argument1, button2=None, argument2=None):
    print("Spawning button notification.")
    if button1 is None or argument1 is None:
        print("No button or body data provided. Closed.")
        exit(1)

    buttons = [{'activationType': 'protocol', 'arguments': argument1, 'content': button1}]

    if button2 is not None and argument2 is not None:
        buttons.append({'activationType': 'protocol', 'arguments': argument2, 'content': button2})

    if 'Windows' in system():
        from win11toast import toast
        return toast(title, body, buttons=buttons)



# def notification_button(title, body, button1, argument):
#     print("Spawning button notification.")
#     if button1 is None or argument is None:
#         print("No button or body data provided. Closed.")
#         exit(1)
#
#     if 'Windows' in system():
#         from src.windows.client import toast
#         return toast(title, body, button={'activationType': 'protocol', 'arguments': argument, 'content': button1})


# print(notification_text("hello", 'weh'))
notification_button("title here", "body", "Button", "https://google.com", "button2", "https://everlastnetworks.com.au")