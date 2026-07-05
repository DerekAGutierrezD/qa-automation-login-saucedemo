from pages.login_page import LoginPage


class TestLogin:

    # Test 1: Login Exitoso (Camino Feliz)
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.load()

        # Usamos las credenciales válidas de la página
        login_page.login("standard_user", "secret_sauce")

        # Verificamos que entramos correctamente al catálogo
        assert login_page.get_title_text() == "Products", "El login falló o no cargó la página de productos"

    # Test 2: Login Fallido (Usuario Bloqueado)
    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.load()

        # Usamos credenciales de un usuario bloqueado
        login_page.login("locked_out_user", "secret_sauce")

        # Verificamos que aparezca el mensaje de error correcto
        error_text = login_page.get_error_message()
        assert "locked out" in error_text, f"Mensaje de error incorrecto: {error_text}"