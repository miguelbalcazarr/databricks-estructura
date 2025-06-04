
# 🧱 Proyecto Base: Datalakehouse en Azure Databricks

Este repositorio contiene la estructura inicial para un proyecto de arquitectura *Datalakehouse* en Azure Databricks, organizada bajo principios modulares y buenas prácticas de ingeniería de datos.

---

## 📁 Estructura del Proyecto

```
├── .azure-pipelines
│   └── pipeline.yml
├── .gitignore
├── README.md
├── config
│   └── env.json
├── notebooks
│   ├── bootstrap.ipynb
│   └── ingestion
│       └── dominio
│           ├── arquetipos
│           │   └── ntb_arquetipo.ipynb
│           ├── bronze
│           │   └── ntb_bronze.ipynb
│           ├── gold
│           │   └── ntb_gold.ipynb
│           └── silver
│               └── ntb_silver.ipynb
├── requirements.txt
└── src
    ├── __init__.py
    ├── env_utils.py
    ├── ingestion_utils.py
    └── init_env.py
```

---

## 📐 Arquitectura

La solución está dividida en las siguientes capas:

- **Bronze**: Ingesta cruda de datos desde fuentes externas.
- **Silver**: Transformaciones estructuradas y limpieza.
- **Gold**: Datos listos para consumo analítico o exposición a negocio.

Los notebooks están organizados bajo el directorio `notebooks/ingestion/dominio/` según su capa y dominio lógico.

---

## ⚙️ Requisitos Previos

- Azure Databricks (workspace configurado)
- Azure Data Lake Storage (montado como volume o acceso vía SAS/credential passthrough)
- Python 3.9+
- Bibliotecas listadas en `requirements.txt`

---

## 🔧 Configuración

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/databricks-estructura.git
   ```

2. Ajusta las variables de entorno en `config/env.json`.

3. Importa los notebooks al workspace de Databricks.

4. Ejecuta el notebook `notebooks/bootstrap.ipynb` para inicializar el entorno.

---

## 📓 Notebooks

| Notebook             | Descripción                                                  |
|----------------------|--------------------------------------------------------------|
| `ntb_arquetipo.ipynb`| Plantilla base para definir nuevas entidades.                |
| `ntb_bronze.ipynb`   | Ingesta desde fuentes externas hacia la capa Bronze.         |
| `ntb_silver.ipynb`   | Lógica de transformación y limpieza hacia Silver.            |
| `ntb_gold.ipynb`     | Cálculo de métricas y agregaciones finales para la capa Gold.|

---

## 🧰 Scripts

Los scripts en `src/` permiten configurar el entorno e implementar funciones comunes:

- `init_env.py`: Inicialización del contexto de ejecución.
- `env_utils.py`: Lectura y gestión de variables de entorno.
- `ingestion_utils.py`: Funciones auxiliares para ingesta y trazabilidad.

---

## 🚀 CI/CD

Incluye una definición base para automatización en Azure DevOps:  
`.azure-pipelines/pipeline.yml`, adaptable a tus flujos de trabajo.

---
