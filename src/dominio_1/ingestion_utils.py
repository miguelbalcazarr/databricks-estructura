from src.common.init_env import path_base

def primera_funcion() -> str:
    return path_base

def segunda_funcion() -> str:
    return "segunda funcion"

def tercera_funcion() -> str:
    return "tercera funcion"

__all__ = ["primera_funcion", "segunda_funcion", "tercera_funcion"]