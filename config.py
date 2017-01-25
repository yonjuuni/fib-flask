class Config(object):

    DEBUG = True

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DEBUG = False


config = {
    'default': Config,
    'production': ProductionConfig,
}
