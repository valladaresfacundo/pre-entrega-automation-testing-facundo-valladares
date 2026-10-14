import logging

from utils.inventory_page import InventoryPage

logger = logging.getLogger(__name__)


def test_titulo_de_la_pagina_es_correcto(inventario):
    """Verificar que el título de la página de inventario sea correcto."""
    assert inventario.driver.title == "Swag Labs", \
        f"Título de la pestaña incorrecto: '{inventario.driver.title}'"
    assert inventario.titulo_seccion() == "Products", \
        f"Título de la sección incorrecto: '{inventario.titulo_seccion()}'"


def test_hay_productos_visibles(inventario):
    """Comprobar que existan productos visibles en la página (al menos uno)."""
    productos = inventario.productos()
    logger.info("Cantidad de productos visibles: %d", len(productos))
    assert len(productos) > 0, "No hay productos visibles en el inventario"


def test_nombre_y_precio_del_primer_producto(inventario):
    """Listar el nombre y el precio del primer producto y validar que tengan datos."""
    nombre, precio = inventario.nombre_y_precio_del_primero()

    assert nombre.strip() != "", "El primer producto no tiene nombre"
    assert precio.startswith("$"), f"El precio no tiene el formato esperado ($xx.xx): '{precio}'"
    assert float(precio.replace("$", "")) > 0, f"El precio debería ser mayor a 0: '{precio}'"

    for nombre_producto, precio_producto in inventario.listar_productos():
        logger.info("  - %s: %s", nombre_producto, precio_producto)


def test_elementos_de_la_interfaz_presentes(inventario):
    """Validar que el menú, el filtro y el carrito estén presentes y visibles."""
    assert inventario.elemento_visible(InventoryPage.BOTON_MENU), "El menú (hamburguesa) no está visible"
    assert inventario.elemento_visible(InventoryPage.FILTRO), "El filtro de productos no está visible"
    assert inventario.elemento_visible(InventoryPage.CARRITO), "El ícono del carrito no está visible"
