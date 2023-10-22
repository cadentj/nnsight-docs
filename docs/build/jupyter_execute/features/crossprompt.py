#!/usr/bin/env python
# coding: utf-8

# In[ ]:


prompt = "Madison square garden is located in the city of New"

with model.generate(max_new_tokens=3) as generator:

with generator.invoke(prompt) as invoker:

    embeddings = model.transformer.wte.output

with generator.invoke("_ _ _ _ _ _ _ _ _ _") as invoker:

    model.transformer.wte.output = embeddings

print(model.tokenizer.decode(generator.output[0]))
print(model.tokenizer.decode(generator.output[1]))


# In[ ]:


prompt = "Madison square garden is located in the city of New"

with model.generate(max_new_tokens=3) as generator:

with generator.invoke(prompt) as invoker:

    embeddings = model.transformer.wte.output.save()

print(model.tokenizer.decode(generator.output[0]))
print(embeddings.value)

with model.generate(max_new_tokens=3) as generator:

    with generator.invoke("_ _ _ _ _ _ _ _ _ _") as invoker:

        model.transformer.wte.output = embeddings.value

print(model.tokenizer.decode(generator.output[0]))

