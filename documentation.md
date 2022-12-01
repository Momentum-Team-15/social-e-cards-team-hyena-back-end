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
	"username":
		"darkstar11"
	,
	"password":
		"redmoon10"
}
```

### response

```
201 Created

{
	"email": "",
	"username": "darkstar11",
	"id": 14
}

```

## Log In

### request

```
POST auth/token/login

{
  "username": "darkstar11",
  "password": "redmoon10"
}
```

### response

```json
{
  "auth_token": "56e7439e812e26a3bf4b891f275636396720cbcf"
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
  },
  {
    "id": 2,
    "title": "Christmas 2022",
    "front_message": "Have a Merry Christmas!!",
    "back_message": "From, The Stockdales",
    "card_color": "GREEN",
    "font": "ARIAL",
    "text_align": "CENTER",
    "border_color": "Red",
    "border_choices": "DOTTED",
    "owner": "TellyTubby"
  },
  {
    "id": 3,
    "title": "Halloween 2023",
    "front_message": "Happy Day of the Dead!",
    "back_message": "Halloween Night, 2023",
    "card_color": "ORANGE",
    "font": "HELVETICA",
    "text_align": "LEFT",
    "border_color": "WHITE",
    "border_choices": "SOLID",
    "owner": "DanceMonkey"
  },
  {
    "id": 4,
    "title": "Marlin Fishing Tourney 2023",
    "front_message": "5th Annual St. John Marlin Fishing Tournament",
    "back_message": "We dont want em if their .500lbs!!",
    "card_color": "BLUE",
    "font": "SCRIPT",
    "text_align": "RIGHT",
    "border_color": "AQUA",
    "border_choices": "JAGGED",
    "owner": "swordfish23"
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
  "title": "July 4th, 2023",
  "front_message": "Happy Independence Day",
  "back_message": "And the rockets' red glare..."
}
```

### response

```json
{
  "id": 8,
  "title": "July 4th, 2023",
  "front_message": "Happy Independence Day",
  "back_message": "And the rocket's red glare...",
  "card_color": null,
  "font": null,
  "text_align": null,
  "border_color": null,
  "border_choices": null,
  "owner": "swordfish23"
}
```

\*\*\* Please note that default values are null for certain parameters, may institute defaults in the future.

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

## List all comments

### request

Authorization is required.

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

Authorization is required.

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

```
