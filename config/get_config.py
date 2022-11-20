import os
from config.env_config import CONFIG


class GetConfig():
    env = os.environ.get('ENV')

    @staticmethod
    def get_config():
        if GetConfig.env in ['staging', 'prod']:
            return CONFIG[GetConfig.env]
        elif GetConfig.env in None:
            raise Exception('ENV is not set in environment variables')
        else:
            raise Exception(f'In valid env. Please set to :: staging, Prod. Current'
                            f' env is {GetConfig.env} ')



