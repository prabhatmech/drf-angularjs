import environ

project_root = environ.Path(__file__) - 3  
env = environ.Env(DEBUG=(bool, False),)  
CURRENT_ENV = 'dev' # 'dev' is the default environment

# read the .env file associated with the settings that're loaded
env.read_env('./mysite/{}.env'.format(CURRENT_ENV))