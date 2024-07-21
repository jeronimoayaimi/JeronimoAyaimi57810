# Barbería Django App

## Descripción

Este proyecto es una aplicación web desarrollada en Django para la gestión de una barbería. La aplicación permite a los usuarios reservar turnos y gestionar sus reservas. Los turnos pueden tener dos estados: **confirmado** (por defecto) y **cancelado** (cuando el usuario cancela la reserva).

## Características

- Reserva de turnos.
- Gestión de reservas (confirmar y cancelar).
- Formulario de sucursal para la administración de la barbería.
- Formulario de edición de usuario.

## Estructura del Proyecto

### Formularios

#### SucursalForm
Formulario utilizado para administrar la información de las sucursales.

Campos:
- `nombreSucursal`: Nombre de la sucursal.
- `direccionSucursal`: Dirección de la sucursal.
- `telSucursal`: Teléfono de la sucursal.
- `horariosSucursal`: Horarios de atención de la sucursal.

#### userEditForm
Formulario utilizado para editar la información de los usuarios. Este formulario extiende de `UserChangeForm`.

Campos:
- `email`: Correo electrónico del usuario.
- `first_name`: Nombre del usuario.
- `last_name`: Apellido del usuario.

### Modelos
La aplicación cuenta con modelos que representan las entidades principales, como usuarios y sucursales, y se encargan de gestionar las reservas de turnos.

## Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/jeronimoayaimi/JeronimoAyaimi57810.git
    ```

2. Crear y activar un entorno virtual:
    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instalar las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Realizar las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```

5. Ejecutar el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Uso

Accede a la aplicación en `http://localhost:8000` y utiliza las funcionalidades para reservar y gestionar turnos en la barbería.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios necesarios y haz commits (`git commit -m 'Agregar nueva funcionalidad'`).
4. Empuja los cambios a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia



## Contacto

Para más información, puedes contactarme a través de [mi perfil de GitHub](https://github.com/jeronimoayaimi).

---




## Desarrollador
Jerónimo Martínez
