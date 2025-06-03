import json
import os

def get_env():
    env_path = "/Workspace/Users/miguel.balcazar@kyndryl.com/databricks-estructura/config/env.json"
    with open(env_path) as f:
        return json.load(f)

def get_scope(key: str) -> str:
    env = get_env()
    return env["scopes"][key]