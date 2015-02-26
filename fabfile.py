from fabric.api import *

env.hosts = ['104.236.45.141',]
env.user = 'root'
env.password = ''

def deploy():
    code_dir = '/home/agendati'
    with cd(code_dir):
        run("git pull")