# ruleid:raise-not-base-exception
raise "error here"

# ruleid:raise-not-base-exception
raise 5


class Foobar:
    x = 5


# ruleid:raise-not-base-exception
raise Foobar()


class Foobar2(BaseException):
    x = 5


# OK
raise Foobar2()

# OK
raise Exception()
