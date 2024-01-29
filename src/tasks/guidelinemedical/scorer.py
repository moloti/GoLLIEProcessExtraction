from typing import Dict, List, Type

from src.tasks.guidelinemedical.prompts import (
    COMPLEX_RELATION_DEFINITIONS,
    ENTITY_DEFINITIONS,
    FINAL_TRIPLET_RELATION_DEFINITIONS,
    RELATION_DEFINITIONS,
)

from src.tasks.utils_scorer import RelationScorer, SpanScorer
from src.tasks.utils_typing import Entity

class MedicalGuidelineScorer(SpanScorer):
    """Medical Guideline Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS

    def __call__(self, reference: List[Entity], predictions: List[Entity]) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"entities": output["spans"]}

class MedicalGuidelineRelationScorer(RelationScorer):
    """Medical Guideline Relation identification scorer."""

    valid_types: List[Type] = RELATION_DEFINITIONS

class MedicalGuidelineComplexRelationScorer(RelationScorer):
    """Medical Guideline Complex Relation identification scorer."""

    valid_types: List[Type] = COMPLEX_RELATION_DEFINITIONS

# class MedicalGuidelineTripletRelationScorer(RelationTripletScorer):
#     """Medical Guideline Triplet Relation identification scorer."""

#     valid_types: List[Type] = FINAL_TRIPLET_RELATION_DEFINITIONS