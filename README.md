# Juego de la Culebrita

Este es un juego clásico de la culebrita, desarrollado en Python utilizando la librería Pygame. El jugador controla una serpiente que debe comer huevos de pollo, y la dificultad aumenta a medida que avanza. El objetivo es llegar a 20 puntos sin perder todas las vidas.

## Características

- **Menú principal**: El jugador puede elegir entre iniciar el juego o salir presionando las teclas correspondientes.
- **Puntuación**: La puntuación aumenta al comer huevos de pollo. Cada huevo vale un punto.
- **Vidas**: El jugador comienza con tres vidas. Si choca con un pollo o es atrapado por ellos, pierde una vida y tres puntos.
- **Dificultad creciente**: Cada tres huevos que come la serpiente, aparece un nuevo pollo. Los pollos se van generando a los tres, seis, doce puntos, y así sucesivamente.
- **Pantalla de Game Over**: Si el jugador pierde todas sus vidas o su puntuación llega a un número negativo, el juego termina y se muestra la pantalla de Game Over. Desde allí, el jugador puede regresar al menú principal.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **Carpeta "Access"**:  
  Contiene las imágenes necesarias para el juego, incluyendo:
  - **Fondo**: Imágenes de fondo para el juego.
  - **Personajes**: Imágenes de la culebra y los pollos.
  - **Huevo**: Imagen del huevo que la serpiente debe comer para ganar puntos.

## Instalación

1. **Requisitos previos**:
   - Python 3.x
   - Pygame (se puede instalar con `pip install pygame`)

2. **Pasos de instalación**:
   - Clona el repositorio:  
     ```bash
     git clone https://tu-repositorio.git
     ```
   - Navega al directorio del proyecto:  
     ```bash
     cd nombre-del-proyecto
     ```
   - Instala las dependencias necesarias:
     ```bash
     pip install pygame
     ```

3. **Ejecutar el juego**:
   - Para iniciar el juego, ejecuta el archivo principal:  
     ```bash
     python main.py
     ```

## Controles

- **Tecla 1**: Iniciar el juego.
- **Tecla 2**: Salir del juego.
- Usa las teclas de flecha para mover la serpiente.

## Contribuciones

Si deseas contribuir al proyecto:
- Realiza un *fork* del repositorio.
- Crea una rama para tus cambios: `git checkout -b feature/nueva-funcionalidad`
- Envía un *pull request* para revisar los cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
