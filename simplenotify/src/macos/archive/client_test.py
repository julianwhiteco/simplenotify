# from mac_notifications import client
#
# def send_notification():
#     client.create_notification(title="Meeting starts now!", subtitle="Team Standup")
#
# if __name__ == "__main__":
#     send_notification()
#
#
#
#
#
#
#
#
#
#


import objc
from Foundation import NSUserNotification, NSUserNotificationCenter


# Text notification
def send_notification(title, subtitle, info_text, delay=0, sound=False):
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(info_text)
    notification.setDeliveryDate_(NSDate.dateWithTimeInterval_sinceDate_(delay, NSDate.date()))
    notification.setSoundName_("NSUserNotificationDefaultSoundName" if sound else None)

    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)


# Interactive notification
from Foundation import NSDistributedNotificationCenter
objc.loadBundleFunctions(Foundation, globals(), [("NSUserNotificationActivationTypeActionButtonClicked", b"I")])

def notify(title, subtitle, info_text, delay=0, sound=False, userInfo={}, actionButton=None):
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(str(title))
    notification.setSubtitle_(str(subtitle))
    notification.setInformativeText_(str(info_text))
    notification.setUserInfo_(userInfo)
    if actionButton:
        notification.setActionButtonTitle_(str(actionButton))
    else:
        notification.setHasActionButton_(False)
    notification.setDeliveryDate_(Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date()))
    NSUserNotificationCenter.defaultUserNotificationCenter().setDelegate_(AppDelegate.alloc().init())
    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)


send_notification("Hello, world!", "Subtitle", "This is a notification", delay=1, sound=True)