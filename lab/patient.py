from typing import List
from exceptions import TemperatureError, PatientError

class Patient:
    """Patient temperature monitor with validation."""
    VALID_TEMP_RANGE = (34.0, 43.0)
    

    #Betyr len i denne sammenhengen lengh? Og hva betyr strip (hvorfor brukes dette?)

    #Betyr len her "length"?

    '''
    Ja ✅

    len(patient_id)

    betyr:

    Hvor mange tegn er det i teksten?

    Eksempel:

    len("P01")   # 3
    len("A")     # 1

    Så når du skriver:

    if len(patient_id) < 3:

    betyr det:

    👉 ID må ha minst 3 tegn.
    '''


    #Hva gjør strip() og hvorfor brukes det?

    '''
    name.strip()

    strip() fjerner mellomrom før og etter tekst.

    Eksempel:

    "   Ole   ".strip()

    blir:

    "Ole"

    Hvorfor er dette viktig?

    Hvis en bruker skriver:

    Patient("P001", "   O   ")

    Uten strip() ville lengden blitt 5 (på grunn av mellomrom),
    men egentlig er navnet bare "O".

    Så:

    len(name.strip()) < 2

    sikrer at det faktisk er minst 2 ekte bokstaver.

    '''

    def __init__(self, patient_id: str, name: str):
        if not patient_id or len(patient_id) < 3:
            raise PatientError(patient_id, "ID must be 3+ characters")
        if not name or len(name.strip()) < 2:
            raise PatientError(patient_id, "Name must be 2+ characters")
        
        self.patient_id = patient_id
        self.name = name.strip()
        self.temperatures: List[float] = []


    # Hva betyr -> None?

    '''
    Dette er en type hint.

    Det betyr:

    Denne funksjonen returnerer ingenting.

    Altså det samme som:

    return None

    Men vi skriver det for tydelighet og type-sjekking.

    '''


    def add_temperature(self, temp_celsius: float)-> None:
        """Add temperature reading. Raise TemperatureError if invalid."""
        if not isinstance(temp_celsius, (int, float)):
            raise TemperatureError(temp_celsius, "Must be number")
        
        temp = float(temp_celsius)

        if temp < self.VALID_TEMP_RANGE[0] or temp > self.VALID_TEMP_RANGE[1]:
            raise TemperatureError(
                temp,
                f"Out of valid range {self.VALID_TEMP_RANGE[0]}-{self.VALID_TEMP_RANGE[1]}°C"
            )
        
        self.temperatures.append(temp)


    def get_average_temperature(self)-> float:
        """Calculate average temperature."""
        if not self.temperatures:
            raise PatientError(self.patient_id, "No temperature readings")


        #Betyr len her også length?
        '''
        Ja 👇

        len(self.temperatures)

        Betyr:

        Hvor mange temperaturmålinger finnes i listen?
        ''' 


        avg=sum(self.temperatures) / len(self.temperatures)
        

        #Hva betyr round(avg, 1)?

        '''
        return round(avg, 1)

        round(tall, 1) betyr:

        Rund av til 1 desimal.

        '''
        
        return round(avg, 1)

        

    def has_fever(self)->bool:
        """Check if current average indicates fever (>38.0°C)."""
        try:
            return self.get_average_temperature()>38.0
        except PatientError:
            return False
        