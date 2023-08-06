
import typer
import uvicorn
from fastapi_migrations.cli import MigrationsCli
# pylint: disable=unused-import
from task_manager.common_api.Api import CommonApi, conf_common_api
from task_manager.common_utils.common import str_to_bool

common_cli: typer.Typer = typer.Typer()


common_cli.add_typer(MigrationsCli())


@common_cli.command()
def runserver() -> None:
    is_debug = str_to_bool(conf_common_api.get('fastapi', 'DEBUG'))
    host = conf_common_api.get('fastapi', 'HOST')
    port = int(conf_common_api.get('fastapi', 'PORT'))
    uvicorn.run('task_manager.common_cli:CommonApi', host=host, port=port, reload=is_debug, debug=is_debug)

