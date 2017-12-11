from boa.blockchain.vm.Neo.Runtime import CheckWitness,Notify,GetTrigger
from boa.blockchain.vm.Neo.TriggerType import Application,Verification
from boa.code.builtins import concat

from common.storage_api import StorageAPI
from common.txio import Attachments,get_asset_attachments

from stuff.question import Questions

owner = b'\xe0\xa9\xce\x8c\xb0j\x8c\xb7-J,\x91+n0\\\xbb\x04\xe5\xb7'

clue_gas_req = 1000000
answer_gas_req = 2000000
progress_gas_req = 100

total_q = 5

def Main(operation, args):

    trigger = GetTrigger()

    if trigger == Verification():

        if CheckWitness(owner):
            return True

        return False


    storage = StorageAPI()

    questions = Questions()
    questions.owner = owner


    if operation == 'get_clue':
        addr = get_addr(clue_gas_req)
        cluenum = args[0]
        return questions.get_clue(storage,cluenum, addr)

    elif operation == 'set_clue':
        cluenum = args[0]
        clueval = args[1]
        return questions.set_clue(storage,cluenum, clueval)

    elif operation == 'set_answer':
        cluenum = args[0]
        answer = args[1]
        return questions.set_answer(storage, cluenum, answer)

    elif operation == 'submit_answer':
        addr = get_addr(answer_gas_req)
        if len(args) < 2:
            return b'Not enough arguments'
        cluenum = args[0]
        answer = args[1]
        return questions.submit_answer(storage,cluenum,answer,addr)

    elif operation == 'total_questions':
        return total_q

    elif operation == 'progress':
        addr = get_addr(progress_gas_req)
        key = concat('progress_',addr)
        return storage.getitem(key)

    elif operation == 'total_winners':
        return storage.getitem('total_winners')

    elif operation == 'first_place':
        return storage.getitem('first_place')

    elif operation == 'second_place':
        return storage.getitem('second_place')

    elif operation == 'third_place':
        return storage.getitem('third_place')

    return b'Method not found'


def get_addr(gas_required):

    attachments = get_asset_attachments() # type: Attachments

    if attachments.gas_attached < gas_required:
        print("Not enough gas")
        return 0

    return  attachments.sender_addr
