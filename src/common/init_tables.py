from .init_env import catalog
from databricks.sdk.runtime import spark

def schema_to_sql(schema_json):
    """
    Convierte el schema JSON a una definición SQL compatible con CREATE TABLE,
    incluyendo tipos, nullabilidad y comentarios por columna.
    """
    def type_to_sql(col_type):
        t = col_type.lower()
        if t.startswith("decimal"):
            return t.replace(" ", "").upper()
        elif t.startswith("varchar"):
            return t.replace(" ", "").upper()
        elif t.startswith("char"):
            return t.replace(" ", "").upper()
        elif t in ["integer", "int"]:
            return "INT"
        elif t == "long":
            return "BIGINT"
        elif t == "double":
            return "DOUBLE"
        elif t == "float":
            return "FLOAT"
        elif t == "string":
            return "STRING"
        elif t == "boolean":
            return "BOOLEAN"
        elif t in ["date"]:
            return "DATE"
        elif t in ["datetime", "timestamp"]:
            return "TIMESTAMP"
        else:
            return t.upper()

    cols = []
    for col in schema_json:
        line = f"{col['name']} {type_to_sql(col['type'])}"
        line += " NOT NULL" if not col.get("nullable", True) else ""
        if col.get("comment"):
            line += f" COMMENT '{col['comment']}'"
        cols.append(line)
    return ",\n    ".join(cols)

def create_table(
    database_name: str,
    table_name: str,
    table_schema: str,
    table_location: str,
    table_comment: str,
    partition=None,
    primary_key=None
):
    sql_query = f"""
    CREATE TABLE IF NOT EXISTS {catalog}.{database_name}.{table_name}
    ({table_schema}
    """

    if primary_key:
        sql_query += f", PRIMARY KEY ({primary_key})"

    sql_query += f"""
    )
    USING DELTA
    LOCATION '{table_location}'
    COMMENT '{table_comment}'
    """

    if partition:
        sql_query += f"PARTITIONED BY ({partition})"

    sql_query += """
    TBLPROPERTIES (
        'delta.autoOptimize.optimizeWrite' = 'True',
        'delta.tuneFileSizesForRewrites' = 'True',
        'delta.autoOptimize.autoCompact' = 'True',
        'vorder.enabled' = 'True'
    )
    """

    spark.sql(sql_query)
    
    print(f"Tabla {catalog}.{database_name}.{table_name} creada.")


__all__ = ["schema_to_sql", "create_table"]

