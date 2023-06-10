import asyncio
from winsdk.windows.data.xml.dom import XmlDocument
from winsdk.windows.foundation import IPropertyValue
from winsdk.windows.ui.notifications import (ToastNotificationManager, ToastNotification, NotificationData, ToastActivatedEventArgs, ToastDismissedEventArgs, ToastFailedEventArgs)

DEFAULT_APP_ID = 'Python'

# todo: Check if we can add an icon too:
# <toast>
#   <visual>
#     <binding template='ToastGeneric'>
#       <image placement="appLogoOverride" hint-crop="circle" src="file://PATH/TO/YOUR/ICON/FILE" />
#       <!-- Rest of your XML here -->
#     </binding>
#   </visual>
# </toast>

API_XML = """
<toast activationType="protocol" launch="http:">
    <visual>
        <binding template='ToastGeneric'></binding>
    </visual>
    <actions>
    </actions>
</toast>
"""


class NotificationClass:
    def __init__(self, app_id=DEFAULT_APP_ID, xml=API_XML):
        self.app_id = app_id
        self.document = XmlDocument()
        self.document.load_xml(xml)
        self.notification = None
        self.result = []

    def set_attribute(self, xpath, name, value):
        attribute = self.document.create_attribute(name)
        attribute.value = value
        self.document.select_single_node(xpath).attributes.set_named_item(attribute)

    def notification_item_text(self, msg):
        if isinstance(msg, str):
            msg = {'text': msg}
        binding = self.document.select_single_node('//binding')
        text = self.document.create_element('text')
        for name, value in msg.items():
            if name == 'text':
                text.inner_text = msg['text']
            else:
                text.set_attribute(name, value)
        binding.append_child(text)

    def notification_item_button(self, button):
        if isinstance(button, str):
            button = {
                'activationType': 'protocol',
                'arguments': 'http:' + button,  # This can possibly be swapped for another URI command, such as an 'update:' command.
                'content': button
            }
        actions = self.document.select_single_node('//actions')
        action = self.document.create_element('action')
        for name, value in button.items():
            action.set_attribute(name, value)
        actions.append_child(action)

    def trigger_arguments(self, _, event):
        e = ToastActivatedEventArgs._from(event)
        user_input = dict([(name, IPropertyValue._from(
            e.user_input[name]).get_string()) for name in e.user_input])
        self.result = {
            'arguments': e.arguments,
            'user_input': user_input
        }
        return self.result

    def send_notification(self, title=None, body=None, on_click=print, duration=None, progress=None, button=None, buttons=[]):
        if isinstance(on_click, str):
            self.set_attribute('/toast', 'launch', on_click)
        if duration:
            self.set_attribute('/toast', 'duration', duration)
        if title:
            self.notification_item_text(title)
        if body:
            self.notification_item_text(body)
        if button:
            self.notification_item_button(button)
        if buttons:
            for button in buttons:
                self.notification_item_button(button)
        self.notification = ToastNotification(self.document)
        if progress:
            data = NotificationData()
            for name, value in progress.items():
                data.values[name] = str(value)
            data.sequence_number = 1
            self.notification.data = data
            self.notification.tag = 'my_tag'
        try:
            notifier = ToastNotificationManager.create_toast_notifier()
        except Exception as e:
            notifier = ToastNotificationManager.create_toast_notifier(self.app_id)
        notifier.show(self.notification)
        return self.notification

    async def toast_async(self, title=None, body=None, on_click=print, duration=None, progress=None, button=None, buttons=[], on_dismissed=print, on_failed=print):
        self.send_notification(title, body, on_click, duration, progress, button, buttons)
        loop = asyncio.get_running_loop()
        futures = []
        activated_future = loop.create_future()
        activated_token = self.notification.add_activated(lambda *args: loop.call_soon_threadsafe(activated_future.set_result, on_click(self.trigger_arguments(*args))))
        futures.append(activated_future)
        dismissed_future = loop.create_future()
        dismissed_token = self.notification.add_dismissed(lambda _, event_args: loop.call_soon_threadsafe(dismissed_future.set_result, on_dismissed(ToastDismissedEventArgs._from(event_args).reason)))
        futures.append(dismissed_future)
        failed_future = loop.create_future()
        failed_token = self.notification.add_failed(lambda _, event_args: loop.call_soon_threadsafe(failed_future.set_result, on_failed(ToastFailedEventArgs._from(event_args).error_code)))
        futures.append(failed_future)
        try:
            _, pending = await asyncio.wait(futures, return_when=asyncio.FIRST_COMPLETED)
            for p in pending:
                p.cancel()
        finally:
            if activated_token is not None:
                self.notification.remove_activated(activated_token)
            if dismissed_token is not None:
                self.notification.remove_dismissed(dismissed_token)
            if failed_token is not None:
                self.notification.remove_failed(failed_token)
            return self.result

    def toast(self, *args, **kwargs):
        return asyncio.run(self.toast_async(*args, **kwargs))
