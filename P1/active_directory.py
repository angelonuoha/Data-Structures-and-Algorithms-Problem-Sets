class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group.users is None and group.groups is None:
        return False

    if user in group.users:
        return True
    
    for item in group.groups:
        return is_user_in_group(user, item)

def test_function(user, group):
    print("Test: (user: {}, group: {}) \n".format(user, group.name))
    if is_user_in_group(user, group):
        print("{} is in {}\n".format(user, group.name))
    else:
        print("{} is not in {}\n".format(user, group.name))

# Inputs
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

number = Group("number")
even = Group("even")
odd = Group("odd")
number.add_group(even)
number.add_group(odd)
seven = "seven"
six = "six"
even.add_user(six)
odd.add_user(seven)

# Test Cases
test_function(sub_child_user, parent) # Should return True
test_function(sub_child_user, number) # Should return False
test_function(seven, even) # Should return False
test_function(six, even) # Should return True