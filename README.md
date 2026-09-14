# Monitor de Mercado Aurífero ETL 📟

Un monitor automatizado que extrae el precio del oro (XAU/USD) en el mercado Forex, lo almacena localmente en una base de datos relacional y presenta un Dashboard interactivo.

---

## Características Principales ✨
* **Consumo de API:** Extracción de precios y fechas en tiempo real desde GoldAPI.
* **Persistencia:** Los datos transformados son almacenados en una base de datos local SQLite mediante consultas parametrizadas.
* **Lógica de Negocio:** El software detecta los horarios de fin de semana (cierre del mercado en Nueva York). Durante estos periodos, el orquestador pausa las peticiones para optimizar la cuota de la API.
* **Seguridad y Tolerancia a Fallos:** Captura de excepciones en la capa de red y separación de responsabilidades para evitar colapsos del sistema ante caídas de conexión.
* **Presentación:** Un dashboard analítico construido con Streamlit para visualizar la fluctuación de precios, consumiendo la base de datos local y limpiando el eje temporal para una lectura ejecutiva.

## Tecnologías Utilizadas 🛠️
* **Lenguaje:** Python 3.12+
* **Almacenamiento:** Base de datos relacional (SQLite3)
* **Framework Web:** Streamlit

## Librerías y Dependencias 📦
* **`requests`:** Para la comunicación HTTP y extracción de datos de la API.
* **`python-decouple`:** Para la gestión segura de variables de entorno y protección de la API Key.
* **`pandas`:** Para la extracción de la base de datos, limpieza del eje temporal y estructuración tabular de la información.
* **`zoneinfo` y `tzdata`:** Manejo nativo de zonas horarias para sincronizar el orquestador con el horario de apertura y cierre de Wall Street (EST/EDT).

---

## Instalación y Ejecución 🚀

**1. Clona este repositorio:**
```bash
git clone [https://github.com/brandonvht26/etl-monitor-mercado-aurifero.git](https://github.com/brandonvht26/etl-monitor-mercado-aurifero.git)
cd etl-monitor-mercado-aurifero
```

**2. Instala las dependencias necesarias:**
```bash
pip install requests python-decouple pandas streamlit tzdata
```

**3. Configura tus variables de entorno:**
* Crea un archivo llamado `.env` en la raíz del proyecto (puedes guiarte con el archivo `.env.example`).
* Añade tu clave de acceso: `GOLD_API_KEY=tu_clave_aqui`

**4. Ejecuta la aplicación:**
Este proyecto se divide en dos motores. Necesitarás abrir dos terminales diferentes.

* **En la Terminal 1 (Inicia el motor de extracción):**
```bash
python main.py
```
*(Esto iniciará el daemon en segundo plano, el cual evaluará si el mercado está abierto y comenzará a guardar precios).*

* **En la Terminal 2 (Levanta el Dashboard visual):**
```bash
streamlit run dashboard.py
```
*(Esto abrirá automáticamente una pestaña en tu navegador web donde podrás ver la gráfica actualizándose con los nuevos datos).*