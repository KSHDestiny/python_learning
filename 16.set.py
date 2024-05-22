college = set(['Bill', 'Katy', 'Verne', 'Dillon', 'Bruce', 'Olivia', 'Richard', 'Jim'])
coworker = set(['Aaron', 'Bill', 'Brandon', 'David', 'Frank', 'Connie', 'Kyle', 'Olivia'])
family = set(['Garry', 'Landon', 'Larry', 'Mark', 'Olivia', 'Katy', 'Rae', 'Tom'])

print(len(college))
print(len(coworker))
print(len(family))

friends = college.union(coworker, family)
print(friends)  # {'Bruce', 'Garry', 'Kyle', 'Verne', 'Brandon', 'Katy', 'Olivia', 'Frank', 'Larry', 'Jim', 'Connie', 'Tom', 'Richard', 'David', 'Mark', 'Landon', 'Dillon', 'Aaron', 'Rae', 'Bill'}
print(len(friends))

# - Store groups of like objects
# - Each item unique
# - No order

#! .intersection()  // returns common elements
#! .difference()  // returns uncommon elements based on one side
#! .symmetric_difference()  // returns uncommon elements based on all sides

zipcode= set(['Jerry', 'Elaine', 'Cindy', 'Verne', 'Rudolph', 'Bill', 'Olivia', 'Jim', 'Lindsay', 'Rae', 'Mark', 'Kramer', 'Landon', 'Newman', 'George'])
munchkins = set(['Steve', 'Jackson', 'Frank', 'Bill', 'Mark', 'Landon', 'Rae'])
olivia = set(['Jim', 'Amanda', 'Verne', 'Nestor'])

local = friends.intersection(zipcode)
print(local)    # {'Jim', 'Mark', 'Landon', 'Verne', 'Rae', 'Bill', 'Olivia'}

invite = local.difference(munchkins)
print(invite)   # {'Olivia', 'Jim', 'Verne'}
not_invite = munchkins.difference(local)
print(not_invite)   # {'Frank', 'Jackson', 'Steve'}

invite = invite.symmetric_difference(olivia)
print(invite)   # {'Nestor', 'Amanda', 'Olivia'}

print('Verne' in invite)    # check whether Verne already exists in invite set  # but re-adding same item didn't change the set & it will not be added
invite.add('Verne')
print(invite)   # {'Olivia', 'Verne', 'Amanda', 'Nestor'}

invite.remove('Nestor')
print(invite)   # {'Verne', 'Olivia', 'Amanda'}

invite.pop()
print(invite)   # {'Amanda', 'Verne'}   // remove randomly one item