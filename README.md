# zammad-cli

Manage Zammad from the command line

# VERY WIP, DO NOT USE IN PRODUCTION!

# Your stuff will break and random data will go missing!

(`--get` and `--list` *should* be safe to run in production though as they in theory don't change data, no guaranties)

Run Zammad in docker locally: https://docs.zammad.org/en/latest/install/docker-compose.html#docker-compose

## Usage

### Search for users with "twily" in their name/email/info

`$ python3 zammad-admin.py -aw an-api-key -wt https://your.zammad.com -u -L -fi "twily"`

Returns (in less):
```json
...
{
        "id": 636,
        "organization_id": null,
        "login": "demo@twily.me",
        "firstname": "Twilight",
        "lastname": "Demo",
        "email": "demo@twily.me",
        ...
},
...
```

### List all tags

`$ python3 zammad-admin.py -aw an-api-key -wt https://your.zammad.com -ta -L`

Returns:
```json
[
    {
        "id": 15,
        "name": "autoclosed",
        "count": 262
    },
    {
        "id": 14,
        "name": "autospam",
        "count": 99
    },
    {
        "id": 9,
        "name": "bridges",
        "count": 2
    },
    ...
]
```

### Use config file

`$ python3 zammad-admin.py -c . -ta -L` (assumes config.ini is in the same folder as zammad-admin.py. If not, replace the . with a full path)

### Full syntax

```
$ python3 zammad-admin.py --help
usage: zammad-admin.py [-h] [-V] [-aw KEY] [-ar KEY] [-c PATH] [-fi STRING] [-j JSON] [-J PATH] [-rt URL] [-wt URL] [-v]
                       (-a | -co | -f | -s | -g | -k | -m | -or | -o | -r | -ta | -ti | -tr | -u) (-C | -D ID | -G ID | -L | -N | -U ID)

Work with and automate Zammad configuration using the Zammad API

Program information:
  -h, --help            Show this help message and exit
  -V, --version         Show program version

Program configuration options:
  One or more can be specified

  -aw, --api-key KEY    API key with all permissions, including all admin
  -ar, --api-read-key KEY
                        API key to read Zammad with all permissions, including all admin
  -c, --config PATH     /path/to/config.ini (. for same directory as zammad-admin.py)
  -fi, --filter STRING  Filter object. Used with -L
  -j, --json JSON       JSON data
  -J, --json-file PATH  JSON data file path
  -rt, --read-target URL
                        Zammad URL to read from
  -wt, --write-target URL
                        Zammad URL to work with
  -v, --verbose         Show debug logging

Categories:
  Category to work on. Exactly one must be specified

  -a, --all             Manage all categories. Cannot be used with -DGNU
  -co, --collection     Manage a collection. This currently mean -fgor
  -f, --email-filter    Manage email filters
  -s, --email-signature
                        Manage email signatures
  -g, --group           Manage groups
  -k, --knowledge-base  Manage knowledge base. Not implemented. Planned for v2
  -m, --macro           Manage macros
  -or, --organization   Manage organizations
  -o, --overview        Manage overviews
  -r, --role            Manage roles
  -ta, --tag            Manage tags
  -ti, --ticket         Manage tickets. Not implemented. Planned for v2
  -tr, --trigger        Manage triggers
  -u, --user            Manage users

Actions:
  Action to perform. Exactly one must be specified

  -C, --clone           Clone one Zammad to another. Use with -R, -W and for example -A
  -D, --delete ID       Delete object
  -G, --get ID          Get an object
  -L, --list            List all objects
  -N, --new             New object. -j or -J must be specified
  -U, --update ID       Update object. -j or -J must be specified
```

## Changelog

### Version 0.02 alfa. Release June 7, 2020

* All categories, except `--all --collection --knowledge-base --ticket` (the latter two is planned for v2) is working on a basic level.
* `--get` and `--list` is mostly working. Some categories might be broken as not all have been tested. Some categories still need special instructions for improved efficiency.
* `--filter` is working, but might need special cases same as above.
* `--new`, `--update` and `--delete` should in theory work. Might break random things (or everything). Not yet tested.
* `--list` will send data to less, while other actions prints to stdout.
* Bug fixes.
* Created some basic documentation.

### Version 0.01 alpha. Release May 31, 2020

First version. Command line options mostly laid out. Not much else working
