# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asynctkinter']

package_data = \
{'': ['*']}

install_requires = \
['asyncgui>=0.5,<0.6']

setup_kwargs = {
    'name': 'asynctkinter',
    'version': '0.2.0',
    'description': "async library that works on top of tkinter's event loop",
    'long_description': '# AsyncTkinter\n\n[Youtube](https://youtu.be/8XP1KgRd3jI)\n\n`asynctkinter` is an async library that saves you from ugly callback-based code,\njust like most of async libraries do.\nLet\'s say you want to do:\n\n1. `print(\'A\')`\n1. wait for 1sec\n1. `print(\'B\')`\n1. wait for a label to be pressed\n1. `print(\'C\')`\n\nin that order.\nYour code would look like this:\n\n```python\ndef what_you_want_to_do(label):\n    bind_id = None\n    print(\'A\')\n\n    def one_sec_later(__):\n        nonlocal bind_id\n        print(\'B\')\n        bind_id = label.bind(\'<Button>\', on_press, \'+\')\n    label.after(1000, one_sec_later)\n\n    def on_press(event):\n        label.unbind(\'<Button>\', bind_id)\n        print(\'C\')\n```\n\nIt\'s barely readable and not easy to understand.\nIf you use `asynctkinter`, the code above will become like this:\n\n```python\nimport asynctkinter as at\n\nasync def what_you_want_to_do(label):\n    print(\'A\')\n    await at.sleep(1000, after=label.after)\n    print(\'B\')\n    await at.event(label, \'<Button>\')\n    print(\'C\')\n```\n\n## Installation\n\n```\npip install asynctkinter\n```\n\n## Pin the minor version\n\nIf you use this module, it\'s recommended to pin the minor version, because if\nit changed, it usually means some breaking changes occurred.\n\n## Usage\n\n```python\nfrom tkinter import Tk, Label\nimport asynctkinter as at\nat.patch_unbind()\n\nroot = Tk()\nlabel = Label(root, text=\'Hello\', font=(\'\', 60))\nlabel.pack()\n\nasync def some_task(label):\n    label[\'text\'] = \'start heavy task\'\n\n    # wait for a label to be pressed\n    event = await at.event(label, \'<Button>\')\n    print(f"pos: {event.x}, {event.y}")\n\n    # wait for 2sec\n    await at.sleep(2000, after=label.after)\n\nat.start(some_task(label))\nroot.mainloop()\n```\n\n#### wait for the completion/cancellation of multiple tasks simultaneously\n\n```python\nasync def some_task(label):\n    from functools import partial\n    import asynctkinter as at\n    sleep = partial(at.sleep, after=label.after)\n    # wait until EITEHR a label is pressed OR 5sec passes\n    tasks = await at.or_(\n        at.event(label, \'<Button>\'),\n        sleep(5000),\n    )\n    print("The label was pressed" if tasks[0].done else "5sec passed")\n\n    # wait until BOTH a label is pressed AND 5sec passes"\n    tasks = await at.and_(\n        at.event(label, \'<Button>\'),\n        sleep(5000),\n    )\n```\n\n#### synchronization primitive\n\nThere is a Trio\'s [Event](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Event) equivalent.\n\n```python\nimport asynctkinter as at\n\nasync def task_A(e):\n    print(\'A1\')\n    await e.wait()\n    print(\'A2\')\nasync def task_B(e):\n    print(\'B1\')\n    await e.wait()\n    print(\'B2\')\n\ne = at.Event()\nat.start(task_A(e))\n# A1\nat.start(task_B(e))\n# B1\ne.set()\n# A2\n# B2\n```\n\n### threading\n\n`asynctkinter` doesn\'t have any I/O primitives like Trio and asyncio do,\nthus threads are the only way to perform them without blocking the main-thread:\n\n```python\nfrom concurrent.futures import ThreadPoolExecuter\nimport asynctkinter as at\n\nexecuter = ThreadPoolExecuter()\n\nasync def some_task(widget):\n    # create a new thread, run a function inside it, then\n    # wait for the completion of that thread\n    r = await at.run_in_thread(\n        thread_blocking_operation, after=widget.after)\n    print("return value:", r)\n\n    # run a function inside a ThreadPoolExecuter, and wait for the completion\n    r = await at.run_in_executer(\n        thread_blocking_operation, executer, after=widget.after)\n    print("return value:", r)\n```\n\nExceptions(not BaseExceptions) are propagated to the caller,\nso you can handle them like you do in synchronous code:\n\n```python\nimport requests\nfrom requests.exceptions import Timeout\nimport asynctkinter as at\n\nasync def some_task(widget):\n    try:\n        r = await at.run_in_thread(\n            lambda: requests.get(\'htt...\', timeout=10), after=widget.after)\n    except Timeout:\n        print("TIMEOUT!")\n    else:\n        print(\'GOT A RESPONSE\')\n```\n\n## Structured Concurrency\n\nBoth `asynctkinter.and_()` and `asynctkinter.or_()` follow the concept of "structured concurrency".\nWhat does that mean?\nThey promise two things:\n\n* The tasks passed into them never outlive them.\n* Exceptions occured in the tasks are propagated to the caller.\n\nRead [this post][njs_sc] if you are curious to the concept.\n\n## Misc\n\n- Why is `patch_unbind()` necessary? Take a look at [this](https://stackoverflow.com/questions/6433369/deleting-and-changing-a-tkinter-event-binding).\n\n[njs_sc]:https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/',
    'author': 'Nattōsai Mitō',
    'author_email': 'flow4re2c@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gottadiveintopython/asynctkinter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
