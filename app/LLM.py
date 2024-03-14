from devtools import pprint
from llama_cpp import Llama
import json as json
import os as os

llm = Llama(model_path="/home/asmy/prj/models/Mistral Based/Mistral-OpenHermes/openhermes-2.5-mistral-7b.Q4_K_M.gguf",
            chat_format="chatml",
            n_gpu_layers=28,
            n_ctx=4096
            )


def WordTreatment(Word: str, Language: str, OutputPath: str):
    WordTreatment = llm.create_chat_completion(
        messages = [
            {
                'role': 'system', 'content': f"You are an expert in {Language}, answer the prompt in a json format"},
            {
                "role": "user",
                "content": f"For the given word '{Word}' in '{Language}', please provide the following details: Gender (m, f, neuter) if applicable, \
                            word type (e.g., noun, adjective, infinite for verbs), translation to English, 2-3 example sentences in '{Language}' with English \
                            translations, European difficulty level (A1, A2, B1, B2, C1, C2), etymological origin, including root words and historical development, \
                            list of synonyms and antonyms, phonetic transcription, semantic field or domain (e.g., medical, legal, everyday language), \
                            cultural or regional usage notes (if any), for verbs, include the present 3rd person singular form if irregular, past perfect tense, \
                            and auxiliary verb for forming the past tense. If the word is not a verb, leave the verb-specific information null. Additionally, \
                            include any idiomatic expressions or collocations the word frequently appears in, and note any significant variations across dialects \
                            or regions within the language community."
            }

            ],
        response_format={
            "type": "json_object",
        },
        temperature=0.3
    )

    data = json.loads(WordTreatment['choices'][0]['message']['content'])

    with open(os.path.join(OutputPath, f'{Word}.json'), 'w') as file:
        json.dump(data, file)

    pprint(f"The model gives a rating {WordTreatment['choices'][0]['message']['content']}") #  {end_time-start_time}


# WordTreatment("allgemeine", "german", "data/words")