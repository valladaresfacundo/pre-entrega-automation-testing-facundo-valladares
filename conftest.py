import logging
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver

from utils.inventory_page import InventoryPage
from utils.login_page import LoginPage

logger = logging.getLogger(__name__)

CARPETA_SCREENSHOTS = Path(__file__).parent / "reports" / "screenshots"


@pytest.fixture
def driver():
    """Abre un Chrome nuevo para cada test (los tests son independientes entre si)."""
    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--incognito")
    opciones.add_argument("--window-size=1366,900")
    # Evita el aviso de Chrome "cambia tu contraseña", que tapa la pagina despues del login
    opciones.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })

    logger.info("Abriendo Chrome")
    driver = webdriver.Chrome(options=opciones)
    yield driver
    logger.info("Cerrando Chrome")
    driver.quit()


@pytest.fixture
def inventario(driver):
    """Deja la sesion iniciada y devuelve la pagina de inventario lista para usar."""
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.login()
    pagina = InventoryPage(driver)
    pagina.esperar_carga()
    return pagina


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Si un test falla, saca una captura de pantalla y la adjunta al reporte HTML."""
    outcome = yield
    reporte = outcome.get_result()

    if reporte.when != "call" or not reporte.failed:
        return

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    CARPETA_SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    nombre = f"{item.name}_{datetime.now():%Y%m%d_%H%M%S}.png"
    ruta = CARPETA_SCREENSHOTS / nombre
    driver.save_screenshot(str(ruta))
    logger.error("Test fallido: %s. Captura guardada en %s", item.name, ruta)

    pytest_html = item.config.pluginmanager.getplugin("html")
    if pytest_html is not None:
        extras = getattr(reporte, "extras", [])
        extras.append(pytest_html.extras.image(driver.get_screenshot_as_base64()))
        reporte.extras = extras
