# DRF Bootcamp
Este proyecto contiene el código desarrollado durante la clase sobre Django Rest Framework.

La clase está diseñada para enseñar a los desarrolladores cómo construir una API RESTful con Django Rest Framework. El proyecto incluye varias secciones que utilizan diferentes enfoques para desarrollar una API, desde la creación de una API básica utilizando solo Django, hasta el uso de vistas de clase y funciones en Django Rest Framework.

Cada sección se almacena en una rama separada, lo que permite a los desarrolladores explorar diferentes enfoques y comparar las diferencias entre ellos. A continuación, se describen las ramas disponibles:

Las distintas secciones estan contenidas en ramas:
- **proyecto-inicial**: proyecto Django inicial, solo con el modelo creado.
- **api-basica-djang**o: API desarrollada usando solo Django.
- **drf-api-views**: API desarrollada usando vistas de API.
- **drf-class-views**: API desarrollada usando vistas de clase.
- **drf-function-views**: API desarrollada usando vistas de función.
- **main**: código final del proyecto.
  
Para cambiar a una rama diferente, utilice el siguiente comando Git:
`git checkout nombre-rama  `

## Instalación de dependencias
Para instalar las dependencias del proyecto, siga estos pasos:
1. Abra una terminal dentro del proyecto, en la misma ubicación que el archivo *requirements.txt.*
2. Active el virtualenv del proyecto.
2. Ejecute el siguiente comando pip para instalar las dependencias del proyecto desde el archivo *requirements.txt*:
`pip install -r requirements.txt`

## Correr migraciones
Para crear la base de datos localmente deben correr el siguiente comando
`python .\manage.py migrate`
