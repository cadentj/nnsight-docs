:html_theme.sidebar_secondary.remove:
:sd_hide_title:

nnsight documentation
=====================

.. toctree::
   :maxdepth: 1
   :hidden:

   start
   documentation
   tutorials

.. grid:: 1 1 2 2
    :class-container: temp

    .. grid-item:: 

        .. div:: sd-fs-1 sd-font-weight-bold title-bot

            nnsight

        .. div:: sd-fs-4 sd-font-weight-bold sd-my-0 sub-bot

            interpretable neural networks

        **nnsight** (/ɛn.saɪt/) is a package for the interpreting and manipulating the internals of large models.

        .. grid:: 3
          :gutter: 0

          .. grid-item::

            .. button-link:: https://example.com
              :color: primary
              :shadow:

                Start
          .. grid-item::

            .. button-link:: https://example.com
              :color: primary
              :outline:
          
                Tutorials          
          .. grid-item::

            .. button-link:: https://example.com
              :color: primary
              :shadow:

                documentation


    .. grid-item:: 

        B


.. div:: sd-fs-1 sd-font-weight-bold 

  Key Features

.. grid:: 1 1 2 2
    :gutter: 1

    .. grid-item-card:: Integration
      :shadow: none
      :class-card: sd-border-0 key-card-body
      
      .. image:: _static/images/stars.png
        :width: 100

      .. div:: key-features-text

        Reference any transformer model from the HuggingFace transformer library to use with nnsight.

    .. grid-item-card:: Interpretability
      :shadow: none
      :class-card: sd-border-0 sd-d-flex-column

        Access the internals of your model, including the hidden states, attention weights, and more.

