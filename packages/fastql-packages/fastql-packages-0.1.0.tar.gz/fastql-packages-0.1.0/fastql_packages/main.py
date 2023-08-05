import click
import requests
import os
from os import walk
import re
from zipfile import ZipFile
import shutil
import sys
from .modules import moduleIsNotExist, addModule
import inflect
import datetime
from jinja2 import Environment, FileSystemLoader
import errno

lectEngine = inflect.engine()

jinja_loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
jinja_env = Environment(loader=jinja_loader)

@click.group()
def main():
    pass

@main.command()
@click.argument('query')
@click.option('--version', '-v', default=None)
def create(query, version):
    click.secho('On Request fastapigql info',fg='blue')
    if version == None:
        req_fastql_data = requests.get("https://api.github.com/repos/rachmanzz/fastapigql/releases/latest")
    else:
        req_fastql_data = requests.get("https://api.github.com/repos/rachmanzz/fastapigql/releases/tags/{}".format(version))
    
    # check if failed
    if req_fastql_data.status_code != 200:
        click.secho('download failed or version undefined', fg='red')
        return
    # get return json data
    reqJson = req_fastql_data.json()

    click.echo('please wait ....')
    click.secho('resource download in progress',fg='blue')
    
    get_zip_file = requests.get("https://github.com/rachmanzz/fastapigql/archive/refs/tags/{}.zip".format(reqJson['tag_name']))

    dispositionFile = get_zip_file.headers['content-disposition']
    filename_fastql = re.findall("filename=(.+)", dispositionFile)[0]


    click.echo('file on creating...')

    with open(os.path.join(os.getcwd(), filename_fastql), 'wb') as f:
        f.write(get_zip_file.content)
    
    # Retrieve HTTP meta-data

    # need make sure directory tm is not exits
    temporary_dir = os.path.join(os.getcwd(), '{}-temp'.format(query))

    click.secho('unzipping resource',fg='blue')
    with ZipFile(os.path.join(os.getcwd(), filename_fastql), 'r') as zipObj:
       # Extract all the contents of zip file in different directory
       zipObj.extractall(temporary_dir)
    
    _, dirnames, _ = next(walk(temporary_dir))
    click.echo('move resources ....')
    shutil.move(os.path.join(temporary_dir, dirnames[0]), os.path.join(os.getcwd(), query))
    click.echo('remove temporary directory ....')
    os.rmdir(temporary_dir)
    os.remove(filename_fastql)

    click.secho('=========done=======', fg='green')


@main.command()
@click.argument('query', type=click.Choice(['model', 'migration', 'serialize']))
@click.option('--name', default=None, type=str, required=True)
@click.option('--migration/--no-migration', '-m', default=False, type=bool)
@click.option('--table', '-t', default=None, type=str)
@click.option('--serialize/--no-serialize', '-s', default=False, type=bool)
@click.option('--all/--no-all', '-a', default=False, type=bool)
def make(query, name, migration, table, serialize, all):


    # make sure first character is UpperCase
    FirstCharUpperCase = name[0].upper() + name[1:]
    
    # split character to array
    SplitChar = re.findall('[A-Z][^A-Z]*', FirstCharUpperCase)

    if query == 'model':
        # if moduleIsNotExist('orator'):
        #     addModule('orator')
        #     click.secho('======================================', fg="blue")
        #     click.secho('=                INFO                =', fg="blue")
        #     click.secho('======================================', fg="blue")
        #     click.secho('= please run:                        =', fg="blue")
        #     click.secho('= * "fastql add driver=database"     =', fg="blue")
        #     click.secho('======================================', fg="blue")

        modelName = name.capitalize()
        modelFile = name.lower()
        # migration class UserAccounts
        # migrationName = lectEngine.plural(name.capitalize())
        # table name user_accounts
        # tableName = migrationName.lower()

        
        # check length 
        if len(SplitChar) > 1:
            modelName = ''.join(SplitChar)
            modelFile = '_'.join(SplitChar).lower()
            # migrationName = ''.join(SplitChar[:-1]) + lectEngine.plural(SplitChar[-1])
            # tableName = ('_'.join(SplitChar[:-1]) + "_" + lectEngine.plural(SplitChar[-1])).lower()

        

        model_template = jinja_env.get_template('model.fastql')

        model_output = model_template.render(modelName=modelName)
        current_model_location = os.path.join(os.getcwd(), 'models/', '{}.py'.format(modelFile))
        if not os.path.exists(os.path.dirname(current_model_location)):
            try:
                os.makedirs(os.path.dirname(current_model_location))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(current_model_location, "w") as f:
            f.write(model_output)
        click.secho("model created", fg="blue")

    if query == 'migration' or migration or all:
        migrationName = lectEngine.plural(name.capitalize())
        migrationFile = lectEngine.plural(name.lower())
        tableName = lectEngine.plural(name.lower()) if table == None else table

        if len(SplitChar) > 1:
            migrationName = ''.join(SplitChar[:-1]) + lectEngine.plural(SplitChar[-1])
            if table == None:
                tableName = ('_'.join(SplitChar[:-1]) + "_" + lectEngine.plural(SplitChar[-1])).lower()
            migrationFile = ('_'.join(SplitChar[:-1]) + "_" + lectEngine.plural(SplitChar[-1])).lower()

        timeNow = datetime.datetime.now()
        extend_table_name = "_create_" + migrationFile + "_" + 'table' if table == None else "_" + migrationFile + "_" + 'table'
        migrationFileName = timeNow.strftime("%Y_%m_%d_%H%M%S") + extend_table_name


        migr_template = jinja_env.get_template('migration.fastql') if table == None else jinja_env.get_template('migration-table.fastql')
        migr_output = migr_template.render(table={'nameCapitalize': migrationName, 'nameLower': tableName})

        current_migr_location = os.path.join(os.getcwd(), 'migrations/', '{}.py'.format(migrationFileName))

        if not os.path.exists(os.path.dirname(current_migr_location)):
            try:
                os.makedirs(os.path.dirname(current_migr_location))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(current_migr_location, "w") as f:
            f.write(migr_output)
        click.secho("migration created", fg="blue")

    if query == 'serialize' or serialize or all:
        serializeName = name.capitalize()
        serializeFile = name.lower()
        
        if len(SplitChar) > 1:
            serializeName = ''.join(SplitChar)
            serializeFile = '_'.join(SplitChar).lower()

        serialize_template = jinja_env.get_template('serialize.fastql')

        serialize_output = serialize_template.render(modelName=serializeName)
        current_serialize_location = os.path.join(os.getcwd(), 'app/serializers/', '{}_serialize.py'.format(serializeFile))
        if not os.path.exists(os.path.dirname(current_serialize_location)):
            try:
                os.makedirs(os.path.dirname(current_serialize_location))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(current_serialize_location, "w") as f:
            f.write(serialize_output)
        click.secho("serialize model created", fg="blue")



        
        
        





        


        
        

    