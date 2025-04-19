# 📊 Análisis Exploratorio de Marketing – TodoMktg

**Autora:** Elena Sánchez Laulhé  
**Descripción:** Proyecto de análisis exploratorio aplicado a campañas de marketing con el objetivo de detectar patrones, optimizar decisiones y mejorar futuras estrategias comerciales.

---

## 🎯 Objetivos del Proyecto

- Explorar y comprender los datos de campañas de marketing.
- Detectar variables influyentes en la conversión.
- Automatizar tareas de limpieza y visualización mediante scripts modulares.
- Desarrollar un entorno base para futuros análisis predictivos o segmentación de clientes.

---

## 🗂 Estructura del Repositorio

```
marketing_analysis/
│
├── Data/
│   ├── marketing_campaign.csv             # Dataset original
│   ├── mktgeda_cleaning.csv               # Limpieza intermedia
│   ├── mktgeda_datos_limpios.csv          # Dataset final transformado
│   └── mktgeda_metricas.csv               # Métricas agregadas (edad, gasto medio, etc.)
│
├── Jupyters/
│   ├── columnas_categoricas_nulos.ipynb   # Análisis de valores nulos en variables categóricas
│   ├── columnas_numericas.ipynb           # Estadísticas y distribuciones de numéricas
│   ├── eda_preliminar.ipynb               # Notebook principal de análisis exploratorio
│   ├── limpieza.ipynb                     # Proceso completo de limpieza
│   └── marketing.ipynb                    # Notebook de exploración general
│
├── SRC/
│   ├── sp_eda.py                          # Funciones generales de EDA
│   ├── sp_limpieza.py                     # Funciones de limpieza de datos
│   ├── sp_nulos_num.py                    # Tratamiento de nulos en columnas numéricas
│   ├── sp_outliers.py                     # Identificación y tratamiento de outliers
│   └── sp_visual.py                       # Visualizaciones personalizadas
│
├── requirements.txt                       # Dependencias del proyecto
├── .gitignore                             # Exclusión de archivos innecesarios en Git
└── README.md                              # Este documento
```

---

## ⚙️ Librerías y Herramientas

- Python 3.12.5
- Pandas, NumPy
- Seaborn, Matplotlib
- Jupyter Notebook
- Git & GitHub

---

## ▶️ Cómo Ejecutar el Proyecto

1. Clona este repositorio:

   ```bash
   git clone https://github.com/esanchezlaulhe1312/marketing_analysis.git
   cd marketing_analysis
   ```

2. (Opcional) Crea un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Abre los notebooks en Jupyter:
   ```bash
   jupyter notebook
   ```

---

## 📈 Contenido del Análisis

- Análisis de valores nulos y su tratamiento por tipo de variable.
- Detección de outliers mediante métodos gráficos y estadísticos.
- Generación de métricas clave: edad, gasto medio, frecuencia de compra...
- Visualizaciones multivariantes.
- Modularización del flujo de trabajo: funciones reutilizables para futuros datasets.

---

## 🛠 Scripts Destacados

| Script            | Funcionalidad                                             |
| ----------------- | --------------------------------------------------------- |
| `sp_eda.py`       | Funciones generales para análisis exploratorio.           |
| `sp_limpieza.py`  | Procesamiento de datos: nulos, formatos, estandarización. |
| `sp_nulos_num.py` | Detección y tratamiento de nulos en columnas numéricas.   |
| `sp_outliers.py`  | Identificación y gestión de outliers.                     |
| `sp_visual.py`    | Visualizaciones automatizadas con Seaborn y Matplotlib.   |

---

## 🔮 Siguientes Pasos

- Aplicar algoritmos de clustering (K-Means, DBSCAN) para segmentación.
- Crear dashboard interactivo con Streamlit o Power BI.
- Incorporar validación de modelos y comparación de métricas.

---

## 👩‍💻 Autoría

Este proyecto ha sido desarrollado por Elena Sánchez Laulhé como parte de su formación en analítica de datos aplicada al marketing.

GitHub: [@esanchezlaulhe1312](https://github.com/esanchezlaulhe1312)

---

##
