
# 🧱 Proyecto Base: Datalakehouse en Azure Databricks

Este repositorio define una arquitectura base para implementar proyectos Datalakehouse sobre Azure Databricks, con enfoque modular por dominio, separación de ambientes, y buenas prácticas de desarrollo y orquestación.

---

## 📦 **Estructura del Proyecto**

```text
databricks-estructura-main/
├── .azure-pipelines/
├── notebooks/
│   └── ingestion/
│       └── dominio_1/
│           ├── arquetipos/
│           │   └── ntb_arquetipo.ipynb
│           ├── bronze/
│           │   ├── ntb_bronze.ipynb
│           │   └── ntb_create_tables.ipynb
│           ├── gold/
│           │   └── ntb_gold.ipynb
│           ├── silver/
│           │   └── ntb_silver.ipynb
│           ├── tables/
│           │   ├── table_01.py
│           │   └── table_02.py
│           └── test/
│               ├── test_business_rules.py
│               └── test_quality.py
├── src/
│   ├── common/
│   │   ├── env_utils.py
│   │   ├── init_env.py
│   │   └── init_tables.py
│   └── dominio_1/
│       └── ingestion_utils.py
├── requirements.txt
└── README.md
```

---

## ⚡️ Descripción General

- **notebooks/**: Contiene notebooks organizados por dominio y capa del lakehouse (bronze, silver, gold, arquetipos).
- **src/**: Código Python modularizado por dominio, con un espacio `common/` para utilidades globales y un submódulo por cada dominio de negocio.
- **requirements.txt**: Dependencias Python del proyecto.
- **.azure-pipelines/**: Definiciones de CI/CD para Azure DevOps.
- **README.md**: Este documento.
- **.gitignore**: Ignora archivos temporales y sensibles.

---

## 📐 **Principios y Arquitectura**

- **Modularidad:** Cada dominio de negocio tiene sus notebooks, scripts y definición de tablas centralizados.
- **Gobernanza de datos:** Los schemas de cada tabla se definen en Python, con soporte a tipos, PK, particiones, comentarios y nullability.
- **SQL-first:** Las tablas Delta se crean vía `CREATE TABLE ...` usando el esquema y metadatos centralizados, asegurando PK, nulls y particiones desde el catálogo.
- **Orquestación automatizada:** Los notebooks pueden iterar sobre todos los esquemas definidos y crear tablas, comentarios, constraints y particiones de forma robusta.
- **Testing:** Pruebas de calidad y reglas de negocio por dominio.

---

## ⚙️ Requisitos Previos

- Azure Databricks (workspace configurado)
- Python 3.9+
- Azure DevOps (para CI/CD, opcional)
- Las dependencias listadas en `requirements.txt`

---

## 🔧 **Configuración y Primeros Pasos**

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tuusuario/databricks-estructura.git
   ```

2. **Configura tus variables de entorno**  
   Edita `src/common/init_env.py` según tu ambiente o usa variables de entorno Databricks para la conexión.

3. **Define/ajusta tus tablas:**  
   En `notebooks/ingestion/dominio_x/tables/table_XX.py` define cada tabla, ejemplo:

   ```python
   def get_table_info():
       return {
           "schema": [
               {"name": "id", "type": "integer", "nullable": False, "comment": "ID único"},
               {"name": "fecha", "type": "date", "nullable": False},
               {"name": "importe", "type": "decimal(18,4)", "nullable": False, "comment": "Importe de la venta"}
           ],
           "primary_key": ["id"],
           "partition_by": ["fecha"],
           "description": "Tabla bronze de ventas por fecha."
       }
   ```

4. **Ejecuta el notebook de creación de tablas:**  
   Abre y ejecuta `notebooks/ingestion/dominio_x/bronze/ntb_create_tables.ipynb`.  
   Este notebook, usando helpers como `schema_to_sql` y `create_table`, crea y documenta todas las tablas a partir de los esquemas modulares.

---

## ✅ **Buenas Prácticas de Importación (Databricks)**

- **Agrega `src/` al `sys.path` de tu notebook**  
  Esto asegura que puedes importar tus módulos Python personalizados desde cualquier notebook.

- **Usa el bootstrap para inicializar rutas y contexto**  
  Al inicio de cada notebook, ejecuta:

  ```python
  %run ../../../bootstrap
  ```

  Esto añade automáticamente el directorio `src/` al path de Python y prepara el entorno.

- **Importa solo lo necesario según el dominio**
  - Así mantienes tu código claro y modular.
  - Ejemplo recomendado en tu notebook:
    ```python
    from common.env_utils import get_env
    from dominio_1.ingestion_utils import funcion_critica
    ```

- **Evita imports globales o comodines (no uses `from src.* import *`)**
  - Solo importa las funciones, clases o utilidades que realmente necesitas para el notebook/domino en cuestión.

---

## 📝 **Testing de calidad y reglas de negocio**

- Coloca tus notebooks y scripts de pruebas en `notebooks/ingestion/dominio_x/test/`
- Recomendado: usar [Great Expectations](https://greatexpectations.io/) o pruebas personalizadas en PySpark.

---

## 🔁 CI/CD

- El pipeline de Azure DevOps en `.azure-pipelines/pipeline.yml` permite automatizar pruebas, despliegues o validaciones del código.
- Puedes adaptar el pipeline para empaquetar el módulo `src/` como library (`.whl`) para su uso productivo.

---

