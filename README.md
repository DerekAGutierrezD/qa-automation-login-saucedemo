# 🤖 QA Automation – Login Testing (Sauce Demo)

## 📋 ¿Qué es esto?
Framework de automatización de pruebas UI desarrollado con Python, 
Selenium y Pytest sobre saucedemo.com, cubriendo los flujos críticos 
de autenticación de usuarios.

---

## 🎯 Objetivo
Automatizar la validación del módulo de login para reducir el tiempo 
de pruebas de regresión en cada nuevo despliegue, asegurando que los 
flujos de autenticación funcionen correctamente.

---

## 🔍 Alcance
**Incluido:**
- Login exitoso con credenciales válidas
- Login fallido con usuario bloqueado

**Excluido:**
- Pruebas de otros módulos (carrito, checkout)
- Pruebas de rendimiento o carga

---

## 🛠️ Tecnologías utilizadas
- **Python** – Lenguaje de programación
- **Selenium WebDriver** – Automatización de navegador
- **Pytest** – Framework de ejecución de pruebas
- **Page Object Model (POM)** – Patrón de diseño para código mantenible
- **WebDriver Manager** – Gestión automática del driver de Chrome

---

## 📁 Estructura del proyecto
qa-automation-login-saucedemo/

├── pages/

│   └── login_page.py      # Page Object del módulo de login

├── tests/

│   └── test_login.py      # Casos de prueba automatizados

├── conftest.py             # Configuración y fixtures de Pytest

└── README.md

---

## 🧪 Casos de prueba

| ID | Escenario | Resultado esperado |
|----|-----------|-------------------|
| TC-001 | Login con credenciales válidas | Redirige a página de productos |
| TC-002 | Login con usuario bloqueado | Muestra mensaje de error "locked out" |

---

## 🔑 Decisiones clave
- Se implementó POM para separar la lógica de navegación de los 
  casos de prueba, facilitando el mantenimiento ante cambios en la UI.
- Se usó WebDriver Manager para eliminar la dependencia manual 
  del chromedriver, haciendo el proyecto portable.
- Se eligió saucedemo.com por ser un entorno de pruebas estable 
  y reproducible por cualquier evaluador.

---

## 📊 Resultados
- 2 casos de prueba automatizados cubriendo flujos críticos de login
- Tiempo de ejecución: ~10 segundos por suite completa
- Código modular y escalable para agregar nuevos módulos fácilmente

---

## 🔄 ¿Qué mejoraría después?
- Agregar caso de prueba para campos vacíos y credenciales incorrectas
- Integrar con GitHub Actions para ejecución automática en cada push

---

## ▶️ ¿Cómo ejecutar?
```bash
# Instalar dependencias
pip install selenium pytest webdriver-manager

# Ejecutar pruebas
pytest tests/test_login.py -v
```
