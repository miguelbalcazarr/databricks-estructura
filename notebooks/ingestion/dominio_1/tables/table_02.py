from src.common.init_env import path_base, catalog

def get_table_info():
    info = {
        "domain": "dominio_1",
        "layer": "bronze",
        "entity": "table_02",
        "path": f"{path_base}/bronze/dominio_1/table_02",
        "table": f"{catalog}.bronze.dominio_1_table_02",
        "schema": [
            {"name": "id", "type": "integer", "nullable": False, "comment": "Identificador único"},
            {"name": "importe", "type": "decimal(18,4)", "nullable": False, "comment": "Monto de la venta"},
            {"name": "importe2", "type": "long", "nullable": True, "comment": "Monto de la venta"},
            {"name": "importe3", "type": "tinyint", "nullable": True, "comment": "Monto de la venta"},
            {"name": "fecha", "type": "datetime", "nullable": False, "comment": "Fecha de la transacción"},
            {"name": "producto", "type": "string", "nullable": False, "comment": "Nombre del producto"},
            {"name": "producto1", "type": "varchar(255)", "nullable": False, "comment": "Nombre del producto"},
            {"name": "producto2", "type": "char(5)", "nullable": False, "comment": "Nombre del producto"}
        ],
        "owner": "miguel.balcazar@kyndryl.com",
        "description": "Tabla bronze de dominio_1 (table_02) con datos crudos."
    }

    return info
