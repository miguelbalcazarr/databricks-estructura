from databricks.sdk.runtime import dbutils
import os, json

def get_env_path() -> str:
    notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
    
    if notebook_path.startswith("/Repos/"):
        base_path = "/".join(notebook_path.split("/")[:4])  # /Repos/<user>/<repo>
    else:
        base_path = "/".join(notebook_path.split("/")[:3])  # /Workspace/Users/<user>

    return f"{base_path}/config/env.json"

# def get_env() -> dict:
#     env_path = get_env_path()
#     with open(env_path) as f:
#         return json.load(f)
    
def get_env() -> dict:
    env_path = get_env_path()
    json_str = dbutils.fs.head(env_path, 4096)
    return json.loads(json_str)

def get_scope(key: str) -> str:
    return get_env()["scopes"][key]