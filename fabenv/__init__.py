from fabric.api import env
from fabric.tasks import Task


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
