import logging
import functools

logging.basicConfig(level=logging.DEBUG)

NOTIFY_METHOD_PREFIX = "notifyme_on_"


class NotifyMeException(Exception):
    pass

def add_logger(func=None, *args_parent, **kwargs_parent):

    def wrapper_func(func):
        @functools.wraps(func)
        def inner_func(*args, **kwargs):
            func_name = func.__name__
            logging.info(f"{func_name} executed {args} | {kwargs}")
            return_data = func(*args, **kwargs)
            logging.info(f"{func_name} response {return_data}")
            return return_data

        return inner_func

    if func is not None and callable(func):
        return wrapper_func(func)
    else:
        return wrapper_func


@add_logger
def publish_msg(subject, msg, data_msg=None):
    if data_msg is None:
        data_msg = {}
    return subject.notify(msg, data_msg)


def get_notify_attrs(source):
    all_attr = dir(source)
    return [
        attr for attr in all_attr
        if isinstance(attr, str) and attr.startswith(NOTIFY_METHOD_PREFIX)
    ]

def get_callable_notify_methods(source, notify_attrs=None):
    if notify_attrs is None:
        notify_attrs = get_notify_attrs(source)

    return [
        getattr(source, attr, None)
        for attr in notify_attrs
        if callable(getattr(source, attr, None))
    ]


