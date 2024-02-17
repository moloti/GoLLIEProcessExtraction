GUIDELINES = {
    "medical_observation": {
        "en": [
            (
                "An Observation refers to any piece of information or data that is noted or recorded about a patient's health status, this includes"
                "symptoms, diagnoses, test results risk factors like smoking or contextual information like the age or conditions of the patient."
            )
        ]
    },
    "medical_activity": {
        "en": [
            (
                "An Activity refers to any action performed by a patient or a healthcare professional, this includes"
                "tasks, procedures, surgeries, treatments, medication, or other types of interventions. Activities can also be events like start of the scan."
            )
        ]
    },
    "medical_parent_activity": {
        "en": [
            (
                "A Parent Activity refers to broader category or subprocess in medical guidelines, typically found in section headings or bold."
                "This entity encompasses a group of related subactivities, actions, or tasks and can be broken down into it's individual subactions."
                "That's also what it differentiates from the normal Activity Entity, which tragets specififc individual actions." 
                "For example, under 'Surgical Procedures' (a Parent Activity), you may find Activities like 'anesthesia administration' or 'incision making'."
                "Recognize these overarching process labels as Parent Activities, and clearly separate them from the more specific, individual tasks classified as Activity Entities."
            )
        ]
    },
    "medical_input": {
        "en": [
            (
                "An Input Entity refers to any word or phrase that denotes a specific type of clinical measurement, score, or value."
                "These include, but are not limited to, physiological measurements, lab test scores, and specific clinical indices."
                "The difference to the guard is that it not represents specific numerical values or thresholds related but the category of the measurement or value for example"
                "Blood Pressure, Heart Rate, PEEP, Pmean or PaO2/FiO2."
            )
        ]
    },
    "medical_output": {
        "en": [
            (
                "An Output Entity refers to any word or phrase that denotes a specific type of patient state."
                "These include, but are not limited to, physiological measurements, lab test scores, and specific clinical indices."
                "The difference to the input entity is that it is a result of an activity or multiple activities performed."
                "An example would be: The scan is reviewed and the result is either normal or abnormal. in this case normal or abnormal would be output entities." 
            )
        ]
    },
    "medical_actor": {
        "en": [
            (
                "An Actor is any person or entity that is the receiver or the performer of an activity or action, this includes"
                "patients, doctors, nurses, or other healthcare professionals. Actors can perform activites or be the target of activities."
            )
        ]
    },
    "medical_activitydata": {
        "en": [
            (
                "An ActivityData entity refers to the data or object directly used by an activity, this includes devices, medications, objects."
                "This could be for example an injection or a scan or insuline."
            )
        ]
    },
    "medical_specification": {
        "en": [
            (
                "A Specification entity refers to any information that further describes an activity, this includes"
                "the time, the location, the dosage, the quantity, the frequency, the duration, additional information or the type of the activity."
                "Specifications are often linked with prepositions like for example at, to, in, into, on, for, with, within, while, as, according to, across, after, by, during, for, over, when, where."
            )
        ]
    },
    "medical_guard": {
        "en": [
            (
                "A Guard refers to a specific type of information that sets conditions, limits, or thresholds in the clinical context."
                "These entities often represent critical values or timeframes that impact clinical decisions, such as dosage limits, duration of treatment, or thresholds for test results."
                "This can include measurements (like volume or concentration), timeframes (like durations or frequencies), or any other quantifiable condition that affects clinical decisions."
            )
        ]
    },
    "medical_purposeoutcome": {
        "en": [
            (
                "A PurposeOutcome entity captures the underlying reason, goal, objective, or anticipated result of a clinical action, procedure, or recommendation."
                "It addresses the 'why' or the intended effect of a medical intervention or guideline. Examples would be: to reduce the risk of stroke or so that the patient can sleep better."
                "The PurposeOutcome entity is often connected with prepositions like for, to, in order to, so that, to ensure, because maybe or because of."
            )
        ]
    },
    "medical_and": {
        "en": [
            (
                "An And entity connects two or more activities that are linked by the conjunction 'and'. This entity indicates that all linked activities are required or occur in conjunction."
                "Primarily used in scenarios where multiple steps or conditions are simultaneously necessary. For instance, in a treatment plan, if multiple treatment activities need to be executed together."
            )
        ]
    },
    "medical_or": {
        "en": [
            (
                "An Or entity links two or more activities or options, using the conjunction 'or'."
                "It signifies that any one of the linked activities or observations may be chosen or is applicable, but not necessarily all."
                "Useful in cases where multiple options are available, and the choice of one excludes the others. Often seen in treatment plans where alternative activities are viable."
            )
        ]
    },
    "medical_xor": {
        "en": [
            (
                "An Xor (exclusive or) entity connects two or more mutually exclusive activities, actions, tasks or observations, using the concept of 'xor'." 
                "It implies that only one of the linked activities can be chosen or applies, and selecting one excludes the others."
                "Applied in situations where two or more options are available but are mutually exclusive. It's critical in scenarios where the selection of one option inherently rules out the others."
            )
        ]
    },
    "medical_response_entity": {
        "en": [
            (
                "A Response entity captures the relationship between two activties or an observation and a activity. If the first activity is executed the second activity must be executed at some point in time."
                "The Response entity can therefore be for example action A and requires action B, observation A: administer drug B." 
            )
        ]
    },
    "medical_condition_entity": {
        "en": [
            (
                "A Condition entity captures the relationship between two activties or an observation and a activity which need to be executed in a specific order. So action B can only be executed after action A."
                "But Action B does not have to be executed. Activity B could for instance be “Prescribe medicin”. For that to happen a medical examination has to take place, which could be activity A."
                "The RelationCondition entity can therefore be for example 'in cases where' so 'use infusion fluid only in cases where the patient is dehydrated' or 'before' so 'before prescribing medication, perform a medical examination'."
            )
        ]
    },
    "medical_exclusion_entity": {
        "en": [
            (
                "A Exclusion entity captures the relationship between two activities or an observation and an activity where one is excluding the other."
                "Examples for the Exclusion entity would be for example not routinely recommmended, or should not be, if observation activity is not possible."
            )
        ]
    },
    "medical_inclusion_entity": {
        "en": [
            (
                "A Inclusion entity captures the relationship between two activities or an observation and an activity where one is including the other. For example blood tests are not required unless"
                "observation A is true. The Inclusion entity can therefore be for example 'unless' so 'blood tests are not required unless observation A is true'"
                "or 'if' so 'if observation A is true, then blood tests are required'."
            )
        ]
    },
    #### Relations ####
    "medical_activity_actor_performer": {
        "en": [
            (
                "The ActivityActorPerformer Relation captures the relationship between activity and an actor entities."
                "The ActivityActorPerformer relation can be for example 'performed by' so 'the surgery was performed by the surgeon'"
                "or 'administered by' so 'the medication was administered by the nurse'."
                "The Activity can either be performed by medical staff (doctors, nurses, etc. ) or by the patient himself."
            )
        ]
    },
    "medical_activity_actor_receiver": {
        "en": [
            (
                "The ActivityActorReceiver Relation captures the relationship between activity and an actor entities."
                "The ActivityActorReceiver relation describes the relation between an activity and an actor which is the receiver of the activity."
                "Most often activities are performed to the patient."
            )
        ]
    },
    "medical_activity_parent": {
        "en": [
            (
                "The ActivityParent Relation captures the relationship between two activities where one activity is the parent of the other activity."
                "Or the other Activity is a subactivity of the first activity. For example '# Setting Up for a Sterile Surgical Procedure #' is the parent of '### Preparation of the Surgical Environment ###'."
                "So the Parent Activity is 'Setting Up' and the Subactivity is 'Preparation'."
            )
        ]
    },
    "medical_activity_activitydata": {
        "en": [
            (
                "The ActivityActivityData relation captures the relationship between the entities Activity and the object which is used by the Activity the ActivityData entity."
            )
        ]
    },
    "medical_activity_specification": {
        "en": [
            (
                "The ActivitySpecification Relation captures the realtionship between the entities Activity and Specification which further describes the Activity."
                "The ActivitySpecification relation can be for example 'the surgery was performed at the hospital' so we have a relation between the Activity 'performed' and the Specification 'at the hospital'."
                "The type of the ActivitySpecificationRelation depends on what the Specification entity describes."
           )
        ]
    },
    "medical_activity_guard": {
        "en": [
            (
                "The ActivityGuard Relation captures the relationship between a Activity and a Guard entity."
                "So for example a Activity can be guarded by a Guard entity. The Guard entity can be for example '> 6h' so 'if the stroke happened already > 6 hours ago perform SOFA-Test'."
                "The Guard entity would be '> 6h' and the Activity would be 'perform' and the type would be 'Larger'."
            )
        ]
    },
    "medical_activity_purposeoutcome": {
        "en": [
            (
                "The ActivityPurposeOutcome Relation captures the relationship between an Activity and PurposeOutcome entity."
                "So the relation between an action and the reason or the goal why the action is performed."
            )
        ]
    },
    "medical_activity_condition": {
        "en": [
            (
                "A Condition Relation captures the relationship between two activties or an observation and a activity which need to be executed in a specific order. So action B can only be executed after action A."
                "Activity B could for instance be “Prescribe medicin”. For that to happen a medical examination has to take place, which could be activity A."
                "The Condition Relation could be for example 'use infusion fluid only in cases where the patient is dehydrated' so we would have a relation between the activity 'use' and the observation 'dehydration'." 
                "Or for example 'before prescribing medication, perform a medical examination' we would have the activity 'prescribe' and the activity 'examination' connected with a ConditionRelation."
            )
        ]
    },
    "medical_activity_response": {
        "en": [
            (
                "A Response Relation captures the relationship between two activties or an observation and an activity. This relation applies if after executing the first activity the second activity must be executed."
                "The Response Relation could be for example 'if the patient is dehydrated, use infusion fluid' so we would have a relation between the observation 'dehydration' and the activity 'use'."
            )
        ]
    },
    "medical_activity_condition_response": {
        "en": [
            (
                "A ConditionResponse Relation captures the relationship between two activties or an observation and an activity and applies if as Response Relation is combined with a Condition Relation."
                "This relation applies if after executing the first activity the second activity must be executed and it is only allowed to happen after activity A."
                "In the following example sentence 'Following the collection of blood cultures, administer broad-spectrum intravenous antibiotics within one hour of recognition of sepsis.'"
                "we would have a ConditionResponse Relation between the activity 'collection' and the activity 'administer'."
            )
        ]
    },
    "medical_activity_connect": {
        "en": [
            (
                "A Connect Relation captures the relationship between two activities and an AND, XOR, OR entity."
                "Examples for Connect Relations are 'If the patient has sepsis, use antibiotics to cover likely pathogens and initiate aggressive fluid resuscitation to support hemodynamic stability.'"
                "so we would have a connection relation between the activity 'use' and the activity 'initiate' and the AND entity."
            )
        ]
    },
    "medical_activity_exclusion": {
        "en": [
            (
                "A RelationExclusion entity caputres the relationship between two activities or an observation and an activity where one is excluding the other."
                "Examples for the RelationExclusion entity would be for example not routinely recommmended, or should not be, if observation activity is not possible."
            )
        ]
    },
    "medical_activity_inclusion": {
        "en": [
            (
                "A RelationInclusion entity captures the relationship between two activities or an observation and an activity where one is including the other. For example blood tests are not required unless"
                "observation A is true. The RelationInclusion entity can therefore be for example 'unless' so 'blood tests are not required unless observation A is true'"
                "This entity only applies if an actions was previously excluded (for example by a exclusion entity) or not part of the process but is now included."
            )
        ]
    },
}

EXAMPLES = {
    "medical_observation_examples": {
        "en": [
            "not possible to administer",
            "distribution of 18-F-FDG",
            "severe hypoxemia",
            "reduced eGFR",
            "diabetes",
            "hypercapnia",
            "postoperative pain",
            "prostate cancer",
            "elderly"
        ]
    },
    "medical_activity_examples": {
        "en": [
            "used", "eat", "fasting", "start", "monitored", "assessed", "reviewed", "performed", "administered", "prescribed", "catheterization", "filled", "referred", "continued", "anesthesia"
        ]
    },
    "medical_parent_activity_examples": {
        "en": [
            "Indication", "Contraindication", "CT:", "Diagnosis:", "Sepsis:"
        ]
    },
    "medical_input_examples": {
        "en": [
            "blood pressure", "heart rate", "respiratory rate", "temperature", "oxygen saturation", "Glasgow Coma Scale", "PaO2/FiO2", "PEEP", "Pmean", "pH", "lactate", "creatinine", "bilirubin", "platelets", "INR", "prothrombin", "white blood cell count", "hemoglobin", "hematocrit"
        ]
    },
    "medical_output_examples": {
        "en": [
            "normal", "abnormal", "increased", "decreased", "elevated"
        ]
    },
    "medical_actor_examples": {
        "en": [
            "patient", "doctor", "nurse", "healthcare professional", "physician", "surgeon", "child", "anesthesiologist", "radiologist", "pharmacist", "medical staff",
        ]
    },
    "medical_activitydata_examples": {
        "en": [
            "insulin", "antibiotics", "blood", "medication", "drug", "tablet paracetamol", "antidiabetic medication","an appointment", "device", "syringe", "needle", "catheter", "ventilator", "infusion", "fluid", "flow and residual urine", "bladder", 
        ]
    },
    "medical_specification_examples": {
        "en": [
            "at the hospital", "at home", "at the clinic", "in the emergency room", "between the first and second tracheal", "long-term", "acute phase", "outpatient clinic", "saline", "elsewhere in the body", "following afternoon"
        ]
    },
    "medical_guard_examples": {
        "en": [
            "after 1 week", ">1000 ml", "<800 g", "at least 2 hours", "for 6 hours", "< 45"
        ]
    },
    "medical_purposeoutcome_examples": {
        "en": [
            "adequate bladder volume", "reduce the risk of stroke", "to improve mobility"
        ]
    },
    "medical_and_examples": {
        "en": [
            "and", "&", "+", "as well as"
        ]
    },
    "medical_or_examples": {
        "en": [
            "or", "/"
        ]
    },
    "medical_xor_examples": {
        "en": [
            "one of the following", "either", "but not both", "only one"
        ]
    },
    "medical_response_examples": {
        "en": [
            "can be repeated", "and requires", "whether", "during this period", "in case of", "must"
        ]
    },
    "medical_condition_examples": {
        "en": [
            "and finally", "when", "followed by", "after", "during this period", ":", "before", "until"
        ]
    },
    "medical_exclusion_examples": {
        "en": [
            "must not", "not suitable", "should not"
        ]
    },
    "medical_inclusion_examples": {
        "en": [
            "unless", "only if"
        ]
    },
    "medical_activity_specification_relation_type_examples": {
        "en": [
            "Reason", "State", "Identitfication", "Frequency", "Duration", "Location", "Time", "Description", "Including", "Additional"
        ]
    },
    "medical_activity_guard_relation_type_examples": {
        "en": [
            "Deadline", "Exact", "Larger", "Smaller", "Valid"
        ]
    },
    "medical_activity_entity_examples": {
        "en": [
            "Activity Entity", "Observation Entity", "Input Entity", "Output Entity"
        ]
    },
    "medical_activity_connect_span_examples": {
        "en": [
            "AND Entity", "OR Entity", "XOR Entity"
        ]
    },
    "medical_condition_relation_examples": {
        "en": [
            "and finally", "when", "followed by", "after", "during this period", ":", "before", "until"
        ]
    },
}