from pyspark.sql.types import (
    StructType, StructField, IntegerType, LongType, ShortType, FloatType, DoubleType,
    DecimalType, ByteType, StringType, BooleanType, DateType, TimestampType, BinaryType,
    CharType, VarcharType
)
import re

def to_struct_type(schema_json):
    type_map = {
        "integer": IntegerType(),
        "int": IntegerType(),
        "long": LongType(),
        "bigint": LongType(),
        "float": FloatType(),
        "real": FloatType(),
        "double": DoubleType(),
        "string": StringType(),
        "boolean": BooleanType(),
        "date": DateType(),
        "datetime": TimestampType(),
        "timestamp": TimestampType(),
        "timestamp_ltz": TimestampType(),
        "binary": BinaryType(),
        "byte": ByteType(),
        "tinyint": ByteType(),
        "short": ShortType(),
        "smallint": ShortType(),
    }

    def resolve_type(t):
        t_lower = t.lower()
        # decimal(x, y)
        if t_lower.startswith("decimal"):
            match = re.match(r"decimal\((\d+),\s*(\d+)\)", t_lower)
            if match:
                precision, scale = int(match.group(1)), int(match.group(2))
                return DecimalType(precision, scale)
            else:
                return DecimalType(38, 18)
        # char(n), varchar(n): mapear a StringType()
        elif t_lower.startswith("char") or t_lower.startswith("varchar"):
            return StringType()
        else:
            dtype = type_map.get(t_lower)
            if dtype is None:
                raise ValueError(f"Tipo de dato no soportado: {t}")
            return dtype

    fields = [
        StructField(col["name"], resolve_type(col["type"]), col["nullable"])
        for col in schema_json
    ]
    return StructType(fields)

__all__ = ["to_struct_type"]
