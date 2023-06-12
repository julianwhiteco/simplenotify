import subprocess


def send_notification(title, text, subtitle=None, sound=True):
    sound_arg = 'sound name "Submarine"' if sound else ''
    subtitle_arg = f'subtitle "{subtitle}"' if subtitle else ''

    applescript = f'display notification "{text}" with title "{title}" {subtitle_arg} {sound_arg}'

    subprocess.run(["osascript", "-e", applescript])


# Example usage:
send_notification("Hello", "This is a simple toast prompt", "Subtitle")
