# Pre-entrega: Automatizacion QA -(saucedemo.com) facundo valladares

**Autor:** Facundo Valladares

## Proposito del proyecto
Proyecto de automatizacion de pruebas realizado con Python, Selenium WebDriver y Pytest

El objetivo del proyecto es automatizar distintas pruebas funcionales de una aplicacion web

- **Login:** ingresar con credenciales válidas y validar la redirección al inventario.
- **Catálogo:** validar el título de la página, que haya productos visibles, el nombre y precio del primer producto, y que estén los elementos principales de la interfaz (menú, filtro, carrito).

## Tecnologías usadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Git

## Instalación de dependencias
A continuación se detalla la forma de instalar las distintas dependencias:
- Python: descargar el ejecutable desde https://www.python.org/downloads/
- Selenium WebDriver: ejecutar en terminal de VS Code "pip install selenium"
- Pytest: ejecutar en terminal de VS Code "pip install pytest"
- Pytest HTML: ejecutar en terminal de VS Code "pip install pytest-html"
- Git: descargar el ejecutable desde https://git-scm.com/


### Decisiones de diseño

- **Page Object Model:** los localizadores y las acciones de cada pantalla están en `utils/`, así los tests quedan cortos y legibles.
- **Esperas explícitas** (`WebDriverWait` + `expected_conditions`) en lugar de `sleep`, para esperar la carga del formulario y la redirección después del login.
- **Tests independientes:** cada test abre su propio navegador (fixture `driver`) y hace su propio login (fixture `inventario`), así que si uno falla no afecta a los demás.
- **Evidencia automática:** si un test falla, `conftest.py` guarda una captura en `reports/screenshots/` y la adjunta al reporte HTML. Los logs de cada paso se guardan en `reports/ejecucion.log`.

## Instalación

- git init
- git commit -m "v1.0"
- git branch -M main
- git remote add origin https://github.com/valladaresfacundo/pre-entrega-automation-testing-facundo-valladares.git
- git push -u origin main

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
