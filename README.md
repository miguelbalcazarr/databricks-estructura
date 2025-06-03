# 🧱 Azure Databricks - Data Lakehouse Project

Este repositorio contiene una arquitectura modular para un proyecto de ingesta y transformación de datos en un entorno de Data Lakehouse usando Azure Databricks.

---

## 📁 Estructura del Proyecto

```
├── databricks-estructura-main/
│   └── .gitignore
│   └── README.md
│   ├── notebooks/
│   │   └── bootstrap.ipynb
│   │   ├── ingestion/
│   │   │   ├── dominio/
│   │   │   │   ├── arquetipos/
│   │   │   │   │   └── ntb_arquetipo.ipynb
│   │   │   │   ├── bronze/
│   │   │   │   │   └── ntb_bronze.ipynb
│   │   │   │   ├── gold/
│   │   │   │   │   └── ntb_gold.ipynb
│   │   │   │   ├── silver/
│   │   │   │   │   └── ntb_silver.ipynb
│   ├── src/
│   │   └── __init__.py
│   │   └── env_utils.py
│   │   └── init_env.py
│   │   └── ingestion_utils.py
```

---

## 🚀 Uso

1. **Inicializar entorno:**

   Agrega al inicio de tus notebooks:

   ```python
   %run ../bootstrap  # o la ruta relativa correcta
   ```

2. **Importar utilidades:**

   ```python
   from ingestion_utils import funcion_x
   from env_utils import get_env, get_scope
   ```

3. **Configurar entorno:**

   Define el entorno en tu job con un parámetro:

   ```bash
   --env=dev
   ```

---
