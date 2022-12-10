Este proyecto consiste en realizar las pruebas para validar el correcto funcionamiento de una tienda de ropa en linea.

A continuación está la explicación del paso a paso que se debe llevar a cabo para realizar la ejecución de la prueba.

Se deben de tener instalados los ambientes, python, selenium, behave y un editor como Pycharm. Ademas para el correcto funcionamiento del programa se debe ejecutar:
pip install requirements.txt

Una vez se tenga todo instalado, se procede a abrir la terminal y ingresar el siguiente comando:
behave features\login.feature   -> Esto con el fin de poder visualizar la ejecución de la prueba

La prueba lo que hace es ingresar de manera automatica en el login, un usuario y contraseña, posteriormente clic en el botón iniciar sesión.
Una vez se inicia sesión correctamente, se seleccionan dos productos que se agregarán al carrito de compras.
Cuando se seleccionan los productos a comprar, el sistema da clic en el carrito de compras y clic en el carrito, en el checkout, seguidamente, se procede a ingresar nombre, apellido, codigo postal y clic en el bloton de continuar.
y finalmente clic en el botón finalizar compra y cerrar sesión.

Es de aclarar que la prueba se desarrollo para que se ejecutara con 3 usuarios diferentes.
