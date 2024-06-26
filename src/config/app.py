from importlib import import_module
from flask import Flask

def register_blueprints(app):

    routes = ("default","profissional","cliente", "atuacao", "portfolio", "avaliacao")

    try:
        for blueprint in routes:
            module = import_module("src.routes.{}".format(blueprint))
            app.register_blueprint(module.blueprint)

    except ModuleNotFoundError:
        app.logger.info("Rotas ou blueprints invalidas")

    except AssertionError:
        app.logger.info("Uma ou mais rotas estão em conflito")

    except Exception as e:
        app.logger.info("Erro Interno")
        app.logger.info(e)



def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    return app