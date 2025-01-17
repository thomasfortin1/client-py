#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Encounter) on 2019-05-07.
#  2019, SMART Health IT.


from . import clinicalresource


class Encounter(clinicalresource.ClinicalResource):
    """ An interaction during which services are provided to the patient.
    
    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """

    resource_type = "Encounter"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.account = None
        """ The set of accounts that may be used for billing for this Encounter.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.appointment = None
        """ The appointment that scheduled this encounter.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.basedOn = None
        """ The ServiceRequest that initiated this encounter.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.classHistory = None
        """ List of past encounter classes.
        List of `EncounterClassHistory` items (represented as `dict` in JSON). """

        self.class_fhir = None
        """ Classification of patient encounter.
        Type `Coding` (represented as `dict` in JSON). """

        self.diagnosis = None
        """ The list of diagnosis relevant to this encounter.
        List of `EncounterDiagnosis` items (represented as `dict` in JSON). """

        self.episodeOfCare = None
        """ Episode(s) of care that this encounter should be recorded against.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.hospitalization = None
        """ Details about the admission to a healthcare service.
        Type `EncounterHospitalization` (represented as `dict` in JSON). """

        self.identifier = None
        """ Identifier(s) by which this encounter is known.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.length = None
        """ Quantity of time the encounter lasted (less time absent).
        Type `Duration` (represented as `dict` in JSON). """

        self.location = None
        """ List of locations where the patient has been.
        List of `EncounterLocation` items (represented as `dict` in JSON). """

        self.partOf = None
        """ Another Encounter this encounter is part of.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.participant = None
        """ List of participants involved in the encounter.
        List of `EncounterParticipant` items (represented as `dict` in JSON). """

        self.period = None
        """ The start and end time of the encounter.
        Type `Period` (represented as `dict` in JSON). """

        self.priority = None
        """ Indicates the urgency of the encounter.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Coded reason the encounter takes place.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Reason the encounter takes place (reference).
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.serviceProvider = None
        """ The organization (facility) responsible for this encounter.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.serviceType = None
        """ Specific type of service.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.status = None
        """ planned | arrived | triaged | in-progress | onleave | finished |
        cancelled +.
        Type `str`. """

        self.statusHistory = None
        """ List of past encounter statuses.
        List of `EncounterStatusHistory` items (represented as `dict` in JSON). """

        self.subject = None
        """ The patient or group present at the encounter.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.type = None
        """ Specific type of encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(Encounter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Encounter, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, True, None, False),
            ("appointment", "appointment", fhirreference.FHIRReference, True, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("classHistory", "classHistory", EncounterClassHistory, True, None, False),
            ("class_fhir", "class", coding.Coding, False, None, True),
            ("diagnosis", "diagnosis", EncounterDiagnosis, True, None, False),
            ("episodeOfCare", "episodeOfCare", fhirreference.FHIRReference, True, None, False),
            ("hospitalization", "hospitalization", EncounterHospitalization, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("length", "length", duration.Duration, False, None, False),
            ("location", "location", EncounterLocation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("participant", "participant", EncounterParticipant, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("serviceProvider", "serviceProvider", fhirreference.FHIRReference, False, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusHistory", "statusHistory", EncounterStatusHistory, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

    def get_date(self, return_all=False):
        """
        if period is None return None

        Return the start date as the default for return_all=False
        if start is None for some reason, return end
        if end is also None return None
        """
        if self.period is None:
            return None
        start = self.period.start.date if self.period.start is not None else None
        end = self.period.end.date if self.period.end is not None else None

        if return_all:
            all_dates = {
                'start': start,
                'end': end
            }
            return start, all_dates if start is not None else end, all_dates
        else:
            return start if start is not None else end


from . import backboneelement


class EncounterClassHistory(backboneelement.BackboneElement):
    """ List of past encounter classes.
    
    The class history permits the tracking of the encounters transitions
    without needing to go  through the resource history.  This would be used
    for a case where an admission starts of as an emergency encounter, then
    transitions into an inpatient scenario. Doing this and not restarting a new
    encounter ensures that any lab/diagnostic results can more easily follow
    the patient and not require re-processing and not get lost or cancelled
    during a kind of discharge from emergency to inpatient.
    """

    resource_type = "EncounterClassHistory"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.class_fhir = None
        """ inpatient | outpatient | ambulatory | emergency +.
        Type `Coding` (represented as `dict` in JSON). """

        self.period = None
        """ The time that the episode was in the specified class.
        Type `Period` (represented as `dict` in JSON). """

        super(EncounterClassHistory, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EncounterClassHistory, self).elementProperties()
        js.extend([
            ("class_fhir", "class", coding.Coding, False, None, True),
            ("period", "period", period.Period, False, None, True),
        ])
        return js


class EncounterDiagnosis(backboneelement.BackboneElement):
    """ The list of diagnosis relevant to this encounter.
    """

    resource_type = "EncounterDiagnosis"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.condition = None
        """ The diagnosis or procedure relevant to the encounter.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.rank = None
        """ Ranking of the diagnosis (for each role type).
        Type `int`. """

        self.use = None
        """ Role that this diagnosis has within the encounter (e.g. admission,
        billing, discharge …).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(EncounterDiagnosis, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EncounterDiagnosis, self).elementProperties()
        js.extend([
            ("condition", "condition", fhirreference.FHIRReference, False, None, True),
            ("rank", "rank", int, False, None, False),
            ("use", "use", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class EncounterHospitalization(backboneelement.BackboneElement):
    """ Details about the admission to a healthcare service.
    """

    resource_type = "EncounterHospitalization"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.admitSource = None
        """ From where patient was admitted (physician referral, transfer).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.destination = None
        """ Location/organization to which the patient is discharged.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.dietPreference = None
        """ Diet preferences reported by the patient.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.dischargeDisposition = None
        """ Category or kind of location after discharge.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.origin = None
        """ The location/organization from which the patient came before
        admission.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.preAdmissionIdentifier = None
        """ Pre-admission identifier.
        Type `Identifier` (represented as `dict` in JSON). """

        self.reAdmission = None
        """ The type of hospital re-admission that has occurred (if any). If
        the value is absent, then this is not identified as a readmission.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.specialArrangement = None
        """ Wheelchair, translator, stretcher, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.specialCourtesy = None
        """ Special courtesies (VIP, board member).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(EncounterHospitalization, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EncounterHospitalization, self).elementProperties()
        js.extend([
            ("admitSource", "admitSource", codeableconcept.CodeableConcept, False, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("dietPreference", "dietPreference", codeableconcept.CodeableConcept, True, None, False),
            ("dischargeDisposition", "dischargeDisposition", codeableconcept.CodeableConcept, False, None, False),
            ("origin", "origin", fhirreference.FHIRReference, False, None, False),
            ("preAdmissionIdentifier", "preAdmissionIdentifier", identifier.Identifier, False, None, False),
            ("reAdmission", "reAdmission", codeableconcept.CodeableConcept, False, None, False),
            ("specialArrangement", "specialArrangement", codeableconcept.CodeableConcept, True, None, False),
            ("specialCourtesy", "specialCourtesy", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class EncounterLocation(backboneelement.BackboneElement):
    """ List of locations where the patient has been.
    
    List of locations where  the patient has been during this encounter.
    """

    resource_type = "EncounterLocation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.location = None
        """ Location the encounter takes place.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.period = None
        """ Time period during which the patient was present at the location.
        Type `Period` (represented as `dict` in JSON). """

        self.physicalType = None
        """ The physical type of the location (usually the level in the
        location hierachy - bed room ward etc.).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.status = None
        """ planned | active | reserved | completed.
        Type `str`. """

        super(EncounterLocation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EncounterLocation, self).elementProperties()
        js.extend([
            ("location", "location", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js


class EncounterParticipant(backboneelement.BackboneElement):
    """ List of participants involved in the encounter.
    
    The list of people responsible for providing the service.
    """

    resource_type = "EncounterParticipant"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.individual = None
        """ Persons involved in the encounter other than the patient.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.period = None
        """ Period of time during the encounter that the participant
        participated.
        Type `Period` (represented as `dict` in JSON). """

        self.type = None
        """ Role of participant in encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(EncounterParticipant, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EncounterParticipant, self).elementProperties()
        js.extend([
            ("individual", "individual", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class EncounterStatusHistory(backboneelement.BackboneElement):
    """ List of past encounter statuses.
    
    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """

    resource_type = "EncounterStatusHistory"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.period = None
        """ The time that the episode was in the specified status.
        Type `Period` (represented as `dict` in JSON). """

        self.status = None
        """ planned | arrived | triaged | in-progress | onleave | finished |
        cancelled +.
        Type `str`. """

        super(EncounterStatusHistory, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EncounterStatusHistory, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js


import sys

try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
