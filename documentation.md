###User Login - Create a new user

'''https://
POST - https://hyena-ecards.onrender.com/auth/users/
'''

| BODY      | TYPE      |DESCRIPTION    |
| :-------- | :-------- | :------------ |
| 'username'| 'string'  | New username  |
| 'password'| 'string'  | New password  |

Request Sample:

'''
POST - /auth/users/
Content-Type: json
Authorization:
Host: hyena-ecards