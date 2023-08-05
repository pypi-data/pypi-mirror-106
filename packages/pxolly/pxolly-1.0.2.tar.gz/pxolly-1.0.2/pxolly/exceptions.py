class PxollyAPIException(Exception):

    def __init__(
            self,
            error_code: int,
            error_msg: str = "",
            error_text: str = "",
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.error_text = error_text

    def __repr__(self):
        return f"<PxollyAPIException:code={self.error_code}, msg={self.error_msg}>"

    def __str__(self):
        return f"[{self.error_code}] {self.error_text}"
