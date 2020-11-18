# coding=utf-8

"""
    by http://www.fabfile.org/index.html.
    对于小型 Web 项目的部署优化
    默认部署的是 dev 环境下的 dev 分支
"""

import os

from fabric import Connection, task
from invoke import Exit

host_string = 'ubuntu@127.0.0.1'
home_dir = "path/to/project"
python_env = "path/to/env"
ini_file = "path/to/uwsgi.ini"
pid_file = 'path/to/uwsgi.pid'

if not os.path.exists(home_dir):
    raise Exit(f"Aborting for: project path {home_dir} is not exists!")

if not os.path.exists(python_env):
    raise Exit(f"Aborting for: env path {python_env} is not exists!")


@task
def deploy(ctx, branch=None):
    """
    :param ctx: default context for invoke.
    :param env: the environment for project run.
    :param branch: target branch.
    :return:
    """

    if branch is None:
        branch = "dev"

    with Connection(host_string) as conn:
        print("Now Begin to deploy")
        conn.local("cd {home_dir}")

        # stop older worker.
        conn.local(f"kill -9 `cat {pid_file}`")
        print(f"You have stop uwsgi workers on env: {env}")

        # git op
        print("Now fetching latest code.")
        conn.local("git fetch --all -p")
        conn.local(f"git reset --hard origin/{branch}")
        # run
        conn.local(f"{python_env}/bin/uwsgi {ini_file}")
        print(f"You have deployed latest code used Branch is: {ranch}")


@task
def stop(ctx):
    """
    :param ctx: default context for invoke.
    :return:
    """

    with Connection(host_string) as conn:
        print("Now Begin to stop uwsgi workers.")
        conn.local(f"cd {home_dir}")
        # kill current env uwsgi process.
        conn.local(f"kill -9 `cat {pid_file}`")
        print("You have stop uwsgi workers.)


@task
def start(ctx):
    """
    不拉取代码 直接启动
    :param ctx: default context for invoke.
    :return:
    """
    with Connection(host_string) as conn:
        conn.local(f"{python_env}/bin/uwsgi {ini_file}")
        print("You have start uwsgi workers")


@task
def restart(ctx, env='dev'):
    """
    不拉取代码 直接重新启动
    :param ctx: default context for invoke.
    :return:
    """
    stop(ctx)
    start(ctx)
    print("Restart Finish!")
