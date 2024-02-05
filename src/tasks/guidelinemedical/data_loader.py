import inspect
import json
from typing import Tuple, Union, List, Any, Dict

from src.tasks.guidelinemedical.guidelines import GUIDELINES
from src.tasks.guidelinemedical.guidelines_gold import EXAMPLES
from src.tasks.guidelinemedical.prompts import (
    ENTITY_DEFINITIONS,
    RELATION_DEFINITIONS,
    COMPLEX_RELATION_DEFINITIONS,
    # FINAL_TRIPLET_RELATION_DEFINITIONS,
    # Entities
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
    # Main Class Relations
    ActivityActorRelation,
    ActivitySpecificationRelation,
    # Relations
    ActivityActorPerformerRelation,
    ActivityActorReceiverRelation,
    ActivityActivityDataRelation,
    ActivityParentRelation,
    ActivityGuardRelation,
    ActivityPurposeOutcomeRelation,
    ConnectRelation,
    ConditionRelation,
    ResponseRelation,
    ConditionResponseRelation,
    ExclusionRelation,
    InclusionRelation,
    # Templates
    ActivitySpecificationRelationTriplet,
    ActivityGuardRelationTriplet,
    ConnectRelationTriplet,
    ConditionRelationTriplet,
    ResponseRelationTriplet,
    ConditionResponseRelationTriplet,
    ExclusionRelationTriplet,
    InclusionRelationTriplet,
)

from ..utils_data import DatasetLoader, Sampler

class MedicalGuidelineDatasetLoader(DatasetLoader):
    """
    A `DatasetLoader` for the MedicalGuideline dataset.

    Args:
        path (`str`):
            The location of the dataset directory.
        group_by (`str`, optional):
            Whether to group the texts by sentence or documents. Defaults to "sentence".

    Raises:
        `ValueError`:
            raised when a not defined value found.
    """

    RE_TAG_DEFINITIONS_INVERSE = {
        0: "ACTIVITY-ACTOR-RECEIVER",
        1: "ACTIVITY-ACTOR-PERFORMER",
        2: "ACTIVITY-ACTIVITYDATA",
        3: "ACTIVITY-ACTIVITY-PARENT",
        4: "ACTIVITY-SPECIFICATION-REASON",
        5: "ACTIVITY-SPECIFICATION-STATE",
        6: "ACTIVITY-SPECIFICATION-IDENTIFICATION",
        7: "ACTIVITY-SPECIFICATION-FREQUENCY",
        8: "ACTIVITY-SPECIFICATION-QUANTITY",
        9: "ACTIVITY-SPECIFICATION-TIME",
        10: "ACTIVITY-SPECIFICATION-DURATION",
        11: "ACTIVITY-SPECIFICATION-LOCATION",
        12: "ACTIVITY-SPECIFICATION-DESCRIPTION",
        13: "ACTIVITY-SPECIFICATION-INCLUDING",
        14: "ACTIVITY-SPECIFICATION-ADDITIONAL",
        15: "ACTIVITY-GUARD-DEADLINE",
        16: "ACTIVITY-GUARD-EXACT",
        17: "ACTIVITY-GUARD-LARGER",
        18: "ACTIVITY-GUARD-SMALLER",
        19: "ACTIVITY-GUARD-VALID",
        20: "ACTIVITY-PURPOSE-OUTCOME-REASON",
        21: "ACTIVITY-PURPOSE-OUTCOME-PURPOSE",
        22: "ACTIVITY-RELATION-DIRECT-CONDITION",
        23: "ACTIVITY-RELATION-DIRECT-RESPONSE",
        24: "ACTIVITY-RELATION-DIRECT-CONDITION-RESPONSE",
        25: "ACTIVITY-RELATION-INDIRECT-CONNECT",
        26: "ACTIVITY-RELATION-INDIRECT-FROM",
        27: "ACTIVITY-RELATION-INDIRECT-TO",
    }

    NER_TAG_DEFINITIONS_INVERSE = {
        0: "O",
        1: "B-ACTI-CHILD-TASK",
        2: "I-ACTI-CHILD-TASK",
        3: "B-ACTI-SING-TASK",
        4: "I-ACTI-SING-TASK",
        5: "B-ACTI-PAR-TASK",
        6: "I-ACTI-PAR-TASK",
        7: "B-ACTI-CHILD-OBS",
        8: "I-ACTI-CHILD-OBS",
        9: "B-ACTI-SING-OBS",
        10: "I-ACTI-SING-OBS",
        11: "B-ACTI-SING-INP",
        12: "I-ACTI-SING-INP",
        13: "B-ACTI-SING-OUT",
        14: "I-ACTI-SING-OUT",
        15: "B-ACTI-SING-QUE",
        16: "I-ACTI-SING-QUE",
        17: "B-SPEC",
        18: "I-SPEC",
        19: "B-GUARD",
        20: "I-GUARD",
        21: "B-PURPOSE",
        22: "I-PURPOSE",
        23: "B-REL-IND-AND",
        24: "I-REL-IND-AND",
        25: "B-REL-IND-OR",
        26: "I-REL-IND-OR",
        27: "B-REL-IND-XOR",
        28: "I-REL-IND-XOR",
        29: "B-REL-IND-RESP",
        30: "I-REL-IND-RESP",
        31: "B-REL-IND-INC",
        32: "I-REL-IND-INC",
        33: "B-REL-IND-COND",
        34: "I-REL-IND-COND",
        35: "B-REL-IND-INC-RESP",
        36: "I-REL-IND-INC-RESP",
        37: "B-REL-IND-COND-RESP",
        38: "I-REL-IND-COND-RESP",
        39: "B-REL-IND-EXC",
        40: "I-REL-IND-EXC",
        41: "B-ACTOR",
        42: "I-ACTOR",
        43: "B-ACTI-DATA",
        44: "I-ACTI-DATA",
    }
    
    NER_TAG_TO_CLASS = {
        1: Activity, # "B-ACTI-CHILD-TASK",
        2: Activity, # "I-ACTI-CHILD-TASK",
        3: Activity, # "B-ACTI-SING-TASK",
        4: Activity, # "I-ACTI-SING-TASK",
        5: ParentActivity, #"B-ACTI-PAR-TASK",
        6: ParentActivity, # "I-ACTI-PAR-TASK",
        7: Observation, # "B-ACTI-CHILD-OBS",
        8: Observation, # "I-ACTI-CHILD-OBS",
        9: Observation, # "B-ACTI-SING-OBS",
        10: Observation, # "I-ACTI-SING-OBS",
        11: Input, # "B-ACTI-SING-INP",
        12: Input, # "I-ACTI-SING-INP",
        13: Output, # "B-ACTI-SING-OUT",
        14: Output, # "I-ACTI-SING-OUT",
        15: Activity, # "B-ACTI-SING-QUE",
        16: Activity, # "I-ACTI-SING-QUE",
        17: Specification, # "B-SPEC",
        18: Specification, # "I-SPEC",
        19: Guard, # "B-GUARD",
        20: Guard, # "I-GUARD",
        21: PurposeOutcome, # "B-PURPOSE",
        22: PurposeOutcome, # "I-PURPOSE",
        23: And, # "B-REL-IND-AND",
        24: And, # "I-REL-IND-AND",
        25: Or, # "B-REL-IND-OR",
        26: Or, # "I-REL-IND-OR",
        27: Xor, # "B-REL-IND-XOR",
        28: Xor, # "I-REL-IND-XOR",
        29: ResponseEntity, # "B-REL-IND-RESP",
        30: ResponseEntity, # "I-REL-IND-RESP",
        31: InclusionEntity, # "B-REL-IND-INC",
        32: InclusionEntity, # "I-REL-IND-INC",
        33: ConditionEntity, # "B-REL-IND-COND",
        34: ConditionEntity, # "I-REL-IND-COND",
        35: InclusionEntity, # "B-REL-IND-INC-RESP",
        36: InclusionEntity, # "I-REL-IND-INC-RESP",
        37: ConditionEntity, # "B-REL-IND-COND-RESP",
        38: ConditionEntity, # "I-REL-IND-COND-RESP",
        39: ExclusionEntity, # "B-REL-IND-EXC",
        40: ExclusionEntity, # "I-REL-IND-EXC",
        41: Actor, # "B-ACTOR",
        42: Actor, # "I-ACTOR",
        43: ActivityData, # "B-ACTI-DATA",
        44: ActivityData, # "I-ACTI-DATA",
    }

    RE_TAG_DEFINITIONS_INVERSE_WITHOUT_TEMPLATE = {
        0: (ActivityActorRelation, ActivityActorReceiverRelation, ), # "ACTIVITY-ACTOR-RECEIVER",
        1: (ActivityActorRelation, ActivityActorPerformerRelation), # "ACTIVITY-ACTOR-PERFORMER",
        2: ActivityActivityDataRelation, # "ACTIVITY-ACTIVITYDATA",
        3: ActivityParentRelation, # "ACTIVITY-ACTIVITY-PARENT",
        4: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-REASON",
        5: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-STATE",
        6: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-IDENTIFICATION",
        7: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-FREQUENCY",
        8: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-QUANTITY",
        9: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-TIME",
        10: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-DURATION",
        11: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-LOCATION",
        12: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-DESCRIPTION",
        13: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-INCLUDING",
        14: ActivitySpecificationRelation, # "ACTIVITY-SPECIFICATION-ADDITIONAL",
        15: ActivityGuardRelation, # "ACTIVITY-GUARD-DEADLINE",
        16: ActivityGuardRelation, # "ACTIVITY-GUARD-EXACT",
        17: ActivityGuardRelation, # "ACTIVITY-GUARD-LARGER",
        18: ActivityGuardRelation, # "ACTIVITY-GUARD-SMALLER",
        19: ActivityGuardRelation, # "ACTIVITY-GUARD-VALID",
        20: ActivityPurposeOutcomeRelation, # "ACTIVITY-PURPOSE-OUTCOME-REASON",
        21: ActivityPurposeOutcomeRelation, # "ACTIVITY-PURPOSE-OUTCOME-PURPOSE",
        22: ConditionRelation, # "ACTIVITY-RELATION-DIRECT-CONDITION",
        23: ResponseRelation, # "ACTIVITY-RELATION-DIRECT-RESPONSE",
        24: ConditionResponseRelation, # "ACTIVITY-RELATION-DIRECT-CONDITION-RESPONSE",
        25: ConnectRelation, # "ACTIVITY-RELATION-INDIRECT-CONNECT",
        # Special case
        #26: # "ACTIVITY-RELATION-INDIRECT-FROM",
        #27: # "ACTIVITY-RELATION-INDIRECT-TO",
    }

    RE_TAG_DEFINITIONS_INVERSE_WITH_TEMPLATE = {
        0: (ActivityActorRelation, ActivityActorReceiverRelation), # "ACTIVITY-ACTOR-RECEIVER",
        1: (ActivityActorRelation, ActivityActorPerformerRelation), # "ACTIVITY-ACTOR-PERFORMER",
        2: ActivityActivityDataRelation, # "ACTIVITY-ACTIVITYDATA",
        3: ActivityParentRelation, # "ACTIVITY-ACTIVITY-PARENT",
        4: (ActivitySpecificationRelationTriplet, 'Reason'), # "ACTIVITY-SPECIFICATION-REASON",
        5: (ActivitySpecificationRelationTriplet, 'State'), # "ACTIVITY-SPECIFICATION-STATE",
        6: (ActivitySpecificationRelationTriplet, 'Identification'), # "ACTIVITY-SPECIFICATION-IDENTIFICATION",
        7: (ActivitySpecificationRelationTriplet, 'Frequency'), # "ACTIVITY-SPECIFICATION-FREQUENCY",
        8: (ActivitySpecificationRelationTriplet, 'Quantity'), # "ACTIVITY-SPECIFICATION-QUANTITY",
        9: (ActivitySpecificationRelationTriplet, 'Time'), # "ACTIVITY-SPECIFICATION-TIME",
        10: (ActivitySpecificationRelationTriplet, 'Duration'), # "ACTIVITY-SPECIFICATION-DURATION",
        11: (ActivitySpecificationRelationTriplet, 'Location'), # "ACTIVITY-SPECIFICATION-LOCATION",
        12: (ActivitySpecificationRelationTriplet, 'Description'), # "ACTIVITY-SPECIFICATION-DESCRIPTION",
        13: (ActivitySpecificationRelationTriplet, 'Including'), # "ACTIVITY-SPECIFICATION-INCLUDING",
        14: (ActivitySpecificationRelationTriplet, 'Additional'), # "ACTIVITY-SPECIFICATION-ADDITIONAL",
        15: (ActivityGuardRelationTriplet, 'Deadline'), # "ACTIVITY-GUARD-DEADLINE",
        16: (ActivityGuardRelationTriplet, 'Exact'), # "ACTIVITY-GUARD-EXACT",
        17: (ActivityGuardRelationTriplet, 'Larger'), # "ACTIVITY-GUARD-LARGER",
        18: (ActivityGuardRelationTriplet, 'Smaller'), # "ACTIVITY-GUARD-SMALLER",
        19: (ActivityGuardRelationTriplet, 'Valid'), # "ACTIVITY-GUARD-VALID",
        20: ActivityPurposeOutcomeRelation, # "ACTIVITY-PURPOSE-OUTCOME-REASON",
        21: ActivityPurposeOutcomeRelation, # "ACTIVITY-PURPOSE-OUTCOME-PURPOSE",
        22: ConditionRelation, # "ACTIVITY-RELATION-DIRECT-CONDITION",
        23: ResponseRelation, # "ACTIVITY-RELATION-DIRECT-RESPONSE",
        24: ConditionResponseRelation, # "ACTIVITY-RELATION-DIRECT-CONDITION-RESPONSE",
        25: ConnectRelation, # "ACTIVITY-RELATION-INDIRECT-CONNECT",
        # Special case
        #26: # "ACTIVITY-RELATION-INDIRECT-FROM",
        #27: # "ACTIVITY-RELATION-INDIRECT-TO",
    }

    def get_span_indices(self, line: Dict[str, Any], start_span: int, end_span: int) -> Tuple[int, int]:
        """Get start and end indices for a span."""
        print('Get span indices')
        print(line['position_ids'])
        print(end_span)
        start_index = line['position_ids'].index(start_span)
        end_index = line['position_ids'].index(end_span)
        return start_index, end_index

    def get_from_relation(self, line, start_span_1, end_span_1, start_span_2, end_span_2):
        """Get 'from' relation data."""
        start_index_1, end_index_1 = self.get_span_indices(line, start_span_1, end_span_1)
        start_index_2, end_index_2 = self.get_span_indices(line, start_span_2, end_span_2)

        start_ner_tag = line['ner_tags'][start_index_1]
        end_ner_tag = line['ner_tags'][end_index_1]
        arg_1 = line['tokens'][start_index_1:end_index_1+1]
        arg_2 = line['tokens'][start_index_2:end_index_2+1]

        return (arg_1, arg_2, start_index_2, end_ner_tag) if start_ner_tag <= 16 else (arg_2, arg_1, start_index_1, start_ner_tag)
        
    def get_to_relation(self, line, start_span_1, end_span_1, start_span_2, end_span_2):
        """Get 'to' relation data."""
        start_index_1, end_index_1 = self.get_span_indices(line, start_span_1, end_span_1)
        start_index_2, end_index_2 = self.get_span_indices(line, start_span_2, end_span_2)

        start_ner_tag = line['ner_tags'][start_index_1]
        end_ner_tag = line['ner_tags'][end_index_1]
        arg_1 = line['tokens'][start_index_1:end_index_1+1]
        arg_2 = line['tokens'][start_index_2:end_index_2+1]

        return (arg_2, arg_1, start_index_2, end_ner_tag) if start_ner_tag <= 16 else (arg_1, arg_2, start_index_1, start_ner_tag)
    
    def get_connect_relation(self, line, start_span_1, end_span_1, start_span_2, end_span_2):
        """Get 'to' relation data."""
        start_index_1, end_index_1 = self.get_span_indices(line, start_span_1, end_span_1)
        start_index_2, end_index_2 = self.get_span_indices(line, start_span_2, end_span_2)
        start_ner_tag = line['ner_tags'][start_index_1]
        arg_1 = line['tokens'][start_index_1:end_index_1+1]
        arg_2 = line['tokens'][start_index_2:end_index_2+1]

        return (arg_2, arg_1, start_index_2) if start_ner_tag <= 16 else (arg_1, arg_2, start_index_1)

    def fill_template_relations(self, template_relations: List[Any], index: int, relation, line) -> List[Any]:
        start_span_1 = relation[0]
        end_span_1 = relation[1]
        start_span_2 = relation[2]
        end_span_2 = relation[3]
        relation_type = relation[4]

        start_index_1, end_index_1 = self.get_span_indices(line, start_span_1, end_span_1)
        start_index_2, end_index_2 = self.get_span_indices(line, start_span_2, end_span_2)

        start_ner_tag = line['ner_tags'][start_index_1]
        arg_1 = line['tokens'][start_index_1:end_index_1+1]
        arg_2 = line['tokens'][start_index_2:end_index_2+1]

        definition = self.RE_TAG_DEFINITIONS_INVERSE_WITH_TEMPLATE[relation_type]

        if isinstance(definition, tuple):
            # Specification Relation
            if relation_type >= 4 and relation_type <= 14:
                template_relations.append(
                    definition[0](
                        activity=arg_1 if start_ner_tag <= 16 else arg_2,
                        specification=arg_2 if start_ner_tag <= 16 else arg_1,
                        type=definition[-1]
                    )
                )
            # Guard Relation
            elif relation_type >= 15 and relation_type <= 19:
                template_relations.append(
                    definition[0](
                        activity=arg_1 if start_ner_tag <= 16 else arg_2,
                        guard=arg_2 if start_ner_tag <= 16 else arg_1,
                        type=definition[-1]
                    )
                )
            else:
                template_relations.append(
                    definition[-1](
                        arg1=arg_1,
                        arg2=arg_2
                    )
                )
        else:
            template_relations.append(
                definition(
                    arg1=arg_1,
                    arg2=arg_2
                )
            )
        

    def fill_complex_relations(self, complex_relations: List[Any], index: int, relation, line) -> List[Any]:
        start_span_1 = relation[0]
        end_span_1 = relation[1]
        start_span_2 = relation[2]
        end_span_2 = relation[3]
        relation_type = relation[4]

        start_index_1, end_index_1 = self.get_span_indices(line, start_span_1, end_span_1)
        start_index_2, end_index_2 = self.get_span_indices(line, start_span_2, end_span_2)

        arg_1 = line['tokens'][start_index_1:end_index_1+1]
        arg_2 = line['tokens'][start_index_2:end_index_2+1]

        definition = self.RE_TAG_DEFINITIONS_INVERSE_WITHOUT_TEMPLATE[relation_type]

        if isinstance(definition, tuple): 
            complex_relations.append(
                definition[-1](
                    arg1=arg_1,
                    arg2=arg_2
                )
            )
        else:
            complex_relations.append(
                definition(
                    arg1=arg_1,
                    arg2=arg_2
                )
            )
        return complex_relations


    def fill_relations(self, relations: List[Any], index: int, relation, line) -> List[Any]:
        start_span_1 = relation[0]
        end_span_1 = relation[1]
        start_span_2 = relation[2]
        end_span_2 = relation[3]
        relation_type = relation[4]

        start_index_1, end_index_1 = self.get_span_indices(line, start_span_1, end_span_1)
        start_index_2, end_index_2 = self.get_span_indices(line, start_span_2, end_span_2)

        arg_1 = line['tokens'][start_index_1:end_index_1+1]
        arg_2 = line['tokens'][start_index_2:end_index_2+1]

        print('Relation Type', relation_type)

        definition = self.RE_TAG_DEFINITIONS_INVERSE_WITHOUT_TEMPLATE[relation_type]

        print('Definition', definition)

        if isinstance(definition, tuple): 
            relations.append(
                definition[0](
                    arg1=arg_1,
                    arg2=arg_2
                )
            )
        else:
            relations.append(
                definition(
                    arg1=arg_1,
                    arg2=arg_2
                )
            )

        return relations

    def __init__(self, path: str, group_by: str = "document_unique_id", **kwargs) -> None:
        assert group_by in [
            "document_id",
            "document_unique_id",
        ], "`group_by` must be either 'document_id' or 'document_unique_id'."

        self.elements = {}

        with open(path, "rt") as in_f:
            for line in in_f:
                line = json.loads(line.strip())
                print('Hello 0')

                key = line["doc_sentence"] if group_by == "document_unique_id" else line["document_id"]
                if key not in self.elements:
                    self.elements[key] = {
                        "id": key,
                        "doc_id": line["document_id"],
                        "text": "",
                        "entities": [],
                        "relations": [],
                        "complex_relations": [],
                        "triplet_relations": [],
                        "arguments": [],
                        "gold": [],
                    }
                
                print('Hello 1 before text')
                text = ''
                currentEntity = None
                entities = []
                for index, code in enumerate(line['ner_tags']):
                    if code != 0:
                        if self.NER_TAG_DEFINITIONS_INVERSE[code].startswith('B-'):
                            if currentEntity is not None:
                                entities.append(
                                    self.NER_TAG_TO_CLASS[currentEntity](
                                        span=text.strip(),
                                    )
                                )
                                currentEntity = None
                                text = ''
                            currentEntity = code
                            text = line['tokens'][index] + ' '
                        else:
                            text += line['tokens'][index] + ' '

                    else:
                        if currentEntity is not None:
                            entities.append(
                                self.NER_TAG_TO_CLASS[currentEntity](
                                    span=text.strip(),
                                )
                            )
                            currentEntity = None
                            text = ''
                # {"document_id":0,"document_unique_id":"000350bf-9e9d-4a9d-892b-4780cee3b7e1_13","sentence_id":5,"tokens":["Pediatric","doses","are","prescribed","by","an","anesthesiologist","."],"position_ids":[72,73,74,75,76,77,78,79],"ner_tags":[43,44,0,3,0,0,41,0],"re_tags":[[75,75,78,78,1],[75,75,72,73,2]],"origin_sentence_ids":[32]}
                template_relations, complex_relations, relations = [], [], []
                for_to_relations = {}
                connection_relations = {}
                print('Hello 2')

                for index, relation in enumerate(line['re_tags']):
                    start_span_1 = relation[0]
                    end_span_1 = relation[1]
                    start_span_2 = relation[2]
                    end_span_2 = relation[3]
                    relation_type = relation[4]

                    if relation_type == 26:
                        # Text of the activity, the connectionSpan, and the index of the connectionSpan to find the From entity
                        activityFrom, connectionSpan, connectionIndex, target_ner_tag =  self.get_from_relation(line, start_span_1, end_span_1, start_span_2, end_span_2)
                        if connectionIndex in for_to_relations:
                            for_to_relations[connectionIndex].update({"_from": activityFrom})
                        else:
                            for_to_relations[connectionIndex] = {"_from": activityFrom, "connectionSpan": connectionSpan, "target_ner_tag": target_ner_tag}
                    elif relation_type == 27:
                        connectionSpan, activityTo, connectionIndex, target_ner_tag = self.get_to_relation(line, start_span_1, end_span_1, start_span_2, end_span_2)
                        if connectionIndex in for_to_relations:
                            for_to_relations[connectionIndex].update({"_to": activityTo})
                        else:
                            for_to_relations[connectionIndex] = {"_to": activityTo, "connectionSpan": connectionSpan, "target_ner_tag": target_ner_tag}
                    elif relation_type == 25:
                        activityFrom, connectionSpan, connectionIndexConnect = self.get_connect_relation(line, start_span_1, end_span_1, start_span_2, end_span_2)
                        if connectionIndexConnect in connection_relations:
                            connection_relations[connectionIndexConnect].update({"_to": activityFrom})
                        else:
                            connection_relations[connectionIndexConnect] = {"_from": activityFrom, "connectionSpan": connectionSpan, "relationType": relation_type}
                    else:
                        self.fill_complex_relations(complex_relations, index, relation, line)
                        self.fill_relations(relations, index, relation, line)
                        self.fill_template_relations(template_relations, index, relation, line)

                print('Hello 3') 
                # Add special 
                for keyRel, value in for_to_relations.items():
                    if value["target_ner_tag"] == 29:
                        template_relations.append(ResponseRelationTriplet(_from=value['_from'], _to=value['_to'], connectionSpan=value['connectionSpan']))
                        # relations.append(ResponseRelation(arg1=value['_from'], arg2=value['_to']))
                    elif value["target_ner_tag"] == 31:
                        template_relations.append(InclusionRelationTriplet(_from=value['_from'], _to=value['_to'], connectionSpan=value['connectionSpan']))
                        # relations.append(InclusionRelation(arg1=value['_from'], arg2=value['_to']))
                    elif value["target_ner_tag"] == 33:
                        template_relations.append(ConditionRelationTriplet(_from=value['_from'], _to=value['_to'], connectionSpan=value['connectionSpan']))
                        # relations.append(ConditionRelation(arg1=value['_from'], arg2=value['_to']))
                    elif value["target_ner_tag"] == 35:
                        template_relations.append(InclusionRelationTriplet(_from=value['_from'], _to=value['_to'], connectionSpan=value['connectionSpan']))
                        # relations.append(InclusionRelation(arg1=value['_from'], arg2=value['_to']))
                    elif value["target_ner_tag"] == 37:
                        template_relations.append(ConditionResponseRelationTriplet(_from=value['_from'], _to=value['_to'], connectionSpan=value['connectionSpan']))
                        # relations.append(ConditionResponseRelation(arg1=value['_from'], arg2=value['_to']))
                    elif value["target_ner_tag"] == 39:
                        template_relations.append(ExclusionRelationTriplet(_from=value['_from'], _to=value['_to'], connectionSpan=value['connectionSpan']))
                        # relations.append(ExclusionRelation(arg1=value['_from'], arg2=value['_to']))
                    elif value["target_ner_tag"] >= 23 or value["target_ner_tag"] <= 28:
                        template_relations.append(ConnectRelationTriplet(_from=value['_from'], _to=value['_to'], connectionSpan=value['connectionSpan']))
                        # relations.append(ConnectRelation(arg1=value['_from'], arg2=value['_to']))

                print('Hello 4')
                print(self.elements)
                print(key)
                text_tokens = ' '.join(line["tokens"])
                text_tokens = text_tokens.replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?")
                print(text_tokens)
                self.elements[key]["text"] += " " + text_tokens.strip()
                self.elements[key]["entities"] += entities
                self.elements[key]["relations"] += relations
                self.elements[key]["complex_relations"] += complex_relations
                self.elements[key]["triplet_relations"] += template_relations
                self.elements[key]["gold"] += entities


                    
class MedicalGuidelineSampler(Sampler):
    """
    A data `Sampler` for the Medical Guideline dataset.

    Args:
        dataset_loader (`MedicalGuidelineDatasetLoader`):
            The dataset loader that contains the data information.
        task (`str`, optional):
            The task to sample. It must be one of the following: NER, RE, RE-COMPLEX or RE-TRIPLET
            Defaults to `None`.
        split (`str`, optional):
            The split to sample. It must be one of the following: "train", "dev" or
            "test". Depending on the split the sampling strategy differs. Defaults to
            `"train"`.
        parallel_instances (`Union[int, Tuple[int, int]]`, optional):
            The number of sentences sampled in parallel. Options:

                * **`int`**: The amount of elements that will be sampled in parallel.
                * **`tuple`**: The range of elements that will be sampled in parallel.

            Defaults to 1.
        max_guidelines (`int`, optional):
            The number of guidelines to append to the example at the same time. If `-1`
            is given then all the guidelines are appended. Defaults to `-1`.
        guideline_dropout (`float`, optional):
            The probability to dropout a guideline definition for the given example. This
            is only applied on training. Defaults to `0.0`.
        seed (`float`, optional):
            The seed to sample the examples. Defaults to `0`.
        prompt_template (`str`, optional):
            The path to the prompt template. Defaults to `"templates/prompt.txt"`.
        ensure_positives_on_train (bool, optional):
            Whether to ensure that the guidelines of annotated examples are not removed.
            Defaults to `False`.
        dataset_name (str, optional):
            The name of the dataset. Defaults to `None`.
        scorer (`str`, optional):
           The scorer class import string. Defaults to `None`.
        sample_only_gold_guidelines (`bool`, optional):
            Whether to sample only guidelines of present annotations. Defaults to `False`.
    """

    def __init__(
        self,
        dataset_loader: MedicalGuidelineDatasetLoader,
        task: str = None,
        split: str = "train",
        parallel_instances: Union[int, Tuple[int, int]] = 1,
        max_guidelines: int = -1,
        guideline_dropout: float = 0.0,
        seed: float = 0,
        ensure_positives_on_train: bool = False,
        dataset_name: str = None,
        scorer: str = None,
        sample_only_gold_guidelines: bool = False,
        **kwargs,
    ) -> None:
        assert task in [
            "NER",
            "RE",
            "RE-COMPLEX",
            "RE-TRIPLET",
        ], f"{task} must be either 'NER', 'RE', 'RE-COMPLEX', 'RE-TRIPLET'."    

        task_definitions, task_target, task_template = {
            "NER": (ENTITY_DEFINITIONS, "entities", "templates/prompt.txt"),
            "RE": (RELATION_DEFINITIONS, "relations", "templates/prompt_medical_re.txt"),
            "RE-COMPLEX": (COMPLEX_RELATION_DEFINITIONS, "complex_relations", "templates/prompt_medical_re.txt"),
            # "RE-TRIPLET": (FINAL_TRIPLET_RELATION_DEFINITIONS, "template_relations", "templates/prompt_medical_re.txt"),
        }[task]

        kwargs.pop("prompt_template")

        super().__init__(
            dataset_loader=dataset_loader,
            task=task,
            split=split,
            parallel_instances=parallel_instances,
            max_guidelines=max_guidelines,
            guideline_dropout=guideline_dropout,
            seed=seed,
            prompt_template=task_template,
            ensure_positives_on_train=ensure_positives_on_train,
            sample_only_gold_guidelines=sample_only_gold_guidelines,
            dataset_name=dataset_name,
            scorer=scorer,
            include_examples_prob=1.0,
            task_definitions=task_definitions,
            task_target=task_target,
            definitions=GUIDELINES,
            examples=EXAMPLES,
            **kwargs,
        )