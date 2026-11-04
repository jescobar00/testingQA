# testingQA

https://gamma.app/docs/PRE-ENTREGA-Automatizacion-QA-yugshe4z3od8i8w?mode=doc
Propósito del proyecto
Tecnologías utilizadas
Instrucciones de instalación de dependencias
Comando para ejecutar las pruebas (por ejemplo: pytest -v --html=reporte.html)

Reporte HTML generado por Pytest con resultados de la ejecución.
Evidencias adicionales: capturas de pantalla automáticas en caso de fallos y logs de ejecución.

Funcionalidad esperada:
Los casos de prueba deben ejecutarse correctamente en el sitio saucedemo.com
Las validaciones deben ser claras y específicas para cada paso
El código debe ser legible y estar bien organizado
Los tests deben ser independientes entre sí (la falla de uno no debe afectar a los demás)

Estructura mínima de carpetas:
tests/
utils/ (funciones auxiliares)

Generar reporte en HTML de las pruebas realizadas:
pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html

### dependencies

```python
pip install selenium
```

```python
pip install pytest
```

```python
pip install pytest-html
```

### to run test cases file

```python
pytest
```

## Test cases

#### Automatización de Login:

[test_login.py](./preentrega/tests/test_login.py)

```
    Navegar a la página de login de saucedemo.com
    Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
    Validar login exitoso verificando que se haya redirigido a la página de inventario
    Criterios mínimos:
    Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”.
```

#### Navegación y verificación del catálogo:

[test_products.py](./preentrega/tests/test_productos.py)

```
Navegación y verificación del catálogo: (Clases 6 a 8)
  Caso de prueba de navegación:
  Verificar que el título de la página de inventario sea correcto
  Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
  Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
  Criterios mínimos:
  Valida título
  Valida presencia de productos
  Lista nombre/precio del primero.

```

#### Interacción con productos:

[test_carrito.py](./preentrega/tests/test_carrito.py)

```
Interacción con productos: (Clase 8)
    Caso de prueba de carrito:
    Añadir un producto al carrito haciendo clic en el botón correspondiente
    Verificar que el contador del carrito se incremente correctamente
    Navegar al carrito de compras
    Comprobar que el producto añadido aparezca correctamente en el carrito
    Criterios mínimos:
    Agrega primer producto
    Verifica ítem en carrito.
```
