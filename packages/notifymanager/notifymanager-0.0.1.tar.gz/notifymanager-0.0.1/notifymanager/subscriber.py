import inspect

from .import utils


class SubscriberMetaClass(type):

    notify_on_args = ["msg", "data_msg"]
    
    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        cls.validate_notify_args(new_class)
        return new_class

    @classmethod
    def validate_notify_args(cls, source):
        notify_methods = utils.get_callable_notify_methods(source)

        for method in notify_methods:
            required_args = inspect.getfullargspec(method).args
            required_args.remove("self")

            if cls.notify_on_args != required_args:
                err_msg = f"{method.__name__} required following args {cls.notify_on_args}"
                raise utils.NotifyMeException(err_msg)


class BaseSubscriber(metaclass=SubscriberMetaClass):

    subsriber_name = None

    def __init__(self, name, *args, **kwargs):
        self.subsriber_name = name

    def __str__(self):
        return f"{self.subsriber_name}"
    
    def get_unique_name(self):
        return f"{self.subsriber_name}_{id(self)}"

    def notifyme_on_http_request(self, msg, data_msg):
        pass

    def notifyme_on_email(self, msg, data_msg):
        pass
