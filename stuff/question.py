from boa.code.builtins import concat, sha256, hash256
from boa.blockchain.vm.Neo.Runtime import CheckWitness
from common.storage_api import StorageAPI


class Questions():

    owner = 0

    def get_progress(self, storage: StorageAPI, address, required):

        key = concat('progress_', address)

        current = storage.getitem(key)
        if required > current:
            return False

        return True

    def get_clue(self, storage: StorageAPI, index, address):

        if address == 0:
            return b'Please attach at least .01 gas to get this clue'

        can_get_clue = self.get_progress(storage, address, index)

        if not can_get_clue:
            return b'You must answer all previous questions before getting this one'

        clue_str = concat('clue', index)
        return storage.getitem(clue_str)

    def submit_answer(self, storage: StorageAPI, index, answer, address):

        if address == 0:
            return b'Please attach at least .02 gas to submit an answer'

        can_submit_answer = self.get_progress(storage, address, index)

        if not can_submit_answer:
            return b'You must answer all previous questions before answering this one'

        hash_answer = hash256(answer)

        answer_key = concat('answer', index)
        real_answer = storage.getitem(answer_key)

#        Notify(hash_answer)

        if hash_answer == real_answer:

            next = index + 1

            if next == 5:

                total_winners = self.check_winners(storage, address)

                if total_winners == 1:

                    message = b'You have won 1st prize in the scavenger hunt! Please contact tom@cityofzion.io to claim your prize.'

                elif total_winners == 2:

                    message = b'You have won 2nd prize in the scavenger hunt! Please contact tom@cityofzion.io to claim your prize.'

                elif total_winners == 3:

                    message = b'You have won 3rd place in the scavenger hunt! Please contact tom@cityofzion.io to claim your prize'

                elif total_winners == 10000:

                    message = b'You are the runner of this contract.  You cant win.'

                elif total_winners == 0:

                    message = b'You already won.'

                else:

                    message = b'You have finished the scavenger hunt! Unfortunately others have beaten you.  Thanks for trying'

            else:
                ok = self.set_progress(storage, next, address)

                message = concat(b'Answer Correct! You may now move on to question ', next)

            return message

        return b'Incorrect Answer'

    def set_clue(self, storage: StorageAPI, index, value):

        if not CheckWitness(self.owner):
            print("must be owner to set clue")
            return False

        clue_str = concat('clue', index)

        storage.putitem(clue_str, value)

        return True

    def set_answer(self, storage: StorageAPI, index, value):

        if not CheckWitness(self.owner):
            print("must be owner to set answer")
            return False

        clue_str = concat('answer', index)

        storage.putitem(clue_str, value)
        return b'Set Answer'

    def set_progress(self, storage: StorageAPI, index, addr):

        if CheckWitness(self.owner):
            progress_key = concat('progress_', addr)
            current_val = storage.getitem(progress_key)

            # we don't want people to go backwards if they answer an old question
            if index > current_val:
                storage.putitem(progress_key, index)

            return True

        return False

    def check_winners(self, storage: StorageAPI, address):

        if address == self.owner:
            return 10000

        place_key = concat('place', address)

        current_place = storage.getitem(place_key)

        # if they aleady won, we don't want to let them do it again
        if current_place > 0:
            return 0

        total_winners = storage.getitem('total_winners')
        place = total_winners + 1
        storage.putitem('total_winners', place)

        storage.putitem(place_key, place)

        # persist winners
        if place == 1:

            storage.putitem('first_place', address)

        elif place == 2:

            storage.putitem('second_place', address)

        elif place == 3:

            storage.putitem('third_place', address)

        return place
