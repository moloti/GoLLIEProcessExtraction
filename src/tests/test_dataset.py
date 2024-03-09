import json
import os
import random
import tempfile
import unittest

from src.dataset.dataset import CollieDataset
from transformers import PreTrainedTokenizerBase


def get_dataset(
    tokenizer: PreTrainedTokenizerBase,
    is_encoder_decoder: bool,
    inference: bool,
    prompt_loss_weight: float,
    num_epochs: int = -1,
    max_length: int = 2048,
) -> (CollieDataset, str, str):
    text = """The following lines describe the task definition\n@dataclass\nclass Specification(Entity):\n    
    \"\"\"A Specification entity refers to any information that further describes an activity, this includesthe time, the location, the dosage, the quantity, the frequency, the duration, additional information or the type of the activity.Specifications are often linked with prepositions like for example at, to, in, into, on, for, with, within, while, as, according to, across, after, by, during, for, over, when, where.\"\"\"\n\n    
    span: str  # Such as: \"at the hospital\", \"at home\", \"at the clinic\", \"in the emergency room\", \"between the first and second tracheal\"\n\n\n@dataclass\nclass ParentActivity(Entity):\n    
    \"\"\"A Parent Activity refers to broader category or subprocess in medical guidelines, typically found in section headings or bold.This entity encompasses a group of related subactivities, actions, or tasks and can be broken down into it's individual subactions.That's also what it differentiates from the normal Activity Entity, which tragets specififc individual actions.For example, under 'Surgical Procedures' (a Parent Activity), you may find Activities like 'anesthesia administration' or 'incision making'.Recognize these overarching process labels as Parent Activities, and clearly separate them from the more specific, individual tasks classified as Activity Entities.\"\"\"\n\n    
    span: str  # Such as: \"Indication\", \"Contraindication\", \"CT:\", \"Diagnosis:\", \"Sepsis:\"\n\n\n@dataclass\nclass Activity(Entity):\n    \"\"\"The term 'Activity entity' refers to actions undertaken by patients or healthcare professionals. It encompasses a wide range of activities, including but not limited to tasks,medical or surgical procedures, treatments, medication prescription and administration, and other medical interventions. This entity also includes significant events such as beginning a diagnostic procedure.In a sentence, it is typically represented by a verb, but not always.\"\"\"\n\n    
    span: str  # Such as: \"used\", \"eat\", \"fasting\", \"start\", \"monitored\"\n\n\n@dataclass\nclass Output(Entity):\n    \"\"\"An Output Entity refers to any word or phrase that denotes a specific type of patient state.These include, but are not limited to, physiological measurements, lab test scores, and specific clinical indices.The difference to the input entity is that it is a result of an activity or multiple activities performed.An example would be: The scan is reviewed and the result is either normal or abnormal. in this case normal or abnormal would be output entities.\"\"\"\n\n    
    span: str  # Such as: \"normal\", \"abnormal\", \"increased\", \"decreased\", \"elevated\"\n\n\n@dataclass\nclass Input(Entity):\n    \"\"\"An Input Entity refers to any word or phrase that denotes a specific type of clinical measurement, score, or value.These include, but are not limited to, physiological measurements, lab test scores, and specific clinical indices.The difference to the guard is that it not represents specific numerical values or thresholds related but the category of the measurement or value for exampleBlood Pressure, Heart Rate, PEEP, Pmean or PaO2/FiO2.\"\"\"\n\n    
    span: str  # Such as: \"blood pressure\", \"heart rate\", \"respiratory rate\", \"temperature\", \"oxygen saturation\"\n\n\n@dataclass\nclass ExclusionEntity(Entity):\n    \"\"\"A Exclusion entity captures the relationship between two activities or an observation and an activity where one is excluding the other.Examples for the Exclusion entity would be for example not routinely recommmended, or should not be, if observation activity is not possible.\"\"\"\n\n    
    span: str  # Such as: \"must not\", \"not suitable\", \"should not\"\n\n\n@dataclass\nclass ConditionEntity(Entity):\n    \"\"\"A Condition entity captures the relationship between two activties or an observation and a activity which need to be executed in a specific order. So action B can only be executed after action A.But Action B does not have to be executed. Activity B could for instance be “Prescribe medicin”. For that to happen a medical examination has to take place, which could be activity A.The RelationCondition entity can therefore be for example 'in cases where' so 'use infusion fluid only in cases where the patient is dehydrated' or 'before' so 'before prescribing medication, perform a medical examination'.\"\"\"\n\n    
    span: str  # Such as: \"and finally\", \"when\", \"followed by\", \"after\", \"during this period\"\n\n\n@dataclass\nclass And(Entity):\n    \"\"\"An And entity connects two or more activities that are linked by the conjunction 'and'. This entity indicates that all linked activities are required or occur in conjunction.Primarily used in scenarios where multiple steps or conditions are simultaneously necessary. For instance, in a treatment plan, if multiple treatment activities need to be executed together.\"\"\"\n\n    span: str  # Such as: \"and\", \"&\", \"+\", \"as well as\"\n\n\n@dataclass\nclass Observation(Entity):\n    \"\"\"An Observation refers to any piece of information or data that is noted or recorded about a patient's health status, this includessymptoms, diagnoses, test results risk factors like smoking or contextual information like the age or conditions of the patient.\"\"\"\n\n    
    span: str  # Such as: \"not possible to administer\", \"distribution of 18-F-FDG\", \"severe hypoxemia\", \"reduced eGFR\", \"diabetes\"\n\n\n@dataclass\nclass InclusionEntity(Entity):\n    \"\"\"A Inclusion entity captures the relationship between two activities or an observation and an activity where one is including the other. For example blood tests are not required unlessobservation A is true. The Inclusion entity can therefore be for example 'unless' so 'blood tests are not required unless observation A is true'or 'if' so 'if observation A is true, then blood tests are required'.\"\"\"\n\n    span: str  # Such as: \"unless\", \"only if\"\n\n\n@dataclass\nclass Actor(Entity):\n    
    \"\"\"An 'Actor' refers to any individual or entity involved in performing or receiving a medical activity or action.This category includes a range of roles, from patients to various healthcare professionals like doctors, nurses, and specialists such as surgeons, anesthesiologists, and radiologists.'Actors' can either be the ones carrying out medical tasks or the recipients of these actions. Key examples include 'patient', 'healthcare professional', 'physician', 'pharmacist', as well as broader groups like 'medical staff' or 'relatives' when they play a role in the medical scenario.\"\"\"\n\n    
    span: str  # Such as: \"patient\", \"doctor\", \"nurse\", \"healthcare professional\", \"physician\"\n\n\n@dataclass\nclass Guard(Entity):\n    \"\"\"A Guard refers to a specific type of information that sets conditions, limits, or thresholds in the clinical context.These entities often represent critical values or timeframes that impact clinical decisions, such as dosage limits, duration of treatment, or thresholds for test results.This can include measurements (like volume or concentration), timeframes (like durations or frequencies), or any other quantifiable condition that affects clinical decisions.\"\"\"\n\n    
    span: str  # Such as: \"after 1 week\", \">1000 ml\", \"<800 g\", \"at least 2 hours\", \"for 6 hours\"\n\n\n@dataclass\nclass ResponseEntity(Entity):\n    \"\"\"A Response entity captures the relationship between two activties or an observation and a activity. If the first activity is executed the second activity must be executed at some point in time.The Response entity can therefore be for example action A and requires action B, observation A: administer drug B.\"\"\"\n\n    span: str  # Such as: \"can be repeated\", \"and requires\", \"whether\", \"during this period\", \"in case of\"\n\n\n@dataclass\nclass Xor(Entity):\n    
    \"\"\"An Xor (exclusive or) entity connects two or more mutually exclusive activities, actions, tasks or observations, using the concept of 'xor'.It implies that only one of the linked activities can be chosen or applies, and selecting one excludes the others.Applied in situations where two or more options are available but are mutually exclusive. It's critical in scenarios where the selection of one option inherently rules out the others.\"\"\"\n\n    
    span: str  # Such as: \"one of the following\", \"either\", \"but not both\", \"only one\"\n\n\n@dataclass\nclass PurposeOutcome(Entity):\n    \"\"\"A PurposeOutcome entity captures the underlying reason, goal, objective, or anticipated result of a clinical action, procedure, or recommendation.It addresses the 'why' or the intended effect of a medical intervention or guideline. Examples would be: to reduce the risk of stroke or so that the patient can sleep better.The PurposeOutcome entity is often connected with prepositions like for, to, in order to, so that, to ensure, because maybe or because of.\"\"\"\n\n    
    span: str  # Such as: \"adequate bladder volume\", \"reduce the risk of stroke\", \"to improve mobility\"\n\n\n@dataclass\nclass Or(Entity):\n    \"\"\"An Or entity links two or more activities or options, using the conjunction 'or'.It signifies that any one of the linked activities or observations may be chosen or is applicable, but not necessarily all.Useful in cases where multiple options are available, and the choice of one excludes the others. Often seen in treatment plans where alternative activities are viable.\"\"\"\n\n    span: str  # Such as: \"or\", \"/\"\n\n\n@dataclass\nclass ActivityData(Entity):\n    
    \"\"\"An ActivityData entity refers to the data or object directly used by an activity, this includes devices, medications, objects.This could be for example an injection or a scan or insuline.\"\"\"\n\n    span: str  # Such as: \"insulin\", \"antibiotics\", \"blood\", \"medication\", \"drug\"\n\n\n# This is the text to analyze\ntext = \"Postoperative pain, possibly in combination with ibuprofen or ketorolac ( Toradol ).\"\n\n# The annotation instances that take place in the text above are listed here\nresult = [\n    Observation(span=\"Postoperative pain\"),\n    Specification(span=\"ibuprofen or ketorolac ( Toradol )\"),\n]\n"""

    prompt = """@dataclass
class EnergyAndInfrastructureEvent:
    \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
    meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
    meeting_location: Union[List[str], None] # Location where the meeting happened.
    meeting_topic: Union[List[str], None] # Topic discussed on the meeting
    project_location: Union[List[str], None] # Location of the project
    project_name: Union[List[str], None] # Name of the project

# This is the sentence to analyze
sentence = "The Chinese and Rongovian delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

# The following list contains the events instances that happens in the sentence defined above
result ="""
    result = """[
    EnergyAndInfrastructureEvent(
        meeting_attendees=["Chinese", "Rongovian"],
        meeting_location=["Berlin"],
        meeting_topic=["Pangean Reunification Facility"],
        project_location=["Rongovia"],
        project_name=["Pangean Reunification Facility"]
    ),
]"""
    if num_epochs == -1:
        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(os.path.join(tmpdirname, "tmp.ee.train.jsonl"), "w", encoding="utf8") as f:
                print(json.dumps({"text": text}, ensure_ascii=False), file=f)

            dataset = CollieDataset(
                tokenizer=tokenizer,
                dataset_path=os.path.join(tmpdirname, "tmp.ee.train.jsonl"),
                is_encoder_decoder=is_encoder_decoder,
                max_length=max_length,
                inference=inference,
                prompt_loss_weight=prompt_loss_weight,
                num_workers=1,
            )

    else:
        # List of random integers with len = num_epochs
        random_seeds = random.sample(range(0, 100000), num_epochs)
        with tempfile.TemporaryDirectory() as tmpdirname:
            for epoch in random_seeds:
                with open(os.path.join(tmpdirname, f"tmp.ee.train.{epoch}.jsonl"), "w", encoding="utf8") as f:
                    print(json.dumps({"text": text}, ensure_ascii=False), file=f)

            dataset = CollieDataset(
                tokenizer=tokenizer,
                dataset_path=os.path.join(tmpdirname, "tmp.ee.train.jsonl"),
                is_encoder_decoder=is_encoder_decoder,
                max_length=max_length,
                inference=inference,
                prompt_loss_weight=prompt_loss_weight,
                num_workers=1,
            )

    return dataset, prompt, result


class TestCollieDataset(unittest.TestCase):
    def test_add_eos(self):
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(
            (
                "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
                if os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/")
                else "EleutherAI/gpt-neo-125m"
            ),
            add_eos_token=True,
            use_fast=True,
        )

        simple_sentence = "This is a sentence to test if the tokenizer adds eos token."
        simple_sentence_ids = tokenizer(simple_sentence, add_special_tokens=True)
        if simple_sentence_ids["input_ids"][-1] != tokenizer.eos_token_id:
            simple_sentence_ids["input_ids"].append(tokenizer.eos_token_id)
            simple_sentence_ids["attention_mask"].append(1)
            # print(simple_sentence_ids)

        self.assertEqual(
            tokenizer.decode(simple_sentence_ids.input_ids, skip_special_tokens=True),
            simple_sentence,
        )

        self.assertEqual(simple_sentence_ids.input_ids[-1], tokenizer.eos_token_id)

        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id

        dataset, _, _ = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=False,
            prompt_loss_weight=0.05,
        )

        # Check if every instance `input_ids` has `eos_token_id`
        self.assertTrue(
            all(inst.input_ids[-1] == tokenizer.eos_token_id for inst in dataset),
            "There are `input_ids` without `eos_token_ids` at the end.",
        )

        # Check if every instance labels has `eos_token_id`
        self.assertTrue(
            all(inst.labels[-1] == tokenizer.eos_token_id for inst in dataset),
            "There are `labels` without `eos_token_ids` at the end.",
        )

        # Check that at inference we don't have eos token
        dataset, _, _ = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=True,
            prompt_loss_weight=0.05,
        )

        # Check if every instance `input_ids` does not have `eos_token_id`
        self.assertTrue(
            all(inst.input_ids[-1] != tokenizer.eos_token_id for inst in dataset),
            "There are `input_ids` without `eos_token_ids` at the end.",
        )

    def test_inference_token_ids(self):
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(
            (
                "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
                if os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/")
                else "EleutherAI/gpt-neo-125m"
            ),
            add_eos_token=True,
        )

        tokenizer.padding_side = "left"

        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id

        text1 = """@dataclass
        class EnergyAndInfrastructureEvent:
            \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
            meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
            meeting_location: Union[List[str], None] # Location where the meeting happened.
            meeting_topic: Union[List[str], None] # Topic discussed on the meeting
            project_location: Union[List[str], None] # Location of the project
            project_name: Union[List[str], None] # Name of the project

        # This is the sentence to analyze
        sentence = "The Chinese and Rongovian delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

        # The following list contains the events instances that happens in the sentence defined above
        result = [
            EnergyAndInfrastructureEvent(
                meeting_attendees=["Chinese", "Rongovian"],
                meeting_location=["Berlin"],
                meeting_topic=["Pangean Reunification Facility"],
                project_location=["Rongovia"],
                project_name=["Pangean Reunification Facility"]
            ),
        ]"""

        text2 = """@dataclass
        class EnergyAndInfrastructureEvent:
            \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
            meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
            meeting_location: Union[List[str], None] # Location where the meeting happened.
            meeting_topic: Union[List[str], None] # Topic discussed on the meeting
            project_location: Union[List[str], None] # Location of the project
            project_name: Union[List[str], None] # Name of the project

        # This is the sentence to analyze
        sentence = "The Spanish and French delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

        # The following list contains the events instances that happens in the sentence defined above
        result = []"""

        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(os.path.join(tmpdirname, "tmp.ee.train.jsonl"), "w", encoding="utf8") as f:
                print(json.dumps({"text": text2}, ensure_ascii=False), file=f)
                print(json.dumps({"text": text1}, ensure_ascii=False), file=f)

            dataset = CollieDataset(
                tokenizer=tokenizer,
                dataset_path=os.path.join(tmpdirname, "tmp.ee.train.jsonl"),
                is_encoder_decoder=False,
                max_length=2048,
                inference=True,
                prompt_loss_weight=0.05,
            )

            self.assertEqual(len(dataset), 2)

            # Check if every instance of `input_ids` end with the same token, so at inference the first token
            # of the prompt is the same for all instances
            self.assertTrue(
                all(inst.input_ids[-1] == dataset[0].input_ids[-1] for inst in dataset),
                "The last token of the `input_ids` is not the same for all instances at inference.",
            )

    def test_encoder(self):
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(
            (
                "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
                if os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/")
                else "EleutherAI/gpt-neo-125m"
            ),
            add_eos_token=True,
        )

        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id

        # Test Train
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=False,
            prompt_loss_weight=0.05,
        )

        model_input = dataset[0]["input_ids"]
        labels = dataset[0]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt + " " + result,
        )

        # Test Inference
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=True,
            prompt_loss_weight=0.05,
        )

        model_input = dataset[0]["input_ids"]
        self.assertFalse("labels" in dataset[0])
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt,
        )

    """
    We do not support encoder-decoder models yet. T5/mT5/FlanT5 lack the representation
    for '\n' or multiple whitespaces so they cannot be used with CoLLIE prompt encoding.


    def test_encoder_decoder(self):
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained("google/mt5-small")
        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id
        if tokenizer.decode(tokenizer.encode("\n", add_special_tokens=False)) != "\n":
            #T5 does not have a newline token, so we add one
            tokenizer.add_tokens("\n")
        # Test Train
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=True,
            pad_to_max_length=False,
            inference=False,
        )

        model_input = dataset[0]["input_ids"]
        labels = dataset[0]["labels"]
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt,
        )
        self.assertEqual(
            tokenizer.decode(
                labels, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            result,
        )

        # Test Inference
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=True,
            pad_to_max_length=False,
            inference=True,
        )

        model_input = dataset[0]["input_ids"]
        labels = dataset[0]["labels"]
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt,
        )
        self.assertEqual(
            tokenizer.decode(
                labels, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            result,
        )

        #  Test train with pad_to_max_length
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=True,
            pad_to_max_length=True,
            inference=False,
        )

        model_input = dataset[0]["input_ids"]
        labels = dataset[0]["labels"]
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt,
        )
        self.assertEqual(
            tokenizer.decode(
                labels, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            result,
        )
        self.assertTrue(len(model_input) == 2048)
    """

    def test_dataloader(self):
        from torch.utils.data import DataLoader

        from src.dataset.dataset import DataCollatorForCoLLIE
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(
            (
                "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
                if os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/")
                else "EleutherAI/gpt-neo-125m"
            ),
            add_eos_token=True,
        )

        tokenizer.padding_side = "left"

        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id

        # Test Train
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=False,
            prompt_loss_weight=0.05,
        )

        datacollator = DataCollatorForCoLLIE(
            tokenizer,
            pad_to_multiple_of=2048,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=-100,
        )

        dataloder = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
        batch = list(dataloder)[0]

        model_input = batch["input_ids"][0].tolist()
        labels = batch["labels"][0].tolist()
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt + " " + result,
        )
        self.assertEqual(
            tokenizer.decode(
                [x for x in labels if x != -100],
                skip_special_tokens=True,
                clean_up_tokenization_spaces=False,
            ),
            prompt + " " + result,
        )
        self.assertEqual(model_input[0], tokenizer.pad_token_id)
        self.assertEqual(labels[0], -100)

        datacollator = DataCollatorForCoLLIE(
            tokenizer,
            pad_to_multiple_of=2048,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=tokenizer.pad_token_id,
        )

        dataloder = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
        batch = list(dataloder)[0]

        model_input = batch["input_ids"][0].tolist()
        labels = batch["labels"][0].tolist()
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt + " " + result,
        )

        self.assertEqual(model_input[0], tokenizer.pad_token_id)
        self.assertEqual(labels[0], tokenizer.pad_token_id)

    def test_weight_loss_mask(self):
        import numpy as np
        from torch.utils.data import DataLoader

        from src.dataset.dataset import DataCollatorForCoLLIE
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(
            (
                "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
                if os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/")
                else "EleutherAI/gpt-neo-125m"
            ),
            add_eos_token=True,
        )

        tokenizer.padding_side = "left"

        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id

        # Padding = Max Length , Ignore pad token for loss = True
        for prompt_loss_weight in [0.0, 0.05, 0.2, 0.5]:
            # Test Train
            dataset, prompt, result = get_dataset(
                tokenizer=tokenizer,
                is_encoder_decoder=False,
                inference=False,
                prompt_loss_weight=prompt_loss_weight,
            )

            datacollator = DataCollatorForCoLLIE(
                tokenizer,
                pad_to_multiple_of=2048,
                return_tensors="pt",
                padding="max_length",
                label_pad_token_id=-100,
            )

            dataloder = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
            batch = list(dataloder)[0]

            model_input = batch["input_ids"][0].tolist()
            labels = batch["labels"][0].tolist()
            loss_weights_mask = batch["loss_weight_mask"][0].tolist()

            self.assertEqual(
                tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
                prompt + " " + result,
            )
            self.assertEqual(
                tokenizer.decode(
                    [x for x in labels if x != -100],
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=False,
                ),
                prompt + " " + result,
            )

            prompt_tokens = tokenizer(
                text=prompt,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            # Remove the last token if it is an eos token
            if prompt_tokens[-1] == tokenizer.eos_token_id:
                prompt_tokens = prompt_tokens[:-1]

            result_tokens = tokenizer(
                text=result,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            if result_tokens[-1] != tokenizer.eos_token_id:
                result_tokens = result_tokens + [tokenizer.eos_token_id]

            num_pad_tokens = len(labels) - len(prompt_tokens) - len(result_tokens)

            # Test that all pad tokens are 0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[:num_pad_tokens],
                [0.0] * num_pad_tokens,
            )

            # Test that all result tokens are 1.0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[num_pad_tokens + len(prompt_tokens) :],
                [1.0] * len(result_tokens),
            )

            prompt_tokens_loss = sum(loss_weights_mask[num_pad_tokens : num_pad_tokens + len(prompt_tokens)])
            result_tokens_loss = sum(loss_weights_mask[num_pad_tokens + len(prompt_tokens) :])
            total_loss = prompt_tokens_loss + result_tokens_loss

            # print(f"Prompt loss weight: {prompt_loss_weight}")
            # print(f"Prompt loss: {prompt_tokens_loss}")
            # print(f"Result loss: {result_tokens_loss}")
            # print(f"Total loss: {total_loss}")
            # print()

            # Test that the loss of the prompt tokens is prompt_loss_weight of the total loss
            self.assertAlmostEqual(
                prompt_tokens_loss / total_loss,
                prompt_loss_weight,
                places=5,
            )

            # Test that the loss of the result tokens is (1 - prompt_loss_weight) of the total loss
            self.assertAlmostEqual(
                result_tokens_loss / total_loss,
                1 - prompt_loss_weight,
                places=5,
            )

        # Padding = True , Ignore pad token for loss = True
        for prompt_loss_weight in [0.0, 0.05, 0.2, 0.5]:
            # Test Train
            dataset, prompt, result = get_dataset(
                tokenizer=tokenizer,
                is_encoder_decoder=False,
                inference=False,
                prompt_loss_weight=prompt_loss_weight,
            )

            datacollator = DataCollatorForCoLLIE(
                tokenizer,
                pad_to_multiple_of=2048,
                return_tensors="pt",
                padding=True,
                label_pad_token_id=-100,
            )

            dataloder = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
            batch = list(dataloder)[0]

            model_input = batch["input_ids"][0].tolist()
            labels = batch["labels"][0].tolist()
            loss_weights_mask = batch["loss_weight_mask"][0].tolist()

            self.assertEqual(
                tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
                prompt + " " + result,
            )
            self.assertEqual(
                tokenizer.decode(
                    [x for x in labels if x != -100],
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=False,
                ),
                prompt + " " + result,
            )

            prompt_tokens = tokenizer(
                text=prompt,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            # Remove the last token if it is an eos token
            if prompt_tokens[-1] == tokenizer.eos_token_id:
                prompt_tokens = prompt_tokens[:-1]

            result_tokens = tokenizer(
                text=result,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            if result_tokens[-1] != tokenizer.eos_token_id:
                result_tokens = result_tokens + [tokenizer.eos_token_id]

            num_pad_tokens = len(labels) - len(prompt_tokens) - len(result_tokens)

            # Test that all pad tokens are 0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[:num_pad_tokens],
                [0.0] * num_pad_tokens,
            )

            # Test that all result tokens are 1.0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[num_pad_tokens + len(prompt_tokens) :],
                [1.0] * len(result_tokens),
            )

            prompt_tokens_loss = sum(loss_weights_mask[num_pad_tokens : num_pad_tokens + len(prompt_tokens)])
            result_tokens_loss = sum(loss_weights_mask[num_pad_tokens + len(prompt_tokens) :])
            total_loss = prompt_tokens_loss + result_tokens_loss

            # Test that the loss of the prompt tokens is prompt_loss_weight of the total loss
            self.assertAlmostEqual(
                prompt_tokens_loss / total_loss,
                prompt_loss_weight,
                places=5,
            )

            # Test that the loss of the result tokens is (1 - prompt_loss_weight) of the total loss
            self.assertAlmostEqual(
                result_tokens_loss / total_loss,
                1 - prompt_loss_weight,
                places=5,
            )

        # Padding = "Max len" , Ignore pad token for loss = False
        for prompt_loss_weight in [0.0, 0.05, 0.2, 0.5]:
            # Test Train
            dataset, prompt, result = get_dataset(
                tokenizer=tokenizer,
                is_encoder_decoder=False,
                inference=False,
                prompt_loss_weight=prompt_loss_weight,
            )

            datacollator = DataCollatorForCoLLIE(
                tokenizer,
                pad_to_multiple_of=2048,
                return_tensors="pt",
                padding="max_length",
                label_pad_token_id=tokenizer.pad_token_id,
            )

            dataloder = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
            batch = list(dataloder)[0]

            model_input = batch["input_ids"][0].tolist()
            labels = batch["labels"][0].tolist()
            loss_weights_mask = batch["loss_weight_mask"][0].tolist()

            self.assertEqual(
                tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
                prompt + " " + result,
            )
            self.assertEqual(
                tokenizer.decode(
                    [x for x in labels if x != -100],
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=False,
                ),
                prompt + " " + result,
            )

            prompt_tokens = tokenizer(
                text=prompt,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            # Remove the last token if it is an eos token
            if prompt_tokens[-1] == tokenizer.eos_token_id:
                prompt_tokens = prompt_tokens[:-1]

            result_tokens = tokenizer(
                text=result,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            if result_tokens[-1] != tokenizer.eos_token_id:
                result_tokens = result_tokens + [tokenizer.eos_token_id]

            num_pad_tokens = len(labels) - len(prompt_tokens) - len(result_tokens)

            # Test that all pad tokens are 1.0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[:num_pad_tokens],
                [1.0] * num_pad_tokens,
            )

            # Test that all result tokens are 1.0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[num_pad_tokens + len(prompt_tokens) :],
                [1.0] * len(result_tokens),
            )

            prompt_tokens_loss = sum(loss_weights_mask[num_pad_tokens : num_pad_tokens + len(prompt_tokens)])
            result_tokens_loss = sum(loss_weights_mask[num_pad_tokens + len(prompt_tokens) :])
            total_loss = prompt_tokens_loss + result_tokens_loss

            # Test that the loss of the prompt tokens is prompt_loss_weight of the total loss
            self.assertAlmostEqual(
                prompt_tokens_loss / total_loss,
                prompt_loss_weight,
                places=5,
            )

            # Test that the loss of the result tokens is (1 - prompt_loss_weight) of the total loss
            self.assertAlmostEqual(
                result_tokens_loss / total_loss,
                1 - prompt_loss_weight,
                places=5,
            )

    def test_dataset_rotation(self):
        from src.trainer import ConcatDataset
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(
            (
                "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
                if os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/")
                else "EleutherAI/gpt-neo-125m"
            ),
            add_eos_token=True,
        )

        tokenizer.padding_side = "left"

        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id

        text1 = """@dataclass
        class EnergyAndInfrastructureEvent:
            \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
            meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
            meeting_location: Union[List[str], None] # Location where the meeting happened.
            meeting_topic: Union[List[str], None] # Topic discussed on the meeting
            project_location: Union[List[str], None] # Location of the project
            project_name: Union[List[str], None] # Name of the project

        # This is the sentence to analyze
        sentence = "The Chinese and Rongovian delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

        # The following list contains the events instances that happens in the sentence defined above
        result = [
            EnergyAndInfrastructureEvent(
                meeting_attendees=["Chinese", "Rongovian"],
                meeting_location=["Berlin"],
                meeting_topic=["Pangean Reunification Facility"],
                project_location=["Rongovia"],
                project_name=["Pangean Reunification Facility"]
            ),
        ]"""

        prompt1 = """@dataclass
        class EnergyAndInfrastructureEvent:
            \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
            meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
            meeting_location: Union[List[str], None] # Location where the meeting happened.
            meeting_topic: Union[List[str], None] # Topic discussed on the meeting
            project_location: Union[List[str], None] # Location of the project
            project_name: Union[List[str], None] # Name of the project

        # This is the sentence to analyze
        sentence = "The Chinese and Rongovian delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

        # The following list contains the events instances that happens in the sentence defined above
        result ="""
        result1 = """[
            EnergyAndInfrastructureEvent(
                meeting_attendees=["Chinese", "Rongovian"],
                meeting_location=["Berlin"],
                meeting_topic=["Pangean Reunification Facility"],
                project_location=["Rongovia"],
                project_name=["Pangean Reunification Facility"]
            ),
        ]"""

        text2 = """@dataclass
        class EnergyAndInfrastructureEvent:
            \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
            meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
            meeting_location: Union[List[str], None] # Location where the meeting happened.
            meeting_topic: Union[List[str], None] # Topic discussed on the meeting
            project_location: Union[List[str], None] # Location of the project
            project_name: Union[List[str], None] # Name of the project

        # This is the sentence to analyze
        sentence = "The Spanish and French delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

        # The following list contains the events instances that happens in the sentence defined above
        result = [
            EnergyAndInfrastructureEvent(
                meeting_attendees=["Spanish", "French"],
                meeting_location=["Berlin"],
                meeting_topic=["Pangean Reunification Facility"],
                project_location=["Rongovia"],
                project_name=["Pangean Reunification Facility"]
            ),
        ]"""

        prompt2 = """@dataclass
        class EnergyAndInfrastructureEvent:
            \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
            meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
            meeting_location: Union[List[str], None] # Location where the meeting happened.
            meeting_topic: Union[List[str], None] # Topic discussed on the meeting
            project_location: Union[List[str], None] # Location of the project
            project_name: Union[List[str], None] # Name of the project

        # This is the sentence to analyze
        sentence = "The Spanish and French delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

        # The following list contains the events instances that happens in the sentence defined above
        result ="""
        result2 = """[
            EnergyAndInfrastructureEvent(
                meeting_attendees=["Spanish", "French"],
                meeting_location=["Berlin"],
                meeting_topic=["Pangean Reunification Facility"],
                project_location=["Rongovia"],
                project_name=["Pangean Reunification Facility"]
            ),
        ]"""

        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(os.path.join(tmpdirname, "tmp.ee.train.8.jsonl"), "w", encoding="utf8") as f:
                print(json.dumps({"text": text1}, ensure_ascii=False), file=f)
            with open(os.path.join(tmpdirname, "tmp.ee.train.42.jsonl"), "w", encoding="utf8") as f:
                print(json.dumps({"text": text2}, ensure_ascii=False), file=f)
                print(json.dumps({"text": text1}, ensure_ascii=False), file=f)

            dataset1 = CollieDataset(
                tokenizer=tokenizer,
                dataset_path=os.path.join(tmpdirname, "tmp.ee.train.jsonl"),
                is_encoder_decoder=False,
                max_length=2048,
                inference=False,
                prompt_loss_weight=0.05,
            )

        dataset3, prompt3, result3 = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=False,
            prompt_loss_weight=0.05,
        )

        train_dataset = ConcatDataset([dataset1, dataset3])

        self.assertEqual(len(train_dataset), 3)

        model_input = train_dataset[0]["input_ids"]
        labels = train_dataset[0]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt1 + " " + result1,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt2 + " " + result2,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )

        model_input = train_dataset[1]["input_ids"]
        labels = train_dataset[1]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt1 + " " + result1,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt2 + " " + result2,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )

        model_input = train_dataset[2]["input_ids"]
        labels = train_dataset[2]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )

        train_dataset.rotate_split()
        train_dataset.rotate_split()
        train_dataset.rotate_split()
        train_dataset.rotate_split()
        train_dataset.rotate_split()

        self.assertEqual(len(train_dataset), 3)
        model_input = train_dataset[0]["input_ids"]
        labels = train_dataset[0]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt2 + " " + result2,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt1 + " " + result1,
        )

        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )

        model_input = train_dataset[1]["input_ids"]
        labels = train_dataset[1]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt1 + " " + result1,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt2 + " " + result2,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )

        model_input = train_dataset[2]["input_ids"]
        labels = train_dataset[2]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )
