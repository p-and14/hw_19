from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):

        user = User(**user_data)

        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, uid):
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()

    def update(self, user_data):
        user = self.get_one(user_data.get("id"))
        user.name = user_data.get("name")

        self.session.add(user)
        self.session.commit()
