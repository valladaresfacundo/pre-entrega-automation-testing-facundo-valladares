# Pre-entrega: Automatización QA (saucedemo.com)

**Autor:** Facundo Valladares

## Propósito del proyecto

Automatizar flujos básicos de navegación web sobre [saucedemo.com](https://www.saucedemo.com), un sitio demo para prácticas de testing, aplicando lo visto hasta la Clase 8 del curso:

- **Login:** ingresar con credenciales válidas y validar la redirección al inventario.
- **Catálogo:** validar el título de la página, que haya productos visibles, el nombre y precio del primer producto, y que estén los elementos principales de la interfaz (menú, filtro, carrito).

## Tecnologías utilizadas

- **Python 3.13**: lenguaje principal.
- **Selenium WebDriver**: automatización del navegador (Google Chrome).
- **Pytest**: estructura y ejecución de los tests (fixtures en `conftest.py`).
- **pytest-html**: reporte HTML de la ejecución.
- **Git y GitHub**: control de versiones.

## Estructura del proyecto

```
├── tests/
│   ├── test_login.py         # Login exitoso: /inventory.html + "Products" + "Swag Labs"
│   └── test_inventory.py     # Título, productos, nombre/precio del primero, menú y filtros
├── utils/
│   ├── login_page.py         # Page Object del login (con esperas explícitas)
│   └── inventory_page.py     # Page Object del inventario
├── reports/
│   ├── reporte.html          # Reporte HTML generado por pytest-html
│   ├── ejecucion.log         # Log de la última ejecución
│   └── screenshots/          # Capturas automáticas de los tests que fallan
├── conftest.py               # Fixtures: navegador, login y captura en fallos
├── pytest.ini                # Configuración de pytest y de los logs
└── requirements.txt          # Dependencias
```

### Decisiones de diseño

- **Page Object Model:** los localizadores y las acciones de cada pantalla están en `utils/`, así los tests quedan cortos y legibles.
- **Esperas explícitas** (`WebDriverWait` + `expected_conditions`) en lugar de `sleep`, para esperar la carga del formulario y la redirección después del login.
- **Tests independientes:** cada test abre su propio navegador (fixture `driver`) y hace su propio login (fixture `inventario`), así que si uno falla no afecta a los demás.
- **Evidencia automática:** si un test falla, `conftest.py` guarda una captura en `reports/screenshots/` y la adjunta al reporte HTML. Los logs de cada paso se guardan en `reports/ejecucion.log`.

## Instalación

Requisitos: Python 3.10 o superior, Google Chrome y Git. Selenium 4 descarga el driver de Chrome solo, no hace falta instalar ChromeDriver.

```bash
git clone https://github.com/valladaresfacundo/pre-entrega-automation-testing-facundo-valladares.git
cd pre-entrega-automation-testing-facundo-valladares

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / macOS

pip install -r requirements.txt
```

## Cómo ejecutar las pruebas

Todas las pruebas, con reporte HTML:

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

Un archivo puntual:

```bash
pytest tests/test_login.py -v
pytest tests/test_inventory.py -v
```

- `-v`: muestra el nombre y el resultado de cada test.
- `--html=reports/reporte.html`: genera el reporte HTML en la carpeta `reports/`.
- `--self-contained-html`: deja el reporte en un único archivo (con estilos y capturas incluidos), fácil de abrir o compartir.

Al terminar, abrí `reports/reporte.html` en el navegador para ver el resultado. Si algún test falló, ahí mismo aparece su captura de pantalla.
