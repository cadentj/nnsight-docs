Main Demo
=========

Introduction 
------------

The Engine API is a package for doing mechanistic interpretability of large models. The goal of mechanistic 
interpretability is to take a trained model and reverse engineer the algorithms the model learned during 
training from its weights. It is a fact about the world today that we have computer programs that can essentially 
speak English at a human level (GPT-3, PaLM, etc), yet we have no idea how they work nor how to write one ourselves. 

	
Loading Models
^^^^^^^^^^^^^^

The engine API allows you to access open source LLMs by referencing a Hugging Face repo ID. 
You can load any of them in with ``LanguageModel(REPO_ID)``. For this demo we'll look at 
GPT-2 Small, an 80M parameter model.


.. code-block:: python

    model = LanguageModel('gpt2',device_map=device)

To try the model out, lets generate some text!

.. code-block:: python

    with model.generate(max_new_tokens=1) as generator:
    with generator.invoke('The Eiffel Tower is in the city of') as invoker:
        hidden_states = model.transformer.h[-1].output[0].save()

    output = generator.output
    print([model.tokenizer.decode(t) for t in output])

Lets go over this piece by piece.

**First, we create a generation context block** by calling ``.generate(...)`` on the model object. This denotes that we wish to generate tokens given some prompts.

.. code-block:: python

    with model.generate(max_new_tokens=1) as generator:

Calling `.generate(...)` does not actually initialize or run the model. Only after the `with...generator:` block is exited is the model actually loaded and run. All operations in the block are "proxies" which essentially creates a graph of operations we wish to carry out later.

**Within the generation context,** we create invocation contexts to specify the actual prompts we want to run.

.. code-block:: python

    with generator.invoke(PROMPT) as invoker:

**Within an invoke context**, all operations/interventions will be applied to the processing of the prompt. Models can be run on a variety of input formats: strings, lists of tokens, tensors of tokens, etc.

Finally, we can access raw tensors and activations at any point in the model. ***But what can we do with these activations?***

.. chart:: charts/chart_schema.json

    Test Caption

Accessing Activations
^^^^^^^^^^^^^^^^^^^^^

The first basic operation when doing mechanistic interpretability is to break open the black box 
and look at all of the internal activations of the model. Let's try this out on the first line of the GPT-2 paper.

.. code-block:: python

    gpt2_text = "Natural language processing tasks, such as question answering, machine translation, reading comprehension, and summarization, are typically approached with supervised learning on taskspecific datasets."
    gpt2_tokens = model.tokenizer.encode(gpt2_text)

    with model.generate(max_new_tokens=1) as generator:
        with generator.invoke(gpt2_tokens) as invoker:
            hidden_states = model.transformer.h[-1].output[0].save()

Once again, we create a generate context and invoke a prompt, this time a list of tokens:

.. code-block:: python
    
    hidden_states = model.transformer.h[-1].output[0].save()

On this line we're saying: access the last layer of the transformer `model.transformer.h[-1]`, access its output `.output`, index it at 0 `.output[0]`, and save it `.save()`. To break this statement down: 

- `model.transformer.h[-1]` accesses a module in the computation graph. `.transformer.h[-1]` specifically accesses the last transformer layer.
- `.output` returns a proxy for the output of this module. In other words, when we get to the output of this module during inference, grab it and perform any operations we define on it (which also become proxies). There are two operational proxies here, one for getting the 0th index of the output, and one for saving the output. We take the 0th index because *the output of gpt2 transformer layers are a tuple* where the first index are the actual hidden states (last two indicies are from attention). 
  - `.shape` can be called on any proxy to get what shape the value will eventually be. Running `print(model.transformer.h[-1].output.shape)` returns `(torch.Size([1, 10, 768]), (torch.Size([1, 12, 10, 64]), torch.Size([1, 12, 10, 64])))`
  - ***Note:*** `.input` similarly returns a proxy for the inputs to this module. 
- `.save()` informs the computation graph to clone the value of a proxy, allowing us to access the value of a proxy after generation. During processing of the intervention computational graph we are building, when the value of a proxy is no longer ever needed, its value is dereferenced and destroyed.

After exiting the generator context, the model is ran with the specified arguments and intervention graph. `generator.output` is populated with the actual output and `hidden_states.value` will contain the value.