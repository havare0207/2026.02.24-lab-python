import pytest
from exceptions import TemperatureError, PatientError
from patient import Patient

class TestPatient:

    def test_valid_patient_cretion(self):

        patient = Patient("Poo1", "Ole Normann")

        #Hvorfor brukes assert her?
        ''' 
        assert patient.patient_id == "Poo1"

        I pytest betyr:

        Hvis dette ikke er sant → testen feiler.

        Altså:

        Hvis patient.patient_id er "Poo1" → testen fortsetter

        Hvis den er noe annet → pytest stopper testen og markerer den som FAIL

        I testing betyr:

        assert noe == noe_annet

        = Testen feiler hvis dette ikke er sant.
        '''


        assert patient.patient_id == "Poo1"
        assert patient.name == "Ole Normann"
        assert len(patient.temperatures) == 0

    def test_invalid_patient_id(self):

        #Hvordan fungerer pytest i denne situasjonen?
        '''
        with pytest.raises(PatientError, match="ID must"):
            Patient("A", "Test")

        Dette betyr:

        Denne koden SKAL kaste en PatientError.

        Hvis den:

        ❌ Ikke kaster feil → testen feiler

        ❌ Kaster feil, men feil type → testen feiler

        ❌ Kaster riktig type, men feilmeldingen inneholder ikke "ID must" → testen feiler

        ✅ Kaster riktig feil med riktig tekst → testen består

        '''
        
        with pytest.raises(PatientError, match="ID must"):


            Patient("A", "Test")


            #Hvorfor "A" og "Test"?

            '''


            Patient("A", "Test")

            Dette er bare testdata.

            Du tester at ID må være minst 3 tegn:

            if len(patient_id) < 3:

            "A" har lengde 1 → det skal trigge:

            raise PatientError(...)

            Så "A" er bare valgt fordi den er for kort.

            "Test" brukes bare som gyldig navn – det er ikke viktig her.

            '''


    def test_temperatures_too_high(self):
        patient = Patient("P001", "Ole")


        with pytest.raises(TemperatureError, match="43.0"):
            patient.add_temperature(45.0)


        #Hva tester man her?

        '''
        with pytest.raises(TemperatureError, match="43.0"):
            patient.add_temperature(45.0)

        Dette tester:

        At temperaturen 45.0 er utenfor gyldig område (34.0–43.0)

        At TemperatureError kastes

        At feilmeldingen inneholder 43.0

        Hvorfor "43.0"?

        Fordi feilmeldingen din inneholder:

        f"Out of valid range 34.0-43.0°C"

        pytest sjekker str(exception).


        '''


    def test_average_temperature(self):
        patient = Patient("P001", "Ole")
        patient.add_temperature(37.0)
        patient.add_temperature(38.0)
        patient.add_temperature(37.5)

        #Skal assert her sjekke om gjennomsnittet av temperaturene er på 37.5, og hva betyr egentlig assert i python i testing av programmer?
        
        '''I testing betyr:

        assert noe == noe_annet

        = Testen feiler hvis dette ikke er sant.
        '''

        assert patient.get_average_temperature() == 37.5

        #Ja – her tester du gjennomsnittet

        '''
        assert patient.get_average_temperature() == 37.5

        Dette tester:

        At summen regnes riktig

        At delingen fungerer

        At round(..., 1) fungerer

        At riktig verdi returneres

        Du tester hele beregningslogikken i én linje.

        '''