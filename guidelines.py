from typing import List

from src.tasks.utils_typing import Entity, dataclass

"""
Entity definitions
"""

@dataclass
class Observation(Entity):
    """An Observation refers to any piece of information or data that is noted or recorded about a patient's health status, this includes
    symptoms, diagnoses, test results risk factors like smoking or contextual information like the age or conditions of the patient."""
    
    span: str
    """
    Such as: not possible to administer, distribution of 18-F-FDG, severe hypoxemia, reduced eGFR, Diabetes, hypercapnia, postoperative pain, prostate cancer, elderly
    """


@dataclass
class Activity(Entity):
    """An Activity refers to any action performed by a patient or a healthcare professional, this includes
    tasks, procedures, surgeries, treatments, medication, or other types of interventions. Activities can also be events like start of the scan."""
    
    span: str # Such as: eat, fasting, start, monitored, assessed, reviewed, performed, administered, prescribed, recommended, catheterization, filled, referred, continued, anesthesia

@dataclass
class Input(Entity):
    """An Input Entity refers to any word or phrase that denotes a specific type of clinical measurement, score, or value. 
    These include, but are not limited to, physiological measurements, lab test scores, and specific clinical indices. 
    The difference to the guard is that it not represents specific numerical values or thresholds related but the category of the measurement or value for example
    Blood Pressure, Heart Rate, PEEP, Pmean or PaO2/FiO2. 
    """

    span: str # Such as: pH, Blood Pressure, Heart Rate, PEEP, Pmean or PaO2/FiO2, retention, distribution, eGFR, se-creatinine, sizes

@dataclass
class Output(Entity):
    """An Input Entity refers to any word or phrase that denotes a specific type of clinical measurement, score, or value. 
    These include, but are not limited to, physiological measurements, lab test scores, and specific clinical indices. 
    The difference to the guard is that it not represents specific numerical values or thresholds related but the category of the measurement or value for example
    Blood Pressure, Heart Rate, PEEP, Pmean or PaO2/FiO2. 
    """

    span: str # Such as: pH, Blood Pressure, Heart Rate, PEEP, Pmean or PaO2/FiO2, retention, distribution, eGFR, se-creatinine, sizes

@dataclass
class Actor(Entity):
    """An Actor refers to any person or entity that is involved in an activity, this includes
    patients, doctors, nurses, or other healthcare professionals. Actors can perform activites or be the target of activities."""
    
    span: str # Such as: patients, patient, doctor, pt., anesthesiologist, 

@dataclass
class ActivityData(Entity):
    """An ActivityData entity refers to the data or object directly used by an activity, this includes devices, medications, objects. 
    This could be for example an injection or a scan or insuline."""
    
    span: str # Such as: flow and residual urine, insuline, bladder, an appointment, tablet paracetamol, antidiabetic medication

@dataclass
class Specification(Entity):
    """A Specification entity refers to any information that further describes an activity, this includes
    the time, the location, the dosage, the quantity, the frequency, the duration, additional information or the type of the activity.
    Specifications are often linked with prepositions like for example at, to, in, into, on, for, with, within, while, as, according to, across, after, by, during, for, over, when, where."""
    
    span: str # Such as: between the first and second tracheal, long-term, acute phase, outpatient clinic, saline, elsewhere in the body, following afternoon

@dataclass
class Guard(Entity):
    """A Guard refers to a specific type of information that sets conditions, limits, or thresholds in the clinical context. 
    These entities often represent critical values or timeframes that impact clinical decisions, such as dosage limits, duration of treatment, or thresholds for test results.
    This can include measurements (like volume or concentration), timeframes (like durations or frequencies), or any other quantifiable condition that affects clinical decisions."""
    
    span: str # after 1 week, >1000 ml, <1000 ml, at least 2 hours, for 6 hours, < 45

@dataclass
class PurposeOutcome(Entity):
    """A PurposeOutcome entity captures the underlying reason, goal, objective, or anticipated result of a clinical action, procedure, or recommendation. 
    It addresses the "why" or the intended effect of a medical intervention or guideline. Examples would be: to reduce the risk of stroke or so that the patient can sleep better.
    The PurposeOutcome entity is often connected with prepositions like for, to, in order to, so that, to ensure, because maybe or because of."""

    span: str # adequate bladder volume, 

@dataclass
class And(Entity):
    """An And entity connects two or more activities that are linked by the conjunction "and." This entity indicates that all linked activities are required or occur in conjunction.
       Primarily used in scenarios where multiple steps or conditions are simultaneously necessary. For instance, in a treatment plan, if multiple treatment activities need to be executed together.
    """

    span: str # Such as: and, &, +, as well as

@dataclass
class Or(Entity):
    """An Or entity links two or more activities or options, using the conjunction "or." 
    It signifies that any one of the linked activities or observations may be chosen or is applicable, but not necessarily all.
    Useful in cases where multiple options are available, and the choice of one excludes the others. Often seen in treatment plans where alternative activities are viable."""

    span: str # Such as: or, /, 

@dataclass
class Xor(Entity):
    """An Xor (exclusive or) entity connects two or more mutually exclusive activities, actions, tasks or observations, using the concept of "xor." 
    It implies that only one of the linked activities can be chosen or applies, and selecting one excludes the others.
    Applied in situations where two or more options are available but are mutually exclusive. It's critical in scenarios where the selection of one option inherently rules out the others.
    """

    span: str 

@dataclass
class RelationResponse(Entity):
    """A RelationResponse entity captures the relationship between two activties or an observation and a activity which need to be executed. So after executing the first activity the second activity must be exectued.
    The RelationResponse entity can therefore be for example action A and requires action B, observation A: administer drug B. 
    """

    span: str # can be repeated, and requires, whether, during this period, in case of, must

@dataclass
class RelationCondition(Entity):
    """A RelationCondition entity captures the relationship between two activties or an observation and a activity which need to be executed in a specific order. So action B can only be executed after action A.
    Activity B could for instance be “Prescribe medicin”. For that to happen a medical examination has to take place, which could be activity A.
    The RelationCondition entity can therefore be for example "in cases where" so "use infusion fluid only in cases where the patient is dehydrated" or "before" so "before prescribing medication, perform a medical examination".
    """

    span: str # Such as: and finally, when, followed by, after, during this period, :, before, until

@dataclass
class RelationExclusion(Entity):
    """A RelationExclusion entity caputres the relationship between two activities or an observation and an activity where one is excluding the other. 
    Examples for the RelationExclusion entity would be for example not routinely recommmended, or should not be, if observation activity is not possible."""

    span: str # Such as: must not, not suitable, should not

@dataclass
class RelationInclusion(Entity):
    """A RelationInclusion entity captures the relationship between two activities or an observation and an activity where one is including the other. For example blood tests are not required unless
    observation A is true. The RelationInclusion entity can therefore be for example "unless" so "blood tests are not required unless observation A is true" 
    or "if" so "if observation A is true, then blood tests are required"."""

    span: str

ENTITY_DEFINITIONS: List[Entity] = [
    Observation,
    Activity,
    Input,
    Output,
    Actor,
    ActivityData,
    Specification,
    Guard,
    PurposeOutcome,
    And,
    Or,
    Xor,
    RelationResponse,
    RelationCondition,
    RelationExclusion,
    RelationInclusion
]

if __name__ == "__main__":
    cell_text = In[-1]
