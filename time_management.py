#Practica3_Jose_Quintana
#Conceptos de clase, atributos(datos miembro) y metodos(funciones miembro)



class Time:
    """
    Class that represent a time with AM/PM or 24 hours format
    
    Class Attributes:
    TIME_FORMATS  #("AM/PM","24 HOURS")
    time_count =0 #Counts the number of Time objects created

    Atrributes:
    hours  #stores the hours  (1 to 12 for AM/PM format, 0 to 23 for 24 hours format)
    minutes #stores the minutes (0 to 59)
    seconds #stores the seconds (0 to 59)
    format #stores the format of the time (AM/PM or 24 hours)    
    """

     # Class attributes
    TIME_FORMATS = ["AM", "PM", "24 HOURS"]
    time_count = 0

    def __init__(self,hours=0,minuts=0,seconds=0,format="24 HOURS"):
        self.hours=hours
        self.minuts=minuts
        self.seconds=seconds
        self.format=format  #Formato AM/PM o 24 horas
        Time.time_count += 1 #incrementa el contador de objetos de tiempo creados
    
    def __asign_format(self, pszFormat):
        """
        Checks pszFormat has correct value & assigns it to format.
        Converts to upper case to avoid problems with capitalization.
        """
        pszFormat = pszFormat.upper()
        if pszFormat in self.TIME_FORMATS:
            self.format = pszFormat
            return True
        return False
       
    def __is_24hour_format(self):
        """
        Checks if the time format is "24 HOURS".
        """
        return self.format == "24 HOURS"

    def __is_valid_time(self):
      if self.__is_24hour_format():
        return (0 <= self.hours < 24) and (0 <= self.minutes < 60) and (0 <= self.seconds < 60)
      else:
        return (1 <= self.hours <= 12) and (0 <= self.minutes < 60) and (0 <= self.seconds < 60)

    def set_time(self,nHours,nMinutes,nSeconds,pszFormat):
        """ 
        Assigns a time to the class.  
 
        Args: 
            nHoras: Hours (1 to 12 AM/PM, 0 to 23 for 24 hours). 
            nMinutos: Minutes (0 to 59). 
            nSegundos: Seconds (0 to 59). 
            pszFormato: Time format ("AM", "PM" or "24 HOURS"). 
 
        Returns: 
            True if the time could be assigned correctly,  
            False otherwise. 
        """ 
        if self.__asign_format(pszFormat):  # Primero se asigna el formato
         if self.__is_valid_time():
            self.hours = nHours
            self.minutes = nMinutes
            self.seconds = nSeconds
            return True
         else:
            print("Hora, minutos o segundos no válidos.")
        else:
         print("Formato de hora no válido.")
        return False


    def get_time(self):
        """
        Returns the current time of the class.
        """
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} {self.format}"

        
    @classmethod  #un decorador  que indica que el metodo es de clase 
    def from_string(cls, time_string):   #from_string es un metodo de clase que recibe un string y devuelve un objeto de la clase Time
        """ 
          Class method to create Time object from string. 
 
          Args: 
            time_string (str): A string representing time in the 
            format "HH:MM:SS FORMAT", where FORMAT is AM, PM, or 24 HOURS. 
 
               Returns: 
               Time: new Time object with the parsed time. 
               If the time string is invalid, print a message. 
        """ 
         #Import the 're' module for regular expressions 
         # Define regular expression pattern to match time strings 
         # Pattern should match strings like  
         # "14:30:00 24 HOURS" or "02:45:30 PM" 
         # Use re.match to check if the time_string matches pattern 
 
         # Extract hours, minutes, seconds, & format from matched  
         # groups 
 
         # Create a new Time object 
 
         # Set the time using the extracted values 
         # Convert hours, minutes, and seconds to integers 
 
         # Return the new Time object 
 
         #Print a message if the time string format is invalid 
         #función de analizar una cadena de texto que representa un tiempo (en formato de 24 horas o AM/PM), extraer los componentes de horas, minutos, segundos y formato, y luego crear un nuevo objeto Time con esos valores. Si la cadena no tiene el formato correcto, imprime un mensaje de error y retorna None.
        
        import re  #importa el modulo re para expresiones regulares
        
        pattern = r"(\d{2}):(\d{2}):(\d{2})\s(AM|PM|24 HOURS)" #define el patron de la expresion regular para coincidir con las cadenas de tiempo
        match = re.match(pattern, time_string.upper())  #usa re.match para verificar si la cadena de tiempo coincide con el patron
        if match: 
            hours, minutes, seconds, format_time = match.groups()   #extrae horas, minutos, segundos y formato de los grupos coincidentes y lo guarda en una tupla
            new_time = cls()
            if new_time.set_time(int(hours), int(minutes), int(seconds), format_time): 
                return new_time
        print("Invalid time string format.")

        return None
    


    @staticmethod 
    def is_valid_format(time_format): 
        """ 
          Static method to check if a given time format is valid. 
 
          Args: 
          time_format (str): The time format to check. 
 
          Returns: 
          bool: True if the format is valid (AM, PM, or 24 HOURS),  
                False otherwise. 
        """ 
        if time_format.upper() in Time.TIME_FORMATS:  
            return True
        else:
            print("Invalid time format.")
            return False
            

    @classmethod
    def get_time_count(cls): #cls es una referencia a la clase actual 
        """
        Class method to get total number of Time objects created.

        """
        return cls.time_count #devuelve el numero de objetos de tiempo creados
    
    
def display_time_as_string(time_obj):
    """
    Function outside the class to show the time in a string format.
    """
    return time_obj.get_time()

def main():
     current_time = Time() #crea un objeto de la clase Time


while True:
    print("\nMenu:")
    print("1. Introducir una nueva hora")
    print("2. Visualizar hora actual")
    print("3. Crear una hora a partir de una cadena (formato HH:MM:SS)")
    print("4. Terminar")

    opcion=input("Seleccione una opción: ")

    if opcion=="1":
        try:
            hours=int(input("Ingrese las horas: "))
            minutes=int(input("Ingrese los minutos: "))
            seconds=int(input("Ingrese los segundos: "))
            format_time=input("Ingrese el formato (AM, PM o 24 HOURS): ")
            if current_time.set_time(hours,minutes,seconds,format_time):   #asigna la hora al objeto de la clase Time
                print("Hora asignada correctamente.")
            else:
                print("Hora no válida.")
        except ValueError:
            print("Error: Por favor, introduzca números para horas, minutos y segundos.")
      
    elif opcion=="2":
        print(f"Hora actual: {display_time_as_string(current_time)}")   #muestra la hora actual

    elif opcion == "3":
            time_str = input("Ingrese la cadena de hora (formato HH:MM:SS FORMAT): ")
            new_time = Time.from_string(time_str)
            if new_time:
                current_time = new_time
                print(f"Hora creada: {display_time_as_string(current_time)}")
            else:
                print("No se pudo crear la hora a partir de la cadena.")

    elif opcion == "4":
            print("Terminando el programa...")
            break

    else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()


      
        
       
       
    
