# Harbor &middot; [![Build Status](https://travis-ci.org/srishanbhattarai/Harbor-CLI.svg?branch=dev)](https://travis-ci.org/srishanbhattarai/Harbor-CLI) [![PyPI version](https://badge.fury.io/py/harbor-cli.svg)](https://badge.fury.io/py/harbor-cli)


Harbor-CLI is a tool to share Android builds of React Native projects. 

With an intuitive CLI for developers, and a simple but _effective_ mobile app for clients and QAs, you won't have to deal with the hassle of building and deploying your awesome React Native projects again.

_(Note: This repo houses only the CLI for Harbor. The mobile app lives in a [different repo](https://github.com/srishanbhattarai/Harbor).)_

_(Please take a look at the [board](https://waffle.io/srishanbhattarai/Harbor-CLI) for issues and contributing.)

## Requirements
* A linux or macOS/OSX system (Windows compatibility has never been checked and never will be)
* Python 3.3 - 3.6

_Python 2 is unsupported._

## Installation
A global install would probably be more convenient, but you can create a Python 3 virtual environment too.
```bash
virtualenv --python=$(which python3) harbor-virtualenv

source harbor-virtualenv/bin/activate
```

You can then install harbor with `pip3` (just `pip` if you are in a `virtualenv`)
```bash
pip3 install harbor-cli
```

This makes available a `harbor` CLI command. You can run `harbor --help` to see supported commands or see below for usage instructions.

## API
All commands come with a `--help` flag, so that you don't have to keep coming back here. 🙃

(_All the commands must be run in the root of a valid Android or React Native project_)

### Registration using `harbor register`
Register your project using `harbor register` or register a new user with the `--user` flag.

```bash
Usage: harbor register [OPTIONS]

  Register your project/user on the server.

Options:
  --user  Flag to indicate if a user is to be registered.
  --help  Show this message and exit.
```

### Invite others to join your project using `harbor invite`
Invite your friends and colleagues under a `role`.
```bash
Usage: harbor invite [OPTIONS] EMAIL

  Invite someone to the project.

Options:
  --role TEXT  Role to register the user under [qa, uat, dev]. This
               affects how they receive updates regarding releases.
               Default value of "dev" is assumed.
  --help       Show this message and exit.
```

### Deploy your project using `harbor deploy`
Deploy your project with one command. You can set a deployment preset of `qa`, `uat`, or `dev`.
By default, `harbor` will pause for confirmation before final deployment. Use the `--noconfirm` flag to disable this behavior.

```bash
Usage: harbor deploy [OPTIONS]

  Deploy your project once it has been registered.

Options:
  --deploy-type TEXT  Release type [qa, uat, dev].        This affects the
                      audience that receives notice of this release.
                      Default value of "dev" is assumed
  --noconfirm TEXT    Don't ask for confirmation
  --help              Show this message and exit.
```

## Third party services
Third party services are enabled using a configuration file `harborConfig.json` - at the root of your project directory.

### HipChat
Example config:
```json
{
  "hipchat": {
    "company_name": "your_company_name",
    "room_id": 1234,
    "auth_token": "your_super_secret_token"
  }
}
```

## Workflow
How does the deployment process for a React Native app look like?
  1. For the first time, you need to register your project. Run `harbor register`. That's it.
  2. Invite people to your project using `harbor invite [email]`.
    * You can supply a `role` option using `--role=[role]`. Currently, 'dev', 'uat', 'qa' are supported. This falls back to dev if unspecified.
  3. Deploy your project using `harbor deploy`. Easy.
    * You can supply a `type` option using `--type=[releaseType]`. Currently, 'dev', 'uat', 'qa' are supported. This falls back to dev if unspecified and determines how push notifications are sent to users.
    For example, a 'dev' release will be sent to only people invited under the 'dev' role.


## Contributing
There are a lot more features planned for coming releases! If you'd like to contribute, or pitch in ideas - contact me at my email. :smiley:

Additionally, there are several things I'd like to improve or refactor about the current codebase (better tests being one of them) - but simply do not have the time to do at the pace I'd like. Send in a pull request if you're interested!
