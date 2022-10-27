"""Examples of a class and objects."""

import profile


class Profile:
    handle: str
    followers: int
    is_private: bool

    def ___init___(self, handle: str):
        """Constructornitializes attributes."""
        self.handle = handle
        self.followers = 0
        self.is_private = False

    def tweet(self, msg: str):
        """An example of a method."""
        print(f"@{self.handle} tweets {msg}")


my_profile: Profile = Profile("krisjordan")
my_profile.tweet("Hello, world.")


