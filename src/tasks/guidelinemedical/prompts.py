from typing import Dict, List, Type

from ..utils_typing import Entity, Relation, dataclass
from ..utils_typing import Generic as Template

"""Entity definitions"""

@dataclass
class Observation(Entity):
    """{medical_observation}"""
    
    span: str # {medical_observation_examples}

@dataclass
class Activity(Entity):
    """{medical_activity}"""

    span: str # {medical_activity_examples}

@dataclass
class ParentActivity(Entity):
    """{medical_parent_activity}"""

    span: str

@dataclass
class Input(Entity):
    """{medical_input}"""

    span: str # {medical_input_examples}

@dataclass
class Output(Entity):
    """{medical_output}"""

    span: str # {medical_output_examples}

@dataclass
class Actor(Entity):
    """{medical_actor}"""

    span: str # {medical_actor_examples}

@dataclass
class ActivityData(Entity):
    """{medical_activitydata}"""
    
    span: str # {medical_activitydata_examples}

@dataclass
class Specification(Entity):
    """{medical_specification}"""
    
    span: str # {medical_specification_examples}

@dataclass
class Guard(Entity):
    """{medical_guard}"""
    
    span: str # {medical_guard_examples}

@dataclass
class PurposeOutcome(Entity):
    """{medical_purposeoutcome}"""

    span: str # {medical_purposeoutcome_examples}

@dataclass
class And(Entity):
    """{medical_and}"""

    span: str # {medical_and_examples}

@dataclass
class Or(Entity):
    """{medical_or}"""

    span: str # {medical_or_examples}

@dataclass
class Xor(Entity):
    """{medical_xor}"""

    span: str # {medical_xor_examples}

@dataclass
class ResponseEntity(Entity):
    """{medical_response}"""

    span: str # {medical_response_examples}

@dataclass
class ConditionEntity(Entity):
    """{medical_condition}"""

    span: str # {medical_condition_examples}

@dataclass
class ExclusionEntity(Entity):
    """{medical_exclusion}"""

    span: str # {medical_exclusion_examples}

@dataclass
class InclusionEntity(Entity):
    """{medical_inclusion}"""

    span: str # {medical_inclusion_examples}

ENTITY_DEFINITIONS: List[Type] = [
    Observation,
    Activity,
    ParentActivity,
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
    ResponseEntity,
    ConditionEntity,
    ExclusionEntity,
    InclusionEntity,
]

"""Relation definitions"""
@dataclass
class ActivityActorRelation(Relation):
    """{medical_activity_actor}"""

    arg1: str
    arg2: str

@dataclass
class ActivitySpecificationRelation(Relation):
    """{medical_activity_specification}"""

    arg1: str
    arg2: str

"""RelationSubclass definitions"""


@dataclass
class ActivityActorPerformerRelation(Relation):
    """{medical_activity_actor_performer}"""

    arg1: str
    arg2: str

@dataclass
class ActivityActorReceiverRelation(Relation):
    """{medical_activity_actor_receiver}"""

    arg1: str
    arg2: str

@dataclass
class ActivityActivityDataRelation(Relation):
    """{medical_activity_activitydata}"""

    arg1: str
    arg2: str

@dataclass
class ActivityParentRelation(Relation):
    """{medical_activity_parent}"""

    arg1: str
    arg2: str

@dataclass
class ActivityGuardRelation(Relation):
    """{medical_activity_guard}"""

    arg1: str
    arg2: str

@dataclass
class ActivityPurposeOutcomeRelation(Relation):
    """{medical_activity_purposeoutcome}"""

    arg1: str
    arg2: str

@dataclass
class ConnectRelation(Relation):
    """{medical_activity_connect}"""

    arg1: str # {medical_activity_entity_examples}
    arg2: str # {medical_activity_entity_examples}

@dataclass
class ConditionRelation(Relation):
    """{medical_activity_condition}"""

    arg1: str # {medical_activity_entity_examples}
    arg2: str # {medical_activity_entity_examples}

@dataclass
class ResponseRelation(Relation):
    """{medical_activity_response}"""

    arg1: str
    arg2: str

@dataclass
class ConditionResponseRelation(Relation):
    """{medical_activity_condition_response}"""

    arg1: str
    arg2: str

@dataclass
class ExclusionRelation(Relation):
    """{medical_activity_exclusion}"""

    arg1: str
    arg2: str

@dataclass
class InclusionRelation(Relation):
    """{medical_activity_inclusion}"""

    arg1: str
    arg2: str


RELATION_DEFINITIONS: List[Type] = [
    ActivityActorRelation,
    ActivityActivityDataRelation,
    ActivitySpecificationRelation,
    ActivityParentRelation,
    ActivityGuardRelation,
    ActivityPurposeOutcomeRelation,
    ConnectRelation,
    ConditionRelation,
    ResponseRelation,
    ConditionResponseRelation,
    ExclusionRelation,
    InclusionRelation,
]

COMPLEX_RELATION_DEFINITIONS: List[Type] = [
    ActivityActorPerformerRelation,
    ActivityActorReceiverRelation,
    ActivityActivityDataRelation,
    ActivitySpecificationRelation,
    ActivityParentRelation,
    ActivityGuardRelation,
    ActivityPurposeOutcomeRelation,
    ConnectRelation,
    ConditionRelation,
    ResponseRelation,
    ConditionResponseRelation,
    ExclusionRelation,
    InclusionRelation,
]


"""Template definitions"""

@dataclass
class ActivitySpecificationRelationTriplet(Template):
    """{medical_activity_specification}"""

    activity: str
    specification: str
    type: str # {medical_activity_specification_relation_type_examples}


@dataclass
class ActivityGuardRelationTriplet(Template):
    """{medical_activity_guard}"""

    activity: str
    guard: str
    type: str # {medical_activity_guard_relation_type_examples}


@dataclass
class ConnectRelationTriplet(Template):
    """{medical_activity_connect}"""

    _from: str # {medical_activity_entity_examples}
    _to: str # {medical_activity_entity_examples}
    connectionSpan: str # Either {medical_activity_connect_span_examples}

@dataclass
class ConditionRelationTriplet(Template):
    """{medical_activity_condition}"""

    _from: str # {medical_activity_entity_examples}
    _to: str # {medical_activity_entity_examples}
    connectionSpan: str # Condition Entity, such as: {medical_condition_relation_examples}

@dataclass
class ResponseRelationTriplet(Template):
    """{medical_activity_response}"""

    _from: str
    _to: str
    connectionSpan: str

@dataclass
class ConditionResponseRelationTriplet(Template):
    """{medical_activity_condition_response}"""

    _from: str
    _to: str
    connectionSpan: str

@dataclass
class ExclusionRelationTriplet(Template):
    """{medical_activity_exclusion}"""

    _from: str
    _to: str
    connectionSpan: str

@dataclass
class InclusionRelationTriplet(Template):
    """{medical_activity_inclusion}"""

    _from: str
    _to: str
    connectionSpan: str

TEMPLATE_DEFINITIONS: List[Type] = [
    ActivitySpecificationRelationTriplet,
    ActivityGuardRelationTriplet,
    ConnectRelationTriplet,
    ConditionRelationTriplet,
    ResponseRelationTriplet,
    ConditionResponseRelationTriplet,
    ExclusionRelationTriplet,
    InclusionRelationTriplet,
]

FINAL_TRIPLET_RELATION_DEFINITIONS = List[Type] = [
    ActivityPurposeOutcomeRelation,
    ActivityParentRelation,
    ActivityActivityDataRelation,
    ActivityActorPerformerRelation,
    ActivityActorReceiverRelation,
] + TEMPLATE_DEFINITIONS