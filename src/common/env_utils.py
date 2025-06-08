import os

def get_env() -> str:
    """
    Devuelve el nombre del entorno (dev, uat, prd) desde una variable de entorno.
    """
    return os.getenv("ENV", "prd")  # "prd" es el valor por defecto

def get_scope(key: str = "databricks") -> str:
    """
    Devuelve el nombre del scope de Databricks desde una variable de entorno.
    """
    scopes = {
        "desarrollo": {"databricks": "scope-dev"},
        "calidad": {"databricks": "scope-uat"},
        "produccion": {"databricks": "scope-prd"}
    }
    env = get_env()
    return scopes.get(env, scopes[env]).get(key)

__all__ = ["get_env", "get_scope"]