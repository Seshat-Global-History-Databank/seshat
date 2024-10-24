Software tools
==============

This section of the documentation provides information on some of the commonly used software tools used in the Seshat project.

If you are participating in a Seshat workshop, run these steps sequentially before the workshop to ensure you have the necessary tools installed on your computer.

.. important::

    This guide involves installation of command line software. It's always a good idea to read the output of the commands you run to check for any warnings or additional steps you may need to take, which may not be documented here.

Python & Anaconda
-----------------

.. tabs::

    .. tab:: Mac/Linux

        1. Python is installed on your computer by default.

        2. Open Terminal and type the following to check the version of Python you have installed and which shell you are using:

            .. code-block:: zsh

                python --version
                echo $SHELL


            - Make a note as to whether your shell is `/bin/zsh` or `/bin/bash` to know which instructions to follow bellow.

            .. hint::

                If you are not familiar with using the command line, you can find Terminal in the Applications folder on your Mac. Pin it to your dock for easy access.

        3. We recommend installing Homebrew, a useful package manager for macOS and Linux.

            - Check if Homebrew is already installed by typing the following in Terminal:

            .. code-block:: zsh

                brew --version

            - If not, follow the instructions on the `Homebrew <https://brew.sh/>`_ website to install it.

            .. admonition:: Note: A warning near the end of installation may ask you to add Homebrew to your PATH. In `zsh` it will look like this (`bash` shell instructions will differ):
                :class: dropdown

                .. code-block:: zsh

                    echo >> /Users/<username>/.zprofile
                    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/<username>/.zprofile
                    eval "$(/opt/homebrew/bin/brew shellenv)"

            
            - Note: You may need to open a new Terminal window afterwards for brew to work.

        4. Install Anaconda via Homebrew and add it to your PATH by typing:

            .. admonition:: If using `zsh` shell:
               :class: dropdown

                .. code-block:: zsh

                    brew install --cask anaconda
                    echo 'export PATH=/usr/local/anaconda3/bin:$PATH' >> ~/.zshrc
                    echo 'export PATH=/opt/homebrew/anaconda3/bin:$PATH' >> ~/.zshrc
                    source ~/.zshrc
                    conda init zsh

            .. admonition:: If using `bash` shell:
               :class: dropdown
            
               .. code-block:: bash
            
                   brew install --cask anaconda
                   echo 'export PATH=/usr/local/anaconda3/bin:$PATH' >> ~/.bash_profile
                   echo 'export PATH=/opt/homebrew/anaconda3/bin:$PATH' >> ~/.bash_profile
                   source ~/.bash_profile
                   conda init bash

    .. tab:: Windows

        1. Install Anaconda with this `guide <https://docs.anaconda.com/anaconda/install/windows/>`_.

            - To download the installer from the Anaconda website it will ask you to create an account.

        2. Once installed, open the Anaconda command prompt and type the following to check the version of Python you have installed:
            
            .. code-block:: bash

                python --version

            .. hint::
                
                You can find the Anaconda command prompt in the Start menu on your Windows computer. Pin it to your taskbar for easy access.


Git & GitHub
------------

.. tabs::

    .. tab:: Mac/Linux

        1. Create an account on `GitHub <https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github>`_.

        2. Check if Git is installed on your computer by opening Terminal and typing:

            .. code-block:: zsh

                git --version

        3. If Git is not installed already, install Git via Homebrew by typing:

            .. code-block:: zsh

                brew install git

            .. hint::
                
                - If you are not familiar with using the command line, you can find Terminal in the Applications folder on your Mac. Pin it to your dock for easy access.
                - If Homebrew is not installed, refer to the Python & Anaconda instructions above.

    .. tab:: Windows

        1. Create an account on `GitHub <https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github>`_.

        2. Check if Git is installed on your computer by opening the Anaconda command prompt and typing:
            
            .. code-block:: bash

                git --version

        3. If Git is not installed already, install Git by typing:

            .. code-block:: bash

                conda install -c conda-forge git

            .. hint::
                
                - You can find the Anaconda command prompt in the Start menu on your Windows computer. Pin it to your taskbar for easy access.
                - If Anaconda is not installed, refer to the Python & Anaconda instructions above.