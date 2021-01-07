from ansible import errors

import hashlib
import secrets
class FilterModule(object):
    ''' A filter to salt sha1-encrypted passwords. '''
    def filters(self):
        return {
            'random_salt': self.random_salt,
            'salted_sha1': self.salted_sha1
        }

    def random_salt(self, salt_length):
        """
        returns a random hex token to use as a salt
        """
        salt = secrets.token_hex(salt_length)
        return salt.encode('utf-8')

    def salted_sha1(self, raw_password, salt):
            """
            Returns a string of the hexdigest of the given plaintext password and salt
            using the sha1 algorithm.
            """
            return hashlib.sha1(salt + raw_password).hexdigest()
