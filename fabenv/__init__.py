from fabric.api import env
from fabric.tasks import Task
from string import Formatter


class Env(object):

    @classmethod
    def as_task(cls, task_name=None):
        instance = cls()

        if not task_name:
            task_name = getattr(instance, 'Meta', None)
        if not task_name:
            task_name = cls.__name__.lower()

        class EnvTask(Task):
            name = task_name

            def run(self):
                for attr in dir(instance):
                    if not attr.startswith('_'):
                        setattr(env, attr, getattr(instance, attr))

        return EnvTask()


class EnvAdapter(object):
    def __init__(self, instance):
        self.instance = instance

    def __getitem__(self, key):
        try:
            return getattr(self.instance, key)
        except AttributeError:
            raise KeyError


class T(object):
    """
    Used to create a template string property. Usage::

        class MyEnv(Env):
            var_one = '1'
            var_two = T('The value of var_one is {var_one}')

    Accessing the attribute from the class will yield the template string::

        MyEnv.var_two >> 'The value of var_one is {var_one}'

    Accessing from an instance will yield the result of interpolating the
    template string with other values from the instance::

        MyEnv().var_two >> 'The value of var_one is 1'

    """

    def __init__(self, template_string):
        self.template_string = template_string

    def __get__(self, instance, owner):
        if instance is None:
            return self.template_string
        else:
            return Formatter().vformat(self.template_string, [],
                    EnvAdapter(instance))
