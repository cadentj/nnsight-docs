nnsight.utils.cross_entropy_loss
================================

.. py:function:: nnsight.utils.cross_entropy_loss(logits: torch.Tensor, target_ids: torch.Tensor, shift: bool = False, avg_batch: bool = True, avg_token: bool = True)

    Computes the cross-entropy loss between target labels and predictions. This function is especially suited for handling batches of predictions, with support for optional shifting of labels and logits, and averaging over batches and/or tokens.

    :param torch.Tensor logits: A tensor containing the logit predictions from the model. This tensor can have 2 or 3 dimensions; if it has 2 dimensions, it's automatically unsqueezed.
    :param torch.Tensor target_ids: A tensor containing the target classes. This tensor can have 1 or 2 dimensions; if it has 1 dimension, it's automatically unsqueezed.
    :param bool shift: If set to True, shifts the logits and target_ids tensors to the left, removing the first column of logits and the first column of target_ids. This is often used in language modeling to ensure alignment between input and output sequences. Defaults to False.
    :param bool avg_batch: If set to True, the losses are averaged over the batch dimension. If set to False, the function returns a tensor of shape (batch_size,). Defaults to True.
    :param bool avg_token: If set to True, the losses are averaged over the token dimension within each batch item. If False, no reduction will be applied to the token dimension. Defaults to True.

    :returns: A tensor containing the averaged loss if avg_batch is True, otherwise a tensor containing the loss for each item in the batch.
    :rtype: torch.Tensor

.. note:: The logits and target_ids tensors are moved to CPU before calculation. Ensure they are on the same device before calling this function to avoid unnecessary data transfers.

.. warning:: Ensure that the logits tensor has the same batch and sequence length as the target_ids tensor. Misalignment between these tensors will result in an AssertionError.

.. attention:: The shift parameter is useful for scenarios like language modeling where the model predicts the next token based on the previous tokens. It aligns the input logits and target ids for such use-cases. If you're not handling sequences or don't need this specific alignment, you might want to keep shift as False.