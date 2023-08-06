

class WalletBase:
    """Base class for PyLibSIMBA Wallet implementations"""

    def __init__(self, signing_confirmation):
        if not signing_confirmation:
            self.signing_confirmation = self.default_accept
        self.signingConfirmation = signing_confirmation
        self.wallet = None

    def default_accept(self):
        return True

    def unlock_wallet(self, passkey):
        """
        If the wallet is locked, unlock it with the given passkey

        Args:
            passkey : used to unlock the wallet
        """
        raise NotImplementedError('Wallet.unlockWallet Not Implemented')

    def generate_wallet(self, mnemonic: str = None):
        """
        Create a new wallet. Set self.wallet to the new wallet.
        Current logic is same as generate_wallet_from_mnemonic.
        Both methods are required for compatibility's sake.

        Args:
            mnemonic : A string the wallet will use to create the wallet
        """
        raise NotImplementedError('Wallet.generate_wallet Not Implemented')

    def generate_wallet_from_mnemonic(self, mnemonic: str = None):
        """
        Create a new wallet using that wallet's mnemonic. Set self.wallet to the new wallet

        Args:
            mnemonic : A string - the wallet's mnemonic - that is used to create the wallet
        """
        raise NotImplementedError('Wallet.generate_wallet_from_mnemonic Not Implemented')

    def generate_wallet_from_private_key(self, private_key: str = None):
        """
        Create a new wallet using that wallet's private key. Set self.wallet to the new wallet.

        Args:
            private_key : A string - the wallet's private key - used to create the wallet
        """
        raise NotImplementedError("Wallet.generate_wallet_from_private_key Not Implemented")

    def delete_wallet(self):
        """
        Remove the current wallet
        """
        raise NotImplementedError('Wallet.deleteWallet Not Implemented')

    def wallet_exists(self) -> bool:
        """
        Does a wallet currently exist?
        """
        raise NotImplementedError('Wallet.deleteWallet Not Implemented')

    def sign(self, payload) -> dict:
        """
        Sign the payload with the wallet

        Args:
            payload : an object
        Returns:
            Returns the signed transaction
        """
        raise NotImplementedError('Wallet.sign Not Implemented')

    def get_address(self):
        """
        The address associated with this wallet
        """
        raise NotImplementedError('Wallet.sign Not Implemented')
