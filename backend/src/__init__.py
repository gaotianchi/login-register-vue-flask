from typing import cast

import click
from flask import Flask

from .api import account, visitor
from .datebase import User, Visits
from .flaskextens import cors, db
from .settings import get_config
from .utlis import abort


def create_app(environment: str | None = "development") -> Flask:
    config = get_config(environment)
    app = Flask(import_name=__package__)
    app.config.from_object(config)
    db.init_app(app)
    cors.init_app(app)
    app.register_blueprint(account)
    app.register_blueprint(visitor)

    @app.shell_context_processor
    def make_shell_context():  # type: ignore
        return dict(db=db, user=User)

    @app.cli.command("initdb", help="Initialize the database.")
    def initdb():  # type: ignore
        click.confirm(
            "The next operation will delete all data. Whether to continue?",
            abort=True,
        )
        db.drop_all()
        click.echo("Successfully delete all data.")

        db.create_all()
        click.echo("Successfully create all tables.")

        Visits.create()

    @app.errorhandler(Exception)
    def handle_error(e):  # type: ignore
        error = cast(Exception, e)
        message = error.args[0] if error.args else "Error occured."
        return abort(message, target=cast(Exception, e).name)  # type: ignore

    return app
