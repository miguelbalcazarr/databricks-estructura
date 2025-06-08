
# 🧱 Proyecto Base: Datalakehouse en Azure Databricks

Este repositorio define una arquitectura base para implementar proyectos Datalakehouse sobre Azure Databricks, con enfoque modular por dominio, separación de ambientes, y buenas prácticas de desarrollo y orquestación.

---

## 📐 Arquitectura de Carpetas

```
├── .azure-pipelines/
│   └── pipeline.yml
├── .gitignore
├── README.md
├── notebooks/
│   ├── bootstrap.ipynb
│   └── ingestion/
│       └── dominio_1/
│           ├── arquetipos/
│           │   └── ntb_arquetipo.ipynb
│           ├── bronze/
│           │   └── ntb_bronze.ipynb
│           ├── gold/
│           │   └── ntb_gold.ipynb
│           └── silver/
│               └── ntb_silver.ipynb
├── requirements.txt
└── src/
    ├── __init__.py
    ├── common/
    │   ├── __init__.py
    │   ├── env_utils.py
    │   └── init_env.py
    └── dominio_1/
        ├── __init__.py
        └── ingestion_utils.py
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

## 🚀 Buenas Prácticas de Importación (Databricks)

1. **Agrega `src/` al path en tu notebook**  
   En cada notebook, al inicio, incluye:

   ```python
   %run ../../../bootstrap
   ```

2. **Importa solo lo que necesitas según el dominio**  
   Ejemplo:

   ```python
   from common.env_utils import get_env
   from dominio_1.ingestion_utils import funcion_critica
   ```

---

## 🧩 Modularidad por Dominio

- **common/**: Utilidades globales, helpers y funciones compartidas.
- **dominio_xx/**: Lógica específica del dominio, por ejemplo reglas de negocio, funciones de ingesta, etc.
- Puedes agregar más dominios en `src/` siguiendo este patrón:  
  `src/dominio_clientes/`, `src/dominio_productos/`, etc.

---

## ⚙️ Requisitos Previos

- Azure Databricks (workspace configurado)
- Python 3.9+
- Azure DevOps (para CI/CD, opcional)
- Las dependencias listadas en `requirements.txt`

---

## 🛠️ Configuración recomendada

1. **Clona este repositorio** en tu entorno Databricks.
2. **Asegúrate de tener tu cluster con Python 3.9+**.
3. **Instala las dependencias** si usas entorno local.
4. **Orienta tu equipo a trabajar con notebooks organizados y modulares.**

---

## 🔁 CI/CD

- El pipeline de Azure DevOps en `.azure-pipelines/pipeline.yml` permite automatizar pruebas, despliegues o validaciones del código.
- Puedes adaptar el pipeline para empaquetar el módulo `src/` como library (`.whl`) para su uso productivo.

---

