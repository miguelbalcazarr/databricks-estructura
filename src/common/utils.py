from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType, DoubleType

def to_struct_type(schema_json):
    type_map = {
        "integer": IntegerType(),
        "string": StringType(),
        "date": DateType(),
        "double": DoubleType()
    }
    
    return StructType([
        StructField(col["name"], type_map[col["type"]], col["nullable"])
        for col in schema_json
    ])

__all__ = ["to_struct_type"]