class Token:
    """Representação de token"""
    def __init__(self, token_type, value, line):
        self.token_type = token_type
        self.value = value
        self.line = line
