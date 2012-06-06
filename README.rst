Fabric is cool. But writing tasks to set environment variables isn't so great::

    @task
    def dev():
        env.hosts = ['127.0.0.1']
        env.my_var = 5
        env.my_other_var = 'whatever'

This project lets you use a more declarative syntax::

    class Dev(Env):
        hosts = ['127.0.0.1']
        my_var = 5
        my_other_var = 'whatever'

    dev = Dev.as_task()
