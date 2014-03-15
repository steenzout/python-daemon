# Python daemonizer class

This is a Python class that will daemonize your Python script so it can continue running in the background.
It works on Unix, Linux and OS X, creates a PID file and
has standard commands (start, stop, restart) + a foreground mode.

Licensed under [Creative Commons BY 3.0 SA][4].


## Usage

Define a class which inherits from `Daemon` and has a `run()` method
(which is what will be called once the daemonization is completed.

```python
from daemon import Daemon

class pantalaimon(Daemon):
    def run(self):
        # Do stuff
```

Create a new object of your class, specifying where you want your PID file to exist:

```python
pineMarten = pantalaimon('/path/to/pid.pid')
pineMarten.start()
```


## Actions

* `start()` - starts the daemon (creates PID and daemonizes).
* `stop()` - stops the daemon (stops the child process and removes the PID).
* `restart()` - does `stop()` then `start()`.


## Foreground

This is useful for debugging because you can start the code without making it a daemon.
The running script then depends on the open shell like any normal Python script.

To do this, just call the `run()` method directly.

```python
pineMarten.run()
```


## Continuous execution

The `run()` method will be executed just once so
if you want the daemon to be doing stuff continuously
you may wish to use the [sched][1] module to execute code repeatedly ([example][2]).


## Changelog

2014 Mar 15
    - converted module into package
    - added pytest.ini, LICENSE.txt, MANIFEST.in, .gitignore, pip requirements files and setup.py file
    - cleanup of main Daemon class

2010 Aug 13 (David Mytton <david@boxedice.com>
    - fixed unhandled exception if PID file is empty

2009 Mar 11 (David Mytton <david@boxedice.com>)
    - fixed problem with daemon exiting on Python 2.4 (before SystemExit was part of the Exception base)

2009 Jan 23 (David Mytton <david@boxedice.com>)
    - replaced hard coded '/dev/null in __init__ with os.devnull
    - added OS check to conditionally remove code that doesn't work on OS X
    - added output to console on completion
    - tidied up formatting


[1]: http://docs.python.org/library/sched.html
[2]: https://github.com/boxedice/sd-agent/blob/master/agent.py#L226
[3]: http://web.archive.org/web/20131017130434/http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/
[4]: http://creativecommons.org/licenses/by-sa/3.0/
[5]: https://github.com/sandermarechal

