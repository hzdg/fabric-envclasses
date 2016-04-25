An app that assists with creating Fabric environments, like this::

    class Dev(Env):
        hosts = ['127.0.0.1']
        my_var = 5
        my_other_var = 'whatever'

    dev = Dev.as_task()

This is primarily used by our :code:`hzfabtasks` Python app.
