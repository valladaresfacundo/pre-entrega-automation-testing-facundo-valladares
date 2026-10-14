import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)


class InventoryPage:
    """Page Object de la página de inventario (catálogo de productos)."""

    TITULO_SECCION = (By.CLASS_NAME, "title")
    LOGO = (By.CLASS_NAME, "app_logo")
    PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
    PRECIO_PRODUCTO = (By.CLASS_NAME, "inventory_item_price")
    BOTON_MENU = (By.ID, "react-burger-menu-btn")
    FILTRO = (By.CLASS_NAME, "product_sort_container")
    CARRITO = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def esperar_carga(self):
        """Espera explícita: la URL cambia a /inventory.html y aparece el título 'Products'."""
        self.wait.until(EC.url_contains("/inventory.html"))
        self.wait.until(EC.text_to_be_present_in_element(self.TITULO_SECCION, "Products"))
        logger.info("Página de inventario cargada: %s", self.driver.current_url)

    def titulo_seccion(self):
        return self.driver.find_element(*self.TITULO_SECCION).text

    def texto_logo(self):
        return self.driver.find_element(*self.LOGO).text

    def productos(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCTOS))

    def nombre_y_precio_del_primero(self):
        primero = self.productos()[0]
        nombre = primero.find_element(*self.NOMBRE_PRODUCTO).text
        precio = primero.find_element(*self.PRECIO_PRODUCTO).text
        logger.info("Primer producto: '%s' - %s", nombre, precio)
        return nombre, precio

    def listar_productos(self):
        """Devuelve [(nombre, precio), ...] de todos los productos del catálogo."""
        lista = []
        for producto in self.productos():
            nombre = producto.find_element(*self.NOMBRE_PRODUCTO).text
            precio = producto.find_element(*self.PRECIO_PRODUCTO).text
            lista.append((nombre, precio))
        return lista

    def elemento_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
