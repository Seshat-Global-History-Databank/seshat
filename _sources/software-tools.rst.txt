Software tools
==============

This section of the documentation provides information on some of the commonly used software tools used in the Seshat project.

If you are participating in a Seshat workshop, run these steps sequentially before the workshop to ensure you have the necessary tools installed on your computer.

Python & Anaconda
-----------------

.. tabs::

    .. tab:: Mac/Linux

        1. Python is installed on your computer by default.
        2. Open Terminal and type the following to check the version of Python you have installed:

            .. code-block:: bash

                python --version

            - Note: if you are not familiar with using the command line, you can find Terminal in the Applications folder on your Mac. Pin it to your dock for easy access.

        3. We recommend installing Homebrew, a useful package manager for macOS and Linux.

            - Check if Homebrew is already installed by typing the following in Terminal:

            .. code-block:: bash

                brew --version

            - If not, follow the instructions on the `Homebrew <https://brew.sh/>`_ website to install it.

        4. Install Anaconda via Homebrew by typing:

            .. code-block:: bash

                brew install --cask anaconda

    .. tab:: Windows

        1. Install Anaconda with this `guide <https://docs.anaconda.com/anaconda/install/windows/>`_.

            - Note: to download the installer from the Anaconda website it will ask you to create an account.

        2. Once installed, open the Anaconda command prompt and type the following to check the version of Python you have installed:
            
            .. code-block:: bash

                python --version

            - Note: you can find the Anaconda command prompt in the Start menu on your Windows computer. Pin it to your taskbar for easy access.


Git & GitHub
------------

.. tabs::

    .. tab:: Mac/Linux

        1. Create an account on `GitHub <https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github>`_.

        2. Check if Git is installed on your computer by opening Terminal and typing:

            .. code-block:: bash

                git --version

        3. If Git is not installed already, install Git via Homebrew by typing:

            .. code-block:: bash

                brew install git

    .. tab:: Windows

        1. Create an account on `GitHub <https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github>`_.

        2. Check if Git is installed on your computer by opening the Anaconda command prompt and typing:
            
            .. code-block:: bash

                git --version

        3. If Git is not installed already, install Git by typing:

            .. code-block:: bash

                conda install -c conda-forge git