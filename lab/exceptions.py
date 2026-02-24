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

