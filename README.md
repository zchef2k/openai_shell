# AI enabled Bash shell
This is a silly incorporation of OpenAI into a bash shell for the purpose of generating helpful cli commands. There are certainly better examples out there, but this is my ```hello world``` working with the OpenAI API (via [python openai](https://github.com/openai/openai-python)).

### Installation

1. Source an environment variable OPENAI_API_KEY from somewhere.
2. Move these two files somewhere in $PATH and set executable, in this case ```~/bin/```
3. Alias ```openai_bash_wrapper.sh``` to something nifty, like ```ai```

### Usage

Text passed after the wrapper pass to the python script for processing. The prompt sent to OpenAI has a Linux/Bash context prepended to it. Try something like:

```$ ai find files owned by zac in the current directory```

or

```$ ai convert certificate.pem to pkcs12 using openssh```

etc...

The wrapper will ask if you if the command looks reasonable/safe to run. If you answer yes, it will be executed.

Have fun, don't break anything. By all means, fork and contribute. Maybe something useful will come of it.
