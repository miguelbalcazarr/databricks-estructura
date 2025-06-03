import sys
from .env_utils import get_env, get_scope
from databricks.sdk.runtime import *

env = get_env()
scope = get_scope()

container = dbutils.secrets.get(scope, "secret-env-container")
storage_account = dbutils.secrets.get(scope, "secret-env-storage-account")
environment = dbutils.secrets.get(scope, "secret-env-environment")
path_base = f"abfss://{container}@{storage_account}.dfs.core.windows.net/{environment}"
catalog = "desarrollo"