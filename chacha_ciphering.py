class ChaCha20:
    """
    Main class for encryption and decryption with ChaCha20 Encryption Algorithm.
    """

    def __init__(self, encryption_key, nonce, counter):
        self.encryption_key = encryption_key
        self.nonce = nonce
        self.counter = counter

    def encryption(self):
        """
        (...)

        :return:
        """

    def decryption(self):
        """
        (...)

        :return:
        """

    def _generate_nonce(self):
        """
        My proposal is to generate nonce in real time for example ---> sha256(string(key)+string(unix_timestamp))

        :return:
        """
# Here will be more methods connected with streaming via network
