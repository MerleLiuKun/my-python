# coding=utf-8

"""
    by http://www.fabfile.org/index.html.
    对于小型 Web 项目的部署优化
    默认部署的是 dev 环境下的 dev 分支
    说明：
        1. 分为两个部署环境(可以跨机器), dev 与 prod
        2. 不同环境下使用不同的 虚拟环境 (可共用)
"""

import os

from fabric import Connection, task
from invoke import Exit

host_string = 'ubuntu@127.0.0.1'


@task
def deploy(ctx, env='dev', branch=None):
    """
    :param ctx: default context for invoke.
    :param env: the environment for project run.
    :param branch: target branch.
    :return:
    """
    home_dir = '~/projects/{}/project_name'.format(env)
    python_env = '~/.pyenv/versions/project_{}_env'.format(env)
    if not os.path.exists(home_dir):
        raise Exit("Aborting for: file path is not exists! Check the target param.")

    if branch is None:
        branch = 'dev'

    if env == 'prod' and branch != 'master':
        raise Exit("Aborting for: Production must be master branch.")

    with Connection(host_string) as conn:
        print("Now Begin to deploy")
        conn.local("cd {}".format(home_dir))

        # stop older worker.
        pid_file = 'var/pids/uwsgi.pid'
        conn.local("kill -9 `cat {}`".format(pid_file))
        print("You have stop uwsgi workers on env: {}".format(env))

        # git op
        print("Now fetching latest code.")
        conn.local("git fetch --all -p")
        conn.local("git reset --hard origin/{}".format(branch))
        # run
        conn.local("{}/bin/uwsgi myapp.ini ".format(python_env))
        print("You have deployed latest code on env: {0}, Used Branch is: {1}".format(env, branch))


@task
def stop(ctx, env='dev'):
    """
    :param ctx: default context for invoke.
    :param env: the environment for project run.
    :return:
    """
    home_dir = '~/projects/{}/project_name'.format(env)
    if not os.path.exists(home_dir):
        raise Exit("Aborting for: file path is not exists! Check the target param.")

    with Connection(host_string) as conn:
        print("Now Begin to stop uwsgi workers.")
        conn.local("cd {}".format(home_dir))
        # kill current env uwsgi process.
        pid_file = 'var/pids/uwsgi.pid'
        conn.local("kill -9 `cat {}`".format(pid_file))
        print("You have stop uwsgi workers on env: {}".format(env))


@task
def start(ctx, env='dev'):
    """
    不拉取代码 直接启动
    :param ctx: default context for invoke.
    :param env: the environment for project run.
    :return:
    """
    home_dir = '~/projects/{}/project_name'.format(env)
    python_env = '~/.pyenv/versions/project_{}_env'.format(env)
    if not os.path.exists(home_dir):
        raise Exit("Aborting for: file path is not exists! Check the target param.")
    with Connection(host_string) as conn:
        conn.local("{}/bin/uwsgi myapp.ini".format(python_env))
        print("You have start uwsgi workers on env: {0}".format(env))


@task
def restart(ctx, env='dev'):
    """
    不拉取代码 直接重新启动
    :param ctx: default context for invoke.
    :param env: the environment for project run.
    :return:
    """
    stop(ctx, env)
    start(ctx, env)
    print("Restart Finish!")
