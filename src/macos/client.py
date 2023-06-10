# import objc
# from Foundation import NSUserNotification, NSUserNotificationCenter, NSUserNotificationDefaultSoundName
#
#
# # Note, the following uses the deprecated NSUserNotification.
# class MacOSNotification:
#     def __init__(self, title, subtitle, info_text, sound=True, action_button_text=None):
#         self.title = title
#         self.subtitle = subtitle
#         self.info_text = info_text
#         self.sound = sound
#         self.action_button_text = action_button_text
#
#     def send(self):
#         notification = NSUserNotification.alloc().init()
#         notification.setTitle_(self.title)
#         notification.setSubtitle_(self.subtitle)
#         notification.setInformativeText_(self.info_text)
#
#         if self.action_button_text:
#             notification.setActionButtonTitle_(self.action_button_text)
#             notification.set_hasActionButton_(True)
#
#         if self.sound:
#             notification.setSoundName_(NSUserNotificationDefaultSoundName)
#
#         center = NSUserNotificationCenter.defaultUserNotificationCenter()
#         center.scheduleNotification_(notification)