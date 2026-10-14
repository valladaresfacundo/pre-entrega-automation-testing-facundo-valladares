import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)

URL_BASE = "https://www.saucedemo.com/"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDA = "secret_sauce"


class LoginPage:
    """Page Object de la pantalla de login de saucedemo.com."""

    INPUT_USUARIO = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def abrir(self):
        logger.info("Navegando a %s", URL_BASE)
        self.driver.get(URL_BASE)
        # Espera explícita: el formulario tiene que estar visible antes de interactuar
        self.wait.until(EC.visibility_of_element_located(self.INPUT_USUARIO))

    def login(self, usuario=USUARIO_VALIDO, password=PASSWORD_VALIDA):
        logger.info("Iniciando sesión con el usuario '%s'", usuario)
        self.wait.until(EC.visibility_of_element_located(self.INPUT_USUARIO)).send_keys(usuario)
        self.wait.until(EC.visibility_of_element_located(self.INPUT_PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.BOTON_LOGIN)).click()
