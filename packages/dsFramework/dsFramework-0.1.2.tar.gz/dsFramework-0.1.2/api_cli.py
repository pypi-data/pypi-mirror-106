import click
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        try:
            cmd_name = ALIASES[cmd_name].name
        except KeyError:
            pass
        return super().get_command(ctx, cmd_name)

@click.group(cls=AliasedGroup)
def cli():
    """DS framework cli"""
# @click.option("--type", prompt="type", help="type of component")
# @click.option("--project_name", prompt="project_name", help="project_name")
# def apis(type, project_name):


@cli.command()
@click.argument('type')
@click.argument('project_name')
def generate(type, project_name):
    """List all cataloged APIs."""
    try:
        f = globals()["generate_%s" % type]
    except Exception as e:
        click.echo('type ' + type + ' not found')
        return
    f(project_name)

ALIASES = {
    "g": generate
}

def generate_model(projectName):
    click.echo('model generated ' + projectName)
    create_project(projectName)

def create_project(projectName):
    create_folder(projectName)
    create_pipeline_file(projectName, 'preprocessor')
    create_pipeline_file(projectName, 'postprocessor')
    create_pipeline_file(projectName, 'labelizer')

def create_folder(projectName):
    global directory
    directory = projectName + '_pipeline'
    if not os.path.exists(directory):
        os.mkdir(directory)

def create_pipeline_file(projectName, pipelineType):
    with open(os.path.join(__location__, 'cli/' + pipelineType + '_template.py'), 'r') as file:
        data = file.read()
        projectNameNoUnderscore = ''.join(elem.capitalize() for elem in projectName.split('_'))
        className = projectNameNoUnderscore + pipelineType.capitalize()
        classNameFotBaseObject = projectNameNoUnderscore + '_' + pipelineType
        data = data.replace('generatedClassName', classNameFotBaseObject)
        data = data.replace('generatedClass',className)
        current_dir = directory + '/' + pipelineType
        if not os.path.exists(current_dir):
            os.mkdir(current_dir)
        new_file = current_dir + "/" + pipelineType + ".py"
        new_init_file = current_dir + "/__init__.py"
        new_init_export = "from " + directory + "." + pipelineType + "." + pipelineType + " import " + className
        if not os.path.exists(new_file):
            f = open(new_file, "w")
            f.write(data)
            f.close()
        create_pipeline_init_file(new_init_file, new_init_export)

def create_pipeline_init_file(init_path, init_export):
    if not os.path.exists(init_path):
        f = open(init_path, "w")
        f.write(init_export)
        f.close()

if __name__ == '__main__':
    cli(prog_name='cli')
