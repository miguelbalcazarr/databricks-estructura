import os
import json
from databricks.sdk.runtime import dbutils

def get_env_path() -> str:
    notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

    if notebook_path.startswith("/Repos/"):
        base_path = "/Workspace" + notebook_path.split("/notebooks")[0]  # full workspace path
        return os.path.join(base_path, "config", "env.json")
    else:
        base_path = "/Workspace" + "/".join(notebook_path.split("/")[:3])
        return os.path.join(base_path, "databricks-estructura", "config", "env.json")

def get_env() -> dict:
    env_path = get_env_path()
    with open(env_path, "r") as f:
        return json.load(f)

def get_scope(key="databricks") -> str:
    return get_env()["scopes"][key]
