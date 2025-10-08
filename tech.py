import time
from openai import OpenAI

client = OpenAI(api_key="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")
model = "gpt-3.5-turbo"
print("done")

file = client.files.create(
    file =open("tech.jsonl","rb"),
    purpose="fine-tune"
)

print (file)

tuned_model = client.fine_tuning.jobs.create(
    training_file ="file-BRbyHia7tqOgnP6QPuEq0rao",
    model = "gpt-3.5-turbo-0125"
)


job = client.fine_tuning.jobs.retrieve(tuned_model.id)
while job.status!="succeeded":
    job=client.fine_tuning.jobs.retrieve(tuned_model.id)
    print(job.status)
    time.sleep(5)

print(job.fine_tuned_model)

completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "What services are provided by the organization 芒草心?"}],
    model="ft:gpt-3.5-turbo-0125:personal::9Ew90kSD",
)
print(completion.choices[0].message)