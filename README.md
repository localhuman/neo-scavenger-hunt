# neo-scavenger-hunt
A Smart Contract for a Scavenger hunt

On Testnet:
``` 
 {
    "code": {
        "script": "... omitted ...",
        "parameters": "0710",
        "hash": "922a1a8394bd26ce8340b7985ffc55535215697e",
        "returntype": 5
    },
    "properties": {
        "storage": true,
        "dynamic_invoke": false
    },
    "name": "ScavengerHunt",
    "code_version": ".2",
    "author": "localhuman",
    "version": 0,
    "email": "tom@cityofzion.io",
    "description": "A Scavenger Hunt"
}


```


### Invoke notes
When sending a string to a smart contract in `neo-python`, spaces must be replaced by `\\` for now.  

### Methods:
All invokes should be a combination of a string for `operation`, and an array of additional arguments.  Even if no additonal arguments, an empty array should be specified.

#### Public:
The following are available for anyone to call
- `get_clue` 
    - Gets a clue by index ( currenty 0 to 4)
    - requires an attachment of .01 gas
    - sample `neo-python` invoke: `testinvoke 922a1a8394bd26ce8340b7985ffc55535215697e get_clue [0] --attach-gas=.01`
    - you must have answered the previous question to get the next clue
- `submit_answer` 
    - submit an answer by index ( currenty 0 to 4)
    - requires an attachment of .02 gas
    - sample `neo-python` invoke: `testinvoke 922a1a8394bd26ce8340b7985ffc55535215697e get_clue [0,'myanswer'] --attach-gas=.02`
    - you must have answered the previous question to submit the next answer

- `total_questions`
    - get the total number of questions
    - sample `neo-python` invoke: `testinvoke 922a1a8394bd26ce8340b7985ffc55535215697e total_questions []`

- `progress`
    - get the current progress for an address
    - requires an attachment of gas
    - sample `neo-python` invoke: `testinvoke 922a1a8394bd26ce8340b7985ffc55535215697e progress [] --attach-gas=.001`
- `total_winners`
    - gets total number of people who have won 
    - sample `neo-python` invoke: `testinvoke 922a1a8394bd26ce8340b7985ffc55535215697e total_winners []`

- `first_place`
    - gets first place winner
    - sample `neo-python` invoke: `testinvoke 922a1a8394bd26ce8340b7985ffc55535215697e first_place []`

- `second_place`
    - gets first place winner
    - sample `neo-python` invoke: `testinvoke 922a1a8394bd26ce8340b7985ffc55535215697e second_place []`

- `third_place`
    - gets first place winner
    - sample `neo-python` invoke: `testinvoke 922a1a8394bd26ce8340b7985ffc55535215697e third_place []`


#### Owner:
The following must be invoked by the owner of the contract
- `set_clue`
    - Sets a clue by index ( currenty 0 to 4)
    - sample `neo-python` invoke: `testinvoke 922a1a8394bd26ce8340b7985ffc55535215697e set_clue [0,'myclue']`
- `set_answer`
    - Sets an answer by index ( currenty 0 to 4)
    - Answer should be hashed to bytearray with Neo's Hash256 method
    - sample `neo-python` invoke: `testinvoke 922a1a8394bd26ce8340b7985ffc55535215697e set_answer [0,bytearray(b'\xcbEY\xadn~T\x05~\x89(>\xc4\xe3"\xefyv\x87\x1d\xb0\xa4\x93\x03N\x1c\x16\xcf\x8a\x7f\xc0\xef')]`
