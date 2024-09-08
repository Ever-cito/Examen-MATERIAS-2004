import psycopg2
class Conexion:

    """Metodo contructor de la materia
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=examenfinaldb user=postgres host=localhost password=everchavez2004")
        
        """getConexion

            retorna la instancia de la base de datos
        """
    def getConexion(self):
        return self.con 