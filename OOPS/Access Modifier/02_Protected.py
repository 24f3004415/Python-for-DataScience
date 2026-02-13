# 2. Protected members
#   • Indicated by a single underscore _ (suggest - “Don’t access directly unless
#       needed.”)
#   • Still accessible from outside (not truly protected).
#   • Intended for internal use or inheritance.


class Person:
    def init (self):
        self._age = 20 # protected variable

p = Person()

print(p._age) # Technically allowed, but not recommended