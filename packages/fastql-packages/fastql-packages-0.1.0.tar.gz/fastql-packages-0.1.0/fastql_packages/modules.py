import sys
import subprocess
import sys
import click


def moduleIsNotExist(name):
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed = [r.decode().split('==')[0] for r in reqs.split()]
    if name not in installed:
        return True
    return False

def addModule(name):
    click.secho("install {} ....".format(name), fg='blue')
    subprocess.check_call([sys.executable, "-m", "poetry", "add", name])




    
