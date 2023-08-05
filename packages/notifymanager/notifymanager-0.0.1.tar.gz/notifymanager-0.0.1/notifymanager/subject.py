from .import utils


class BaseSubject:

    subject_name = None

    def __init__(self, name):
        self.subject_name = name
        self._subsribers = {}

    def __str__(self):
        return f"{self.subject_name}"

    def subscribe(self, subscriber, notify_attrs=None):
        notify_methods = []
        if not notify_attrs:
            notify_attrs = ["all"]

        if "all" in notify_attrs:
            notify_attrs = utils.get_notify_attrs(subscriber)
        
        notify_methods = utils.get_callable_notify_methods(subscriber, notify_attrs)
        
        if not notify_methods:
            raise utils.NotifyMeException("notify methods not found")

        if subscriber not in self._subsribers:
            self._subsribers[subscriber] = notify_methods
            return True

    def unsubscribe(self, subsriber):
        if subsriber in self._subsribers:
            self._subsribers.pop(subsriber, None)
            return True

    def unsubscribe_all(self):
        self._subsribers.clear()

    def get_all_subscribers(self):
        return self._subsribers

    def notify(self, msg, data_msg=None):
        notify_response = {}
        if not data_msg:
            data_msg = {}

        data_msg["subject_name"] = self.subject_name

        for sub, notify_methods in self._subsribers.items():
            sub_name = sub.get_unique_name()
            notify_response[sub_name] = [
                utils.add_logger(each_method)(msg, data_msg)
                for each_method in notify_methods
            ]
            
        return notify_response