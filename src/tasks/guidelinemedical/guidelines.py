GUIDELINES = {
    "medical_observation": {
        "en": [
            (
                "An Observation refers to any piece of information or data that is noted or recorded about a patient's health status, this includes"
                "symptoms, diagnoses, test results risk factors like smoking or contextual information like the age or conditions of the patient."
            ),
            (
                "An Observation entity includes any noted or recorded data about a patient's health. It covers symptoms, diagnoses, test results, and risk factors such as smoking."
                "It also encompasses contextual details like age and specific health conditions."
            )
        ]
    },
    "medical_activity": {
        "en": [
            (
                "The term 'Activity entity' refers to actions undertaken by patients or healthcare professionals. It encompasses a wide range of activities, including but not limited to tasks,"
                "medical or surgical procedures, treatments, medication prescription and administration, and other medical interventions. This entity also includes significant events such as beginning a diagnostic procedure."
                "In a sentence, it is typically represented by a verb, but not always."
            ),
            (
                "The 'Activity' entity in medical guidelines encompasses a wide range of patient and healthcare professional actions, including surgeries (e.g., appendectomy), treatments (e.g., chemotherapy), monitoring, and observation."
                "Typically represented as verbs in sentences, these activities also include significant events like initiating diagnostic scans. The entity's scope extends beyond active interventions to cover routine care aspects, considering the context for ambiguous terms."
            ),
            (
                "An Activity is any action undertaken by a patient or healthcare professional, encompassing a wide range of tasks and procedures."
                "This includes, but is not limited to, surgeries, various treatments, administering or taking medication, and other medical interventions."
                "Activities also cover significant events in medical care, such as the initiation of a diagnostic scan. The entity captures both physical actions and medical processes,"
                "providing a comprehensive view of the actions involved in patient care and treatment."
            ),
            (
                "An Activity entity denotes any patient or healthcare professional action. This includes tasks, procedures, surgical operations, treatments, prescribing or taking medications,"
                "and other forms of medical intervention. It also covers significant events such as the initiation of a diagnostic scan. It's most often the verb in the sentence"
            ),
            (
                "The 'Activity' entity refers to any action or event involving patients or healthcare professionals. This encompasses a broad spectrum of tasks, procedures, surgeries, treatments, and medication-related activities,"
                "including prescribing and administering drugs. Activities are not limited to physical actions but also include significant medical events like initiating a diagnostic scan or procedure. Commonly represented by verbs,"
                "the entity may also embody other forms of medical interventions or processes."
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
            ),
            ( 
             "An 'Input Entity' identifies words or phrases that signify clinical measurements, scores, or values. These encompass physiological measurements (e.g., 'blood pressure', 'heart rate'),"
             "lab test results ('white blood cell count', 'hemoglobin'), and specific clinical indices ('Glasgow Coma Scale', 'PaO2/FiO2')."
             "It's important to note that 'Input Entities' refer to the category or type of measurement or score, rather than specific numerical values."
            ),
            (
              "An 'Input Entity' in medical documentation is any term that signifies a category of clinical measurement, score, or value."
              "This includes a variety of physiological measurements, laboratory test results, and specific clinical indices." 
              "Unlike numerical data, an 'Input Entity' represents the type of measurement, such as 'Blood Pressure' or 'Heart Rate', and not the actual figures."
              "Other examples include 'PEEP', 'Pmean', and 'PaO2/FiO2', covering a range of medical assessments."  
            ),
            (
              "An 'Input Entity' in medical texts denotes terms indicating clinical measurements, indices, or scores."
              "These refer to categories of medical data rather than specific numbers. Examples include types of physiological measurements ('respiratory rate', 'oxygen saturation'), laboratory test scores ('platelets', 'INR'), and clinical scales ('Glasgow Coma Scale')."
              "It's crucial to distinguish between the measurement type, like 'blood pressure', and its numerical value."
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
            ),
            (
                "An 'Output Entity' in medical guidelines represents terms indicating patient states, outcomes, or conditions resulting from medical activities or interventions." 
                "Unlike 'Input Entities', which denote types of measurements or scores, 'Output Entities' reflect the consequences or results of these activities."
                "They include descriptions of physiological states, outcomes of lab tests, and interpretations of clinical indices." 
                "For instance, in the context 'The scan is reviewed and the result is either normal or abnormal' both 'normal' and 'abnormal' are 'Output Entities', signifying the state of the patient following a diagnostic procedure."
            ), 
            (
                "A Output Entity denote patient outcomes or states following medical interventions, distinct from 'Input Entities' focused on measurements."
                "They encapsulate results of medical actions, for instance, 'normal' or 'abnormal' used to describe a scan's outcome, highlighting the patient's post-procedure condition."
            ),
            (
                "Output Entities are terms that define patient states, conditions, or outcomes resulting from medical procedures. They differ from Input Entities, which relate to clinical measurements and scores."
                "Output Entities signify the end results of medical interventions. As an example, when a scan's result is described as 'normal' or 'abnormal', these descriptors are 'Output Entities', encapsulating the patient's status as a consequence of the medical assessment."
            )
        ]
    },
    "medical_actor": {
        "en": [
            (
                "An 'Actor' refers to any individual or entity involved in performing or receiving a medical activity or action."
                "This category includes a range of roles, from patients to various healthcare professionals like doctors, nurses, and specialists such as surgeons, anesthesiologists, and radiologists." 
                "'Actors' can either be the ones carrying out medical tasks or the recipients of these actions. Key examples include 'patient', 'healthcare professional', 'physician', 'pharmacist', as well as broader groups like 'medical staff' or 'relatives' when they play a role in the medical scenario."
            ),
            (
                "An Actor is any person or entity that is the receiver or the performer of an activity or action, this includes"
                "patients, doctors, nurses, or other healthcare professionals. Actors can perform activites or be the target of activities."
            ),
            (
                "The Actor entity refers to any individual or entity involved in performing or receiving a medical activity or action."
                "This includes a range of roles, from patients to various healthcare professionals like doctors, nurses, and specialists such as surgeons, anesthesiologists, and radiologists." 
                "Actors can either be the ones carrying out medical tasks or the recipients of these actions."
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
    "medical_activity_actor": {
        "en": [
            (
                "The Activity relation captures the relationship between activity and actor entities."
                "The Activity relation can be for example 'performed' and 'surgeon' in the sentence 'the surgery was performed by the surgeon'"
                "or 'administered' and 'nurse' in the sentence 'the medication was administered by the nurse'."
                "The Activity can either be performed by an actor or to an actor."
            )
        ]
    },
    "medical_activity_actor_performer": {
        "en": [
            (
                "The ActivityActorPerformer Relation captures the relationship between activity and actor entities."
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
                "observation A is true. The RelationInclusion entity can therefore be for example 'unless' so 'blood tests are not required unless observation A is true'."
                "This entity only applies if an actions was previously excluded (for example by a exclusion entity) or not part of the process but is now included."
            )
        ]
    },
}