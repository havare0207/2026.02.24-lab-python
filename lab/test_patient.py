import pytest
from exceptions import TemperatureError, PatientError
from patient import Patient

class TestPatient:

    def test_valid_patient_cretion(self):

        patient = Patient("Poo1", "Ole Normann")

        #Hvorfor brukes assert her, og hva var det det betydde igjen?

        '''I testing betyr:

        assert noe == noe_annet

        = Testen feiler hvis dette ikke er sant.
        '''


        assert patient.patient_id == "Poo1"
        assert patient.name == "Ole Normann"
        assert len(patient.temperatures) == 0

    def test_invalid_patient_id(self):

        #Hvordan fungerer pytest i denne situasjonen?
        
        with pytest.raises(PatientError, match="ID must"):

            #Hvorfor A og Test, hva gjør en egentlig her?

            Patient("A", "Test")


    def test_temperatures_too_high(self):
        patient = Patient("P001", "Ole")

        #Hva tester en her, og hvordan fungerer pytest i denne situasjonen?

        with pytest.raises(TemperatureError, match="43.0"):
            patient.add_temperature(45.0)


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
