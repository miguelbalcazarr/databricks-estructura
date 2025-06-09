from common.init_env import path_base, catalog

def get_table_info():
    info = {
        "domain": "dominio_1",
        "layer": "bronze",
        "entity": "table_01",
        "path": f"{path_base}/bronze/dominio_1/table_01",
        "table": f"{catalog}.bronze.dominio_1_table_01",
        "schema": [
            {"name": "id", "type": "integer", "nullable": False},
            {"name": "fecha", "type": "date", "nullable": False},
            {"name": "producto", "type": "string", "nullable": False}
        ],
        "owner": "miguel.balcazar@kyndryl.com",
        "description": "Tabla bronze de dominio_1 (table_01) con datos crudos."
    }

    return info
