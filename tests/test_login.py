from utils.inventory_page import InventoryPage
from utils.login_page import LoginPage


def test_login_exitoso_redirige_al_inventario(driver):
    """Login con credenciales válidas: debe redirigir a /inventory.html y mostrar 'Products' / 'Swag Labs'."""
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.login("standard_user", "secret_sauce")

    inventario = InventoryPage(driver)
    inventario.esperar_carga()  # espera explícita de la redirección

    assert "/inventory.html" in driver.current_url, \
        f"No redirigió al inventario. URL actual: {driver.current_url}"
    assert inventario.titulo_seccion() == "Products", \
        f"El título de la sección no es 'Products': '{inventario.titulo_seccion()}'"
    assert inventario.texto_logo() == "Swag Labs", \
        f"El logo no dice 'Swag Labs': '{inventario.texto_logo()}'"
