'''Create TemperatureError exception that stores temperature value and message'''

class TemperatureError(Exception):
    
    """Custom exception for invalid temperatures."""

    def __init__ (self, temperature: float, message: str):
        self.temperature = temperature
        self.message = message
        super().__init__(f"TemperatureError: {temperature}°C - {message}")



'''Create PatientError exception that stores patient_id and message'''

class PatientError(Exception):
    """Base exception for patient-related errors."""

    def __init__ (self, patient_id: str, message: str):
        self.patient_id = patient_id
        self.message = message
        super().__init__(f"PatientError[{patient_id}]: {message}")



'''Both should inherit from Exception and call super().__init__() with
formatted message'''


#Hvorfor definerer vi Exception classen på denne måten, bare som det en tar inn i de andre classene?
# Og hvorfor kaller en på superklassen (Exception) for å skrive ut errormeldingene, og hvordan fungerer dette?


#Hvorfor arver vi fra Exception?

'''
class TemperatureError(Exception):

Når vi skriver dette, betyr det:

TemperatureError er en type Exception

Altså: den oppfører seg akkurat som en vanlig Python-feil, men med vår egen tilpasning.

Hvis vi ikke arvet fra Exception, ville ikke:

with pytest.raises(TemperatureError):

fungert riktig.

Python kjenner bare igjen feil som kan fanges (except) hvis de arver fra BaseException (og normalt Exception).

Så dette gjør at vi kan:

raise TemperatureError(...)

og så:

except TemperatureError:

'''


#Hvorfor kaller vi super().__init__()?

'''
Dette er den viktigste delen.

super().__init__(f"TemperatureError: {temperature}°C - {message}")

super() betyr:

Kjør init til foreldrekassen (Exception)

Hva gjør egentlig Exception?

Den lagrer feilmeldingen internt slik at:

print(e)

fungerer.

Hvis du ikke kaller super().__init__(), vil ikke feilmeldingen bli registrert riktig.
'''