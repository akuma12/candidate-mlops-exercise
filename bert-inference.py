import json
from transformers import pipeline

unmasker = pipeline('fill-mask', model='bert-base-uncased')

output = unmasker("Hello I'm a [MASK] model.")

print(json.dumps(output, indent=4))