from .cryptography import Cryptography
from .database import Database
from .gui import GUI
from .regex import Regex
from .hashing import Hashing
from .exceptions import UserNotFoundError

actions = {
    "login": {
        "positive": 'Login Successfull', 
        "negative": 'Login Unsuccessfull'
    },
    "register": {
        "positive": 'Registration Successfull',
        "negative":'Registration Unsuccessfull'
    },
    "account": {
        "positive": 'Account Information has been Added',
        "negative": 'Account Information cannot be Added'
    },
    "credentials": {
      "negative": 'Invalid Username or Password'
    },
    "not_found": {
      "negative": 'User not Found'
    }
}

Database.init()