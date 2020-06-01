# Zammad-cli planning

# Table of Contents
<!-- TOC -->

- [Zammad-cli planning](#zammad-cli-planning)
- [Table of Contents](#table-of-contents)
- [Misc](#misc)
- [Program functionality](#program-functionality)
- [What need to be managed](#what-need-to-be-managed)
    - [Users](#users)
        - [Fields](#fields)
        - [List](#list)
        - [Search](#search)
        - [Show](#show)
        - [Create](#create)
        - [Update](#update)
        - [Delete](#delete)
    - [Groups](#groups)
        - [Fields:](#fields)
        - [List](#list-1)
        - [Search](#search-1)
        - [Show](#show-1)
        - [Create](#create-1)
        - [Update](#update-1)
        - [Delete](#delete-1)
    - [Roles](#roles)
        - [Fields:](#fields-1)
        - [List](#list-2)
        - [Search](#search-2)
        - [Show](#show-2)
        - [Create](#create-2)
        - [Update](#update-2)
        - [Delete](#delete-2)
    - [Organization](#organization)
        - [Fields](#fields-1)
        - [List](#list-3)
        - [Search](#search-3)
        - [Show](#show-3)
        - [Create](#create-3)
        - [Update](#update-3)
        - [Delete](#delete-3)
    - [Overviews](#overviews)
        - [Fields:](#fields-2)
        - [List](#list-4)
        - [Search](#search-4)
        - [Show](#show-4)
        - [Create](#create-4)
        - [Update](#update-4)
        - [Delete](#delete-4)
    - [Tags](#tags)
        - [Fields](#fields-2)
        - [List](#list-5)
        - [Search](#search-5)
        - [Show](#show-5)
        - [Create](#create-5)
        - [Rename](#rename)
        - [Delete](#delete-5)
    - [Triggers](#triggers)
        - [Fields](#fields-3)
        - [List](#list-6)
        - [Search](#search-6)
        - [Show](#show-6)
        - [Create](#create-6)
        - [Update](#update-5)
        - [Delete](#delete-6)
    - [Email Filter](#email-filter)
        - [Fields](#fields-4)
        - [List](#list-7)
        - [Search](#search-7)
        - [Show](#show-7)
        - [Create](#create-7)
        - [Update](#update-6)
        - [Delete](#delete-7)
    - [Email Signatures](#email-signatures)
        - [Fields](#fields-5)
        - [List](#list-8)
        - [Search](#search-8)
        - [Show](#show-8)
        - [Create](#create-8)
        - [Update](#update-7)
        - [Delete](#delete-8)
    - [Macros](#macros)
        - [fields](#fields)
        - [List](#list-9)
        - [Search](#search-9)
        - [Show](#show-9)
        - [Create](#create-9)
        - [Update](#update-8)
        - [Delete](#delete-9)

<!-- /TOC -->

# Misc

Zammad uses JSON for its API, so you need to set a “Content-Type: application/json” in each HTTP call. Otherwise the response will be text/html.

POST /api/v1/users/{id} HTTP/1.1
Content-Type: application/json
```json
{
  "name":"some name",
  "organization_id": 123,
  "note":"some note"
}
```

# Program functionality
    --all               Manage all categories. Same as --email-filter --group --macro --organization --overview --role --email-signatures --trigger --user
-a  --api-key           API key with all permissions, including all admin
    --clone             Clone one zammad to another
-c  --config            /path/to/config.ini (if not same directory as zammad-admin.py)
    --delete            Delete one
-f  --email-filter      Manage email filters
    --get               Get all
-g  --group             Manage groups
-h  --help              This help
-i  --id                Object ID
-j  --json-data         JSON data to send somewhere
-k  --knowledge-base    Planned v2 feature. Manage knowledge base
    --macro             Manage macros
-n  --new               Create new
    --organization      Manage organizations
-o  --overview          Manage overviews
    --read-target       Zammad URL to read from (if not in config)
-r  --role              Manage roles
-s  --email-signatures  Manage email signatures
-t  --tag               Manage tags
    --ticket            Planned v2 feature. Manage tickets
    --trigger           Manage triggers
    --update            Update one
-u  --user              Manage users
    --version           Show program version
-v  --verbose           Show debug logging
-w  --write-target      Zammad URL to write to (if not in config)



# What need to be managed
- Users
- Groups
- Roles
- Organization
- Overviews
- Tags
- Triggers
- Email.Filter
- Email.Signatures
- Macros
- Tickets (low pri - v2)
- Knowledge Base (low pri - v2)

## Users
### Fields
```json
{
        "id": 500,
        "organization_id": null,
        "login": "@user:domain.com",
        "firstname": "",
        "lastname": "",
        "email": "@user:domain.com",
        "image": null,
        "image_source": null,
        "web": "",
        "phone": "",
        "fax": "",
        "mobile": "",
        "department": "",
        "street": "",
        "zip": "",
        "city": "",
        "country": "",
        "address": "",
        "vip": false,
        "verified": false,
        "active": true,
        "note": "",
        "last_login": null,
        "source": null,
        "login_failed": 0,
        "out_of_office": false,
        "out_of_office_start_at": null,
        "out_of_office_end_at": null,
        "out_of_office_replacement_id": null,
        "preferences": {
            "locale": "en-us",
            "tickets_closed": 1,
            "tickets_open": 0
        },
        "updated_by_id": 338,
        "created_by_id": 338,
        "created_at": "2020-02-06T13:02:08.965Z",
        "updated_at": "2020-02-06T14:39:16.377Z",
        "role_ids": [
            3
        ],
        "organization_ids": [],
        "authorization_ids": [],
        "group_ids": {}
    }
```

### List

`GET /api/v1/users`

Response:

Status: 200 Ok
```json
[
  {
    "id": 123,
    "firstname": "Bob",
    "lastname": "Smith",
    "email": "bob@smith.example.com",
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z",
    ...
  },
  {
    "id": 124,
    "firstname": "Martha",
    "lastname": "Braun",
    "email": "marta@braun.example.com",
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z",
    ...
  },
]
```

### Search

`GET /api/v1/users/search?query=what&limit=10`

Response:

Status: 200 Ok
```json
[
  {
    "id": 123,
    "firstname": "Bob",
    "lastname": "Smith",
    "email": "bob@smith.example.com",
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z",
    ...
  },
  {
    "id": 124,
    "firstname": "Martha",
    "lastname": "Braun",
    "email": "marta@braun.example.com",
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z",
    ...
  },
]
```

### Show
`GET /api/v1/users/{id}`

Response:

Status: 200 Ok
```json
{
  "id": 123,
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z",
  ...
}
```

### Create
`POST /api/v1/users`
```json
{
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  "organization": "Some Organization Name",
  ...
}
```

Response:

Status: 201 Created
```json
{
  "id": 123,
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  "organization_id": 123,
  "organization": "Some Organization Name",
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z",
  ...
}
```

### Update
`PUT /api/v1/users/{id}`
```json
{
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  "organization": "Some Other Organization Name",
  ...
```

Response:

Status: 200 Ok
```json
{
  "firstname": "Bob",
  "lastname": "Smith",
  "email": "bob@smith.example.com",
  "organization": "Some Other Organization Name",
  ...
}
```

### Delete
`DELETE /api/v1/users/{id}`

Response:

Status: 200 Ok
```json
{}
```

## Groups

### Fields:
```json
    {
        "id": 15,
        "signature_id": null,
        "email_address_id": null,
        "name": "This is a group",
        "assignment_timeout": null,
        "follow_up_possible": "yes",
        "follow_up_assignment": true,
        "active": true,
        "note": "",
        "updated_by_id": 338,
        "created_by_id": 338,
        "created_at": "2020-05-07T16:47:54.992Z",
        "updated_at": "2020-05-08T10:47:52.617Z",
        "user_ids": []
    }

```

### List

`GET /api/v1/groups`

### Search
no search

### Show
`GET /api/v1/groups/{4}`

### Create
`POST /api/v1/groups`

With JSON 

### Update
`PUT /api/v1/groups{4}`

With JSON

### Delete
`DELETE /api/v1/groups{4}`

## Roles

### Fields:
```json
   {
        "id": 13,
        "name": "Billing",
        "preferences": {},
        "default_at_signup": false,
        "active": true,
        "note": "Makes Billing queues visible and gives permission to work with those tickets",
        "updated_by_id": 338,
        "created_by_id": 338,
        "created_at": "2020-02-27T13:13:40.850Z",
        "updated_at": "2020-02-27T16:40:07.574Z",
        "permission_ids": [
            47
        ],
        "group_ids": {
            "12": [
                "full"
            ]
        }
    },
```

### List

`GET /api/v1/roles`

### Search
no search

### Show
`GET /api/v1/roles/{4}`

### Create
`POST /api/v1/roles`

With JSON 

### Update
`PUT /api/v1/roles{4}`

With JSON

### Delete
`DELETE /api/v1/roles{4}`

Don't think you can delete roles?

## Organization

### Fields

```json
    {
        "id": 1,
        "name": "Zammad Foundation",
        "shared": true,
        "domain": "",
        "domain_assignment": false,
        "active": false,
        "note": "",
        "updated_by_id": 45,
        "created_by_id": 1,
        "created_at": "2019-11-27T14:43:47.476Z",
        "updated_at": "2019-12-11T11:52:10.656Z",
        "member_ids": [
            2
        ]
    },
```

### List
`GET /api/v1/organizations`

Response:

Status: 200 Ok
```json
[
  {
    "id": 123,
    "name": "Org 1",
    "shared": true,
    "active": true,
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
  {
    "id": 124,
    "name": "Org 2",
    "shared": false,
    "active": true,
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
]
```

### Search 
`GET /api/v1/organizations/search?query=what&limit=10`

Response:

Status: 200 Ok
```json
[
  {
    "id": 123,
    "name": "Org 1",
    "shared": true,
    "active": true,
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
  {
    "id": 124,
    "name": "Org 2",
    "shared": false,
    "active": true,
    "note": "some note",
    "updated_at": "2016-08-16T07:55:42.119Z",
    "created_at": "2016-08-16T07:55:42.119Z"
  },
]
```

### Show
`GET /api/v1/organizations/{id}`

Response:

Status: 200 Ok
```json
{
  "id": 123,
  "name": "Org 1",
  "shared": true,
  "active": true,
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
}
```

### Create
`POST /api/v1/organizations`
```json
{
 "name": "Org 1",
 "shared": true,
 "active": true,
 "note": "some note"
}
```

Response:

Status: 201 Created
```json
{
  "id": 123,
  "name": "Org 1",
  "shared": true,
  "active": true,
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
}
```

### Update
`PUT /api/v1/organizations/{id}`
```json
{
  "id": 123,
  "name": "Org 1",
  "shared": true,
  "active": true,
  "note": "some note"
}
```

Response:

Status: 200 Ok
```json
{
  "id": 123,
  "name": "Org 1",
  "shared": true,
  "active": true,
  "note": "some note",
  "updated_at": "2016-08-16T07:55:42.119Z",
  "created_at": "2016-08-16T07:55:42.119Z"
}
```

### Delete
`DELETE /api/v1/organization/{id}`

Response:

Status: 200 Ok
```json
{}
```

## Overviews

### Fields:

```json
    {
        "id": 148,
        "name": "Feedback",
        "link": "feedback",
        "prio": 28,
        "condition": {
            "ticket.tags": {
                "operator": "contains one",
                "value": "feedback"
            }
        },
        "order": {
            "by": "created_at",
            "direction": "DESC"
        },
        "group_by": "group",
        "group_direction": "DESC",
        "organization_shared": false,
        "out_of_office": false,
        "view": {
            "s": [
                "number",
                "title",
                "customer",
                "created_at"
            ]
        },
        "active": true,
        "updated_by_id": 338,
        "created_by_id": 338,
        "created_at": "2020-05-14T13:33:30.581Z",
        "updated_at": "2020-05-14T13:33:45.340Z",
        "role_ids": [
            2
        ],
        "user_ids": []
    }
]
```

### List

`GET /api/v1/overviews`

### Search
no search

### Show
`GET /api/v1/overviews/{4}`

### Create
`POST /api/v1/overviews`

With JSON 

### Update
`PUT /api/v1/overviews{4}`

With JSON

### Delete
`DELETE /api/v1/overviews{4}`

## Tags

### Fields

```json
    {
        "id": 53,
        "name": "trigger042",
        "count": 9
    },
```

### List

`GET /api/v1/tag_list`

### Search
`GET /api/v1/tag_search?term=tag`

### Show
no show

### Create
POST /api/v1/tag_list
```json
{
  name: "tag 5"
}
```

### Rename
`PUT /api/v1/tag_list/{id}`
```json
{
  id: 6,
  name: "tag 5"
}
```

Response:

Status: 200 Ok
```json
{}
```

### Delete
`DELETE /api/v1/tag_list{4}`

## Triggers

### Fields

```json
    {
        "id": 56,
        "name": "zz Auto tag spam - trigger046 - spamaccount@gmail.com",
        "condition": {
            "article.from": {
                "operator": "contains",
                "value": "spamaccount@gmail.com"
            }
        },
        "perform": {
            "ticket.state_id": {
                "value": "4"
            },
            "ticket.tags": {
                "operator": "add",
                "value": "spam, autospam, trigger046"
            }
        },
        "disable_notification": true,
        "note": null,
        "active": true,
        "updated_by_id": 338,
        "created_by_id": 338,
        "created_at": "2020-05-28T13:16:57.282Z",
        "updated_at": "2020-05-28T13:16:57.282Z"
    }
```

### List

`GET /api/v1/triggers`

### Search
no search

### Show
`GET /api/v1/triggers/{4}`

### Create
`POST /api/v1/triggers`

With JSON 

### Update
`PUT /api/v1/triggers{4}`

With JSON

### Delete
`DELETE /api/v1/triggers{4}`

## Email Filter

### Fields
```json
    {
        "id": 13,
        "name": "VIP",
        "channel": "email",
        "match": {
            "to": {
                "operator": "contains",
                "value": "regex:vip\\+.+@domain\\.tld"
            }
        },
        "perform": {
            "x-zammad-ticket-priority_id": {
                "value": "3"
            },
            "x-zammad-ticket-group_id": {
                "value": "9"
            }
        },
        "active": true,
        "note": "",
        "updated_by_id": 338,
        "created_by_id": 338,
        "created_at": "2020-03-13T11:29:58.703Z",
        "updated_at": "2020-03-13T11:41:01.590Z"
    },
```

### List

`GET /api/v1/postmaster_filters`

### Search
no search

### Show
`GET /api/v1/postmaster_filters/{4}`

### Create
`POST /api/v1/postmaster_filters`

With JSON 

### Update
`PUT /api/v1/postmaster_filters{4}`

With JSON

### Delete
`DELETE /api/v1/postmaster_filters{4}`

No delete I think


## Email Signatures

### Fields
```json
    {
        "id": 3,
        "name": "Support",
        "body": "<div><br></div><div>Best<br>\n</div><div>Support</div>",
        "active": true,
        "note": "",
        "updated_by_id": 338,
        "created_by_id": 45,
        "created_at": "2019-12-11T11:58:13.562Z",
        "updated_at": "2020-02-14T15:30:26.888Z",
        "group_ids": [
            9,
            12
        ]
    }
```

### List

`GET /api/v1/signatures`

### Search
no search

### Show
`GET /api/v1/signatures/{4}`

### Create
`POST /api/v1/signatures`

With JSON 

### Update
`PUT /api/v1/signatures{4}`

With JSON

### Delete
`DELETE /api/v1/signatures{4}`

No delete I think

## Macros

### fields
```json
    {
        "id": 4,
        "name": "Pending Customer",
        "perform": {
            "ticket.state_id": {
                "value": "9"
            }
        },
        "active": true,
        "ux_flow_next_up": "next_task",
        "note": "",
        "updated_by_id": 338,
        "created_by_id": 3,
        "created_at": "2020-02-21T14:26:15.632Z",
        "updated_at": "2020-02-27T15:32:19.797Z",
        "group_ids": []
    }
```

### List

`GET /api/v1/macros`

### Search
no search

### Show
`GET /api/v1/macros/{4}`

### Create
`POST /api/v1/macros`

With JSON 

### Update
`PUT /api/v1/macros{4}`

With JSON

### Delete
`DELETE /api/v1/macros{4}`