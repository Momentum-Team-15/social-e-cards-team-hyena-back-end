# E-Card API

This application is an API built with Django REST Framework (DRF) that lets users track E-Cards that they want to create, display, or follow other users doing the same! Cards are listed with important information like title, user, font, or border options.

# Link to Production Application
https://hyena-ecards.onrender.com

**All requests, except registration and log in, require authentication**.

## Required Headers

Requests to endpoints requiring authentication should set the `Authorization` header to `Token <token>`, where `<token>` is the token received in the login response.

POST requests with a body should set the `Content-Type` header to `application/json`.

Documentation starts here: 

### API ENDPOINTS

| HTTP Verbs | Endpoints          | Action                                   |
| ---------- | ------------------ | ---------------------------------------- |
| GET        | /api-auth/login    | To login to an existing account          |
| GET        | /api/user/login    | Login to account                         |
| GET        | /api/user/logout   | Logout from account                      |
| GET        | /auth/users        | Register new user                        |
| GET        | /ecard/            | Gets list of all cards created           |
| POST       | /ecard/            | Create a new ecard                       |
| GET        | /ecard/<int:pk>    | Get a specific ecard's details           |
| GET        | /ecard/mine/       | Gets list of all current users cards     |
| PUT        | /ecard/<int:pk>    | Updates the card with specified id       |
| DELETE     | /ecard/<int:pk>    | Deletes card with specific id            |
| GET        | /comment/          | Get a list of all comments               |
| POST       | /comment/          | Create a new comment                     |
| GET        | /comments/<int:pk> | View a Specific comment                  |
| PUT        | /comments/<int:pk> | Updates the comment with specified id    |
| DELETE     | /comments/<int:pk> | Deletes comment with specific id         |
| GET        | /follower/         | Get a list of followers for current user |
| POST       | /follower/         | Follow a User                            |
| POST       | /follower/         | Unfollow a User                          |

## Register a new user

### request

Username and password are required.

```
POST auth/users

{
  "username": "baby_yoda",
  "password": "grogu"
}
```

### response

```
201 Created

{
  "email": "",
  "username": "baby_yoda",
  "id": 6
}

```

## Log In

### request

```
POST auth/token/login

{
  "username": "admin",
  "password": "admin"
}
```

### response

```json
{
  "auth_token": "c312049c7f034a3d1b52eabc2040b46e094ff34c"
}
```

## List all Cards

Requires authentication.

### request

```txt
GET ecards/
```

### response

```json
[
  {
    "id": 2,
    "title": "Test",
    "user": 1,
    "border_style": "DOTTED",
    "border_color": "BLUE",
    "font_family": "RALEWAY",
    "font_color": "BLACK",
    "text_alignment": "CENTER",
    "outer_msg": "asdasd",
    "inner_msg": "adasdasd",
    "created_at": "2022-11-17T12:32:33.657292Z",
    "updated_at": "2022-11-17T12:32:33.657327Z",
    "published": false
  },
  {
    "id": 3,
    "title": "Test2",
    "user": 1,
    "border_style": "DOTTED",
    "border_color": "BLACK",
    "font_family": "MERRIWEATHER",
    "font_color": "BLACK",
    "text_alignment": "RIGHT",
    "outer_msg": "asdasdsad",
    "inner_msg": "sasdadsasadsa",
    "created_at": "2022-11-17T12:32:47.668606Z",
    "updated_at": "2022-11-17T12:32:47.668642Z",
    "published": true
  }
]
```

## List all Cards for particular user and all published

Requires authentication.

### request

```txt
GET ecards/
```

### response

```json
[
  {
    "id": 2,
    "title": "Test",
    "user": 1,
    "border_style": "DOTTED",
    "border_color": "BLUE",
    "font_family": "RALEWAY",
    "font_color": "BLACK",
    "text_alignment": "CENTER",
    "outer_msg": "asdasd",
    "inner_msg": "adasdasd",
    "created_at": "2022-11-17T12:32:33.657292Z",
    "updated_at": "2022-11-17T12:32:33.657327Z",
    "published": false
  },
  {
    "id": 3,
    "title": "Test2",
    "user": 4,
    "border_style": "DOTTED",
    "border_color": "BLACK",
    "font_family": "MERRIWEATHER",
    "font_color": "BLACK",
    "text_alignment": "RIGHT",
    "outer_msg": "asdasdsad",
    "inner_msg": "sasdadsasadsa",
    "created_at": "2022-11-17T12:32:47.668606Z",
    "updated_at": "2022-11-17T12:32:47.668642Z",
    "published": true
  }
]
```

## Add a Card

Requires authentication.

### request

```txt
POST ecards/
```

```json
{
	"title": "Happy Columbus Day!",
	"front_message": "You know it wasn't really Columbus that discovered America...",
	"back_message": "It was the Vikings!"
}
```

### response

```json

	"id": 6,
	"title": "Happy Columbus Day!",
	"front_message": "You know it wasn't really Columbus that discovered America...",
	"back_message": "It was the Vikings!",
	"card_color": null,
	"font": null,
	"text_align": null,
	"border_color": null,
	"border_choices": null,
	"owner": "swordfish23"
}
```
*** Please note that default values are null for certain parameters, may institute defaults in the future.

## Look at cards details

Requires authentication.

### request

```txt
GET ecard/<int:pk>
```

### response

```json
{
	"id": 1,
	"title": "Trolling",
	"front_message": "Sometime I troll all of you into thinking I'm the best",
	"back_message": "Just kidding I am the actual worst",
	"card_color": "Blue",
	"font": "regular",
	"text_align": "left",
	"border_color": "Blue",
	"border_choices": "dotted",
	"owner": "Bigchonga"
}
```

## To look at info in a user profile

Requires authentication.

### request

```txt
GET profile/<int:id>
```

### response

```json
{
  "id": 1,
  "name": null,
  "bio": "The greatest example ever",
  "username": "admin",
  "email": ""
}
```

## List all comments

### request

Username and password are required.

```
GET <BASE_URL>/comment/

```

### response

```json
200 OK

[
	{
		"id": 1,
		"card": 1,
		"comment": "What the actual FFFFFFF",
		"user": "DanceMonkey"
	},
	{
		"id": 2,
		"card": 3,
		"comment": "I'll be there!!",
		"user": "GodMode"
	},
	{
		"id": 3,
		"card": 2,
		"comment": "Just be here already!!!",
		"user": "GodMode"
	}

```

## Comment detail page

### request

Username and password are required.

```
GET <BASE_URL>/comment/2/

```

### response

```json
200 OK

{
	"id": 2,
	"card": 3,
	"comment": "I'll be there!!",
	"user": "GodMode"
}

```

## Get a List of Followers

### request

Authorization is required.

```
GET <BASE_URL>/follower/

```

### response

```json
200 OK

[
	{
		"id": 6,
		"user": 3,
		"being_followed": 4,
		"created": "2022-12-01T14:43:46.105659Z"
	}
]

```

## Follow a User

Authorization is required.

### request

```
POST <BASE_URL>/follower/

```

{
	"user": "This field is required.",
	"being_followed": "This field is required."
}

### response

```json
200 OK

{
	"id": 19,
	"user": 2,
	"being_followed": 3,
	"created": "2022-12-01T20:55:23.430178Z"
}

