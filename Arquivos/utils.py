import os 


def get_path(file_name):
    """
    GET STRING NAME FOR FILE, AND RETURN HIS FILE PATH.
    """

    return os.path.join("Arquivos", "SenhasSalvas", file_name)