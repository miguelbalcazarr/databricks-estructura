from databricks.sdk.runtime import dbutils
import json
import os
from pathlib import Path

def get_env_path() -> str:
    notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
    base_path = "/".join(notebook_path.split("/")[:3])  # /Workspace/Users/<user>
    return f"{base_path}/databricks-estructura/config/env.json"

def get_env() -> dict:
    env_path = get_env_path()
    with open(env_path) as f:
        return json.load(f)

def get_scope(key: str) -> str:
    env = get_env()
    return env["scopes"][key]
