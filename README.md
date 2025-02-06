# Gestión de la Declaración de Aplicabilidad (SoA) - ISO 27001

Este proyecto tiene como objetivo ayudar a gestionar la Declaración de Aplicabilidad (SoA) de los controles a tener en cuenta para proyectos de implementación de la ISO 27001. Permite crear y gestionar los diferentes controles por categorías, validar si se aplicará el control y, en caso de que no, registrar las razones o justificación de por qué no se aplicará.

## Características

- **Gestión de controles**: Crear, editar y eliminar controles.
- **Categorías de controles**: Organizar los controles en diferentes categorías.
- **Validación de controles**: Validar si un control se aplicará o no.
- **Justificación de exclusiones**: Registrar las razones o justificación de por qué un control no se aplicará.

## Requisitos

- Python 3.x
- Django
- UV (para la gestión de entornos virtuales)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. Crea y activa el entorno virtual:

    ```bash
    uv .venv
    .venv\Scripts\activate  # En Windows
    source .venv/bin/activate  # En Unix o MacOS
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

5. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

## Uso

1. Accede a la aplicación en tu navegador web en `http://127.0.0.1:8000/`.
2. Crea y gestiona los controles y categorías desde la interfaz de usuario.
3. Valida si los controles se aplicarán y registra las justificaciones necesarias.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cualquier cambio importante antes de enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.