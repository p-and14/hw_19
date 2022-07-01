import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_one(self, uid):
        return self.user_dao.get_one(uid)

    def get_all(self):
        return self.user_dao.get_all()

    def create(self, user_data):
        password = user_data["password"]
        generated_password = self.generate_password(password)
        user_data["password"] = generated_password

        return self.user_dao.create(user_data)

    def update(self, user_data):
        self.user_dao.update(user_data)
        return self.user_dao

    def delete(self, uid):
        self.user_dao.delete(uid)

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)

    def get_by_username(self, username):
        return self.user_dao.get_by_username(username)

    def compare_passwords(self, password_hash, other_password) -> bool:
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        hash_digest_b64 = base64.b64encode(hash_digest)

        return hmac.compare_digest(password_hash, hash_digest_b64)
