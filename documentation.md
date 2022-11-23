
### API ENDPOINTS
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | /api-auth/login | To login to an existing account |
| GET | /api/user/logout | Logout from account |
| GET | /auth/users | Register new user |
| GET | /ecard/ | Gets list of cards from users you follow |
| POST | /ecard/ | Create new ecard/post |
| GET | /ecard/<int:pk> | Get a specific ecard's details |
| PUT | /ecard/<int:pk> | Updates the card with specified id |
| DELETE | /ecard/<int:pk> | Deletes card with specific id |
| POST | /comments/ | Make a comment |
| GET | /comments/<int:pk> | Specific comment |
| PUT | /comments/<int:pk> | Updates the comment with specified id |
| DELETE | /comments/<int:pk> | Deletes comment with specific id |
| POST | /friends/ | add user as a friend |






# E-Card API

This application is an API built with Django REST Framework (DRF) that lets users track E-Cards that they want to create, share, or favorite -- kind of like any social media. Cards are listed with important information like title, user,font, and whether it is marked as “Published”.

**All requests, except registration and log in, require authentication**.

## Required Headers

Requests to endpoints requiring authentication should set the `Authorization` header to `Token <token>`, where `<token>` is the token received in the login response.

POST requests with a body should set the `Content-Type` header to `application/json`.


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



## List all Cards for particular user
Requires authentication.
### request
```txt
GET ecards/user/
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
	"title": "example",
	"border_style": "SOLID",
	"font_family": "UBUNTO",
	"text_alignment": "LEFT",
	"outer_msg": "blabla",
	"inner_msg": "yes sir"
}
```

### response

```json

{
	"id": 7,
	"title": "example",
	"user": 1,
	"border_style": "SOLID",
	"border_color": "BLACK",
	"font_family": "UBUNTO",
	"font_color": "BLACK",
	"text_alignment": "LEFT",
	"outer_msg": "blabla",
	"inner_msg": "yes sir",
	"created_at": "2022-11-17T18:13:32.950733Z",
	"updated_at": "2022-11-17T18:13:32.950747Z",
	"published": false
}

```

## Look at cards details

Requires authentication. 

### request

```txt
GET ecards/<int:pk>
```

### response
```json
{
	"id": 7,
	"title": "example",
	"user": 1,
	"border_style": "SOLID",
	"border_color": "BLACK",
	"font_family": "UBUNTO",
	"font_color": "BLACK",
	"text_alignment": "LEFT",
	"outer_msg": "blabla",
	"inner_msg": "yes sir",
	"created_at": "2022-11-17T18:13:32.950733Z",
	"updated_at": "2022-11-17T18:13:32.950747Z",
	"published": false
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

## To update a user profile

Requires authentication. NOTE THAT username is required in order to update other attributes

### request

```txt
PUT profile/<int:id>
```
```json
{
	"id": 1,
	"name": null,
	"bio": "The greatest test",
	"username": "admin",
	"email": ""
}
```

### response

```json
[
	{
		"id": 1,
		"name": null,
		"bio": "The greatest test",
		"username": "admin",
		"email": ""
	}
]
```

## List all comments

### request

Username and password are required.

```
GET <BASE_URL>/comments

```

### response

```json
200 OK

[
	{
		"id": 3,
		"card": 3,
		"comment": "This is a comment by user on Ray's bday card!",
		"commentor": 2
	},
	{
		"id": 2,
		"card": 3,
		"comment": "This is a comment on Ray's Birthday card by admin!",
		"commentor": 1
	},
	{
		"id": 1,
		"card": 1,
		"comment": "This is a comment by admin on Autumn 2022 card!",
		"commentor": 1
	}
]

```

## Comment detail page

### request

Username and password are required.

```
GET <BASE_URL>/comments/1

```

### response

```json
200 OK

{
	"id": 1,
	"card": 1,
	"comment": "This is a comment by admin on Autumn 2022 card!",
	"commentor": 1
}

```

## List all Friends

### request

Username and password are required.

```
GET <BASE_URL>/friends

```

### response

```json
200 OK

[
	{
		"id": 6,
		"user": 2
	},
	{
		"id": 9,
		"user": 3
	}
]

```

## Friends detail page

### request

Username and password are required.

```
GET <BASE_URL>/friends/6

```

### response

```json
200 OK

{
	"id": 6,
	"user": 2
}


## List all favorites

### request

Username and password are required.

```
GET <BASE_URL>/favorites

```

### response

```json
200 OK

[
	{
		"id": 1,
		"card": 1,
		"user": 1,
		"created_at": "2022-11-17T18:50:20.189108Z"
	},
	{
		"id": 2,
		"card": 2,
		"user": 1,
		"created_at": "2022-11-17T19:16:30.587099Z"
	}
]

```

## Favorite detail page

### request

Username and password are required.

```
GET <BASE_URL>/favorites/2

```

### response

```json
200 OK

{
	"id": 2,
	"card": 2,
	"user": 1,
	"created_at": "2022-11-17T19:16:30.587099Z"
}

```

| POST | /ecard | Create new ecard/post |
| GET | /ecard/<int:pk> | Specific card/post |
| POST | /comments | Make a comment |
| GET | /comments/<int:pk> | Specific comment |
| GET | /auth/users | Register new user |


