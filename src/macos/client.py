import subprocess


def notification_item_text(title, text, subtitle=None, sound=True):
    sound_arg = 'sound name "Submarine"' if sound else ''
    subtitle_arg = f'subtitle "{subtitle}"' if subtitle else ''
    applescript = f'display notification "{text}" with title "{title}" {subtitle_arg} {sound_arg}'
    subprocess.run(["osascript", "-e", applescript])


def notification_item_button(title, message, button_text, url):
    dialog_applescript = f'''
    tell app "System Events"
        display dialog "{message}" buttons {{"Cancel", "{button_text}"}} with title "{title}"
    end tell
    '''

    dialog_result = subprocess.run(
        ["osascript", "-e", dialog_applescript],
        capture_output=True,
        text=True
    )

    # Check if the button was clicked...
    if button_text in dialog_result.stdout:
        url_applescript = f'open location "{url}"'
        subprocess.run(["osascript", "-e", url_applescript])


# Example usage:
notification_item_button(title="Software Update Available", message="A new version of the software is available. Would you like to update now?", button_text="Update", url="https://www.example.com/update")

# Example usage:
notification_item_text("Hello", "This is a simple toast prompt", "Subtitle")
