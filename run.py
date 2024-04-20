from src.config import create_app, config_dict
from sys import exit
from decouple import config


DEBUG = config("DEBUG", default=True, cast=bool)
get_config_mode = "Development" if DEBUG else "Production"


try:
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit("Error: Invalid <config_mode>. Excepted values [Debug, Production]")

app = create_app(app_config)

if DEBUG:
    app.logger.info("DEBUG      = " + str(DEBUG))
    app.logger.info("Enviroment = " + get_config_mode)
    app.logger.info("SRC        = " + app_config.basedir)


if __name__ == "__main__":
    
    app.run()