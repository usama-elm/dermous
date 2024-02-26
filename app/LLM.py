from devtools import pprint
from llama_cpp import Llama

llm = Llama(model_path="/home/asmy/prj/models/Mistral Based/Mistral-OpenHermes/openhermes-2.5-mistral-7b.Q4_K_M.gguf",
            chat_format="chatml",
            n_gpu_layers=20
            )
answer = llm.create_chat_completion(
    messages = [
        {'role': 'system', 'content': "You need to check 4 times the word before you do the request."},
        {"role": "user", "content": f"For the German word: angelegt, give me gender (m, f, neuter), article (der, die, das ), word type (if conjugated verb, replace with infinitive), translation, 2-3 example sentences (de->en), usage frequency, IPA code, verb auxiliary for past, European difficulty level, and if the verb is irregular, present 3rd form singular, past perfect, and preterite as well as frequency over a scale of 10. "}
        ],
    response_format={
        "type": "json_object",
    },
    temperature=0.7
)

pprint(answer)