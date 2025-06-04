import os

def get_env(default: str = "dev") -> str:
    try:
        return dbutils.widgets.get("env")
    except:
        return os.getenv("ENV", default)


def get_scope(service: str = "databricks") -> str:
    env = get_env()
    scope_map = {
        "databricks": {
            "dev": "scope-dev",
            "qa": "scope-qa",
            "prod": "scope-prd"
        },
        "sql": {
            "dev": "sql-scope-dev",
            "qa": "sql-scope-qa",
            "prod": "sql-scope-prod"
        },
    }
    return scope_map[service][env]