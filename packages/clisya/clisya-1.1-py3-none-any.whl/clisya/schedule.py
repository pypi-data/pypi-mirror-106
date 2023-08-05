import clisya
import pytz
import datetime

# Esta es la hora local que asume GMT-5:
LOCAL_TZ = pytz.timezone('America/Bogota')

# En orden de tamaño de mercado/prioridad
ZONES = [
    ["🇲🇽", "America/Mexico_City","Mexico"],
    ["🇨🇴", "America/Bogota","Colombia"],
    ["🇵🇪", "America/Lima","Peru"],
    ["🇨🇱", "America/Santiago","Chile"],
    ["🇦🇷", "America/Buenos_Aires","Argentina"],
    ["🇧🇷","America/Sao_Paulo","Brasil"],
    ["🇪🇸", "Europe/Madrid","España"],
    ["🇺🇾", "America/Montevideo","Uruguay"],
    ["🇪🇨", "America/Guayaquil","Ecuador"],
    ["🇬🇹", "America/Guatemala","Guatemala"],
    ["🇸🇻", "America/El_Salvador","El_Salvador"],
    ["🇧🇴", "America/La_Paz","Bolivia"],
    ["🇵🇾", "America/Asuncion","Paraguay"],
    ["🇩🇴", "America/Santo_Domingo","Republica_Dominicana"],
    ["🇵🇦", "America/Panama","Panama"],
    ["🇨🇷", "America/Costa_Rica","Costa_Rica"],
    ["🇭🇳", "America/Tegucigalpa","Honduras"],
    ["🇻🇪", "America/Caracas","Venezuela"],
    ["🇳🇮", "America/Managua","Nicaragua"],
    ["🇨🇺", "Cuba","Cuba"],
    ["🇺🇸", "US/Pacific","Us_Pacific"]
]


class Schedule:
    """

    Instancia para generar el horario correspondiente
    segun el horario de cada país.

    """


    def convert(self, date_to_convert, country: list = None, times: dict = None):

        date_to_convert = datetime.datetime.strptime(
        date_to_convert, "%Y-%m-%d %H:%M:%S")
        
        
        date_to_convert = LOCAL_TZ.localize(date_to_convert)

        dtc = date_to_convert.astimezone(pytz.timezone(country[1]))
        if country[1] == "Europe/Madrid":
                # Imprime la hora en formato de 24 horas y una "H" al final
            dtc = dtc.strftime("%-HH")
        else:
            # Imprime la hora en formato de 12 horas PM/AM
            dtc = dtc.strftime("%-I%p")
        try:
            times[dtc] = times[dtc] + country[0]
        except KeyError:
            times[dtc] = country[0]
        # Si el país es USA en Pacific, agregar el "PT" frente a bandera de US
        if country[1] == "US/Pacific":
            times[dtc] = times[dtc] + " PT"

        times[dtc] = times[dtc] + " "

        return times[dtc]


    def date_to_convert(self, date_to_convert, country: list = None):


        if country is None:

            """

            Decisión que obtiene todos los horarios de los países,
            sin necesidad de especificar country=[] como parámetro.

            """
            # Inicializamos el diccionario
            times = {"00pm": "X"}

            print(date_to_convert,"\nGenerating block of flags:\n")            
            for country in ZONES:
                #Llamando al metodo convert          
                self.convert(date_to_convert,country,times)
            #Listando resultado hora y bandera correspondiente
            for time, flag in times.items():
                if flag != 'X':
                    print(time.lower(), flag.strip())        

        elif country != None:

            """
            Desición que compara y recorre la búsqueda
            de los elementos dados por el usuario en la lista country[].
            
            ejemplo: country['Colombia','Peru','Mexico].

            """
            # Inicializamos el diccionario
            times = {"00pm": "X"}
            #Convirtiendo elementos de la lista en title()
            list_country = [list_country.title() for list_country in country]            
            #Generando lista de zonas
            list_zones=[]   
            #Ciclo que busca los elementos entrantes de la lista y los guarda en list_zones
            for country in ZONES:
                if country[2] in list_country:
                    list_zones.append(country)
            #Si la lista list_zones tiene algun elemento, entonces recorre los elementos dados.
            #Depende de cuantos elementos hayan ingresado en la lista country=[] 
            if len(list_zones) > 0:
                print(date_to_convert,"\nGenerating block of flags:\n")
                for country in list_zones: 
                    #Llamando al metodo convert.
                    self.convert(date_to_convert,country,times)
                #Listando resultado hora y bandera correspondiente
                for time, flag in times.items():
                    if flag != 'X':
                        print(time.lower(), flag.strip())
            else:
                return "The country list is empty, enter a name, example, country = ['Colombia', 'Mexico,'Peru']"


if __name__ == '__main__':
    # Fecha y hora de entrada
    clisya = Schedule()
    clisya.date_to_convert("2021-05-13 15:00:00")




