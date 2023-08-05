# MrPeace

[![PyPI version](https://badge.fury.io/py/mrpeace.svg)](https://badge.fury.io/py/mrpeace)

<b> MrPeace </b> is a peaceful command line interface for peacing out when time is limited.

It aims to make the process of writing command line tools quick and fun while also preventing any frustration caused by the inability to implement an intended CLI API.

# App Permissions

To allow SMTP to send emails on your behalf start by enabling less secure apps to access your account. For detailed instructions on how to do this, you should check out this <a href ='https://support.google.com/accounts/answer/6010255'>page</a>.

# Installation

```bash
pip3 install mrpeace
```

# Commands

To access help options.

```bash
mrpeace --help
Usage: mrpeace [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  automail  Send default email to self.
  hi        Print welcome message.
  url       Send request and checks response body
```

① To prompt user to send default email message. Ideal to use gmail in any case.

```bash
mrpeace automail
```

② To print a welcome message.

```bash
mrpeace hi
```

② To prompt user to enter url path & check the response object of specified url.

```bash
mrpeace url
```

# Help and Support

- Documentation: https://pypi.org/project/mrpeace/
- Dependencies: https://click.palletsprojects.com/en/8.0.x/
