# neo-scavenger-hunt
A Smart Contract for a Scavenger hunt

On Coznet:
``` 
  "description": "scavergerhunt",
    "version": 0,
    "properties": {
        "storage": true,
        "dynamic_invoke": false
    },
    "author": "localhuman",
    "code": {
        "returntype": 5,
        "parameters": "0710",
        "hash": "c8652f2b5030fc26fa8adf4f66dafb7848106e02",
        "script": "a lot of stuff here..."
    },
    "email": "tom@cityofzion.io",
    "name": "Scavenge2",
    "code_version": "2"
}
```

### Methods:
All invokes should be a combination of a string for `operation`, and an array of additional arguments.  Even if no additonal arguments, an empty array should be specified.

#### Public:
The following are available for anyone to call
- `get_clue` 
    - Gets a clue by index ( currenty 0 to 4)
    - requires an attachment of .01 gas
    - sample `neo-python` invoke: `testinvoke c8652f2b5030fc26fa8adf4f66dafb7848106e02 get_clue [0] --attach-gas=.01`
    - you must have answered the previous question to get the next clue
- `submit_answer` 
    - submit an answer by index ( currenty 0 to 4)
    - requires an attachment of .02 gas
    - sample `neo-python` invoke: `testinvoke c8652f2b5030fc26fa8adf4f66dafb7848106e02 get_clue [0,'myanswer'] --attach-gas=.02`
    - you must have answered the previous question to submit the next answer

- `total_questions`
    - get the total number of questions
    - sample `neo-python` invoke: `testinvoke c8652f2b5030fc26fa8adf4f66dafb7848106e02 total_questions []`

- `progress`
    - get the current progress for an address
    - requires an attachment of gas
    - sample `neo-python` invoke: `testinvoke c8652f2b5030fc26fa8adf4f66dafb7848106e02 progress [] --attach-gas=.001`
- `total_winners`
    - gets total number of people who have won 
    - sample `neo-python` invoke: `testinvoke c8652f2b5030fc26fa8adf4f66dafb7848106e02 total_winners []`

- `first_place`
    - gets first place winner
    - sample `neo-python` invoke: `testinvoke c8652f2b5030fc26fa8adf4f66dafb7848106e02 first_place []`

- `second_place`
    - gets first place winner
    - sample `neo-python` invoke: `testinvoke c8652f2b5030fc26fa8adf4f66dafb7848106e02 second_place []`

- `third_place`
    - gets first place winner
    - sample `neo-python` invoke: `testinvoke c8652f2b5030fc26fa8adf4f66dafb7848106e02 third_place []`


#### Owner:
The following must be invoked by the owner of the contract
- `set_clue`
    - Sets a clue by index ( currenty 0 to 4)
    - sample `neo-python` invoke: `testinvoke c8652f2b5030fc26fa8adf4f66dafb7848106e02 set_clue [0,'myclue']`
- `set_answer`
    - Sets an answer by index ( currenty 0 to 4)
    - Answer should be hashed to bytearray with Neo's Hash256 method
    - sample `neo-python` invoke: `testinvoke c8652f2b5030fc26fa8adf4f66dafb7848106e02 set_answer [0,bytearray(b'\xcbEY\xadn~T\x05~\x89(>\xc4\xe3"\xefyv\x87\x1d\xb0\xa4\x93\x03N\x1c\x16\xcf\x8a\x7f\xc0\xef')]`
