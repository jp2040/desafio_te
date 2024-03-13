class Te:
    # Atributo de clase para el tiempo de duración en días
    tiempo_duracion_dias = 365

    def __init__(self, sabor: int, formato: int):
        """
        Clase para representar un tipo de té.

        Args:
        - sabor (int): Número correspondiente al sabor del té.
        - formato (int): Número correspondiente al formato del té.
        """
        self.sabor = sabor
        self.formato = formato

    @staticmethod
    def obtener_tiempo_recomendacion(sabor: int):
        """
        Método estático para obtener el tiempo de preparación y la recomendación según el sabor.

        Args:
        - sabor (int): Número correspondiente al sabor del té.

        Returns:
        - tuple: (tiempo de preparación, recomendación)
        """
        if sabor == 1:
            return 3, "Al desayuno"
        elif sabor == 2:
            return 5, "Al medio día"
        elif sabor == 3:
            return 6, "Al atardecer"

    @staticmethod
    def obtener_precio(formato: int):
        """
        Método estático para obtener el precio según el formato.

        Args:
        - formato (int): Número correspondiente al formato del té.

        Returns:
        - int: Precio del té.
        """
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
