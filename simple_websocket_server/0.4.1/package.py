name = "simple_websocket_server"

version = "0.4.1"


description = \
    """
    simple_websocket_server
    """

build_command = False
timestamp = 0


def commands():
    env.PATH.append("{root}")
    env.PYTHONPATH.append("{root}")
   
vcs = "git"