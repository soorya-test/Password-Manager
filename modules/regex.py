import re

class Regex:

    # * Function to verify Master Username
    # * Parameters: Master USer Name
    # * Return Value: Boolean
    @classmethod
    def verifyMasterUserName(cls, master_user_name: str) -> bool:
        pattern = '^[A-Za-z0-9._]+$'
        return bool(re.match(pattern, master_user_name))
    
    # * Function to verify Master Password
    # * Parameters: Master Password
    # * Return Value: Boolean
    @classmethod
    def verifyPassword(cls, master_password: str) -> bool:
        spec_char = r'''!@$%^&*()_+-={}[]|\:;"'?/><,.~`#'''
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*["+spec_char+"])[A-Za-z\d"+spec_char+"]{8,35}$"
        return bool(re.match(pattern, master_password))
