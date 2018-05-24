from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# Object Relational Tutorial
# Ref: http://docs.sqlalchemy.org/en/latest/orm/tutorial.html

## Connecting
# in-memory-only SQLite database
engine = create_engine('sqlite:///:memory:', echo=True)


## Declare a Mapping
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    addresses = relationship("Address", back_populates='user',
                    cascade="all, delete, delete-orphan")

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
               self.name, self.fullname, self.password)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")


    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


## Create a Schema
print repr(User.__table__)
Base.metadata.create_all(engine)


## Create an Instance of the Mapped Class
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
print ed_user.name
print ed_user.password
print str(ed_user.id) # None


## Creating a Session
# whenever you need to have a conversation with the database, you instantiate a Session
# Session is associated with our SQLite-enabled Engine, but it hasn't opened any connections yet. When it's first used, it retrieves a connection from a pool of connections maintained by the Engine, and holds onto it until we commit all changes and/or close the session object.
Session = sessionmaker(bind=engine)
session = Session()


## Adding and Updating Objects
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first()
print ed_user is our_user

session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah')])
ed_user.password = 'f8s7ccs'

print session.new
print session.dirty
session.commit()

print str(ed_user.id) # 1

# Session Object States
# As our User object moved from being outside the Session(transient),
# to inside the Session without a primary key(pending),
# to actually being inserted(persistent),
# it moved between three out of four available "object states" - transient, pending, and persistent.
# Being aware of these states and what they mean is always a good idea - be sure to read Quickie Intro to Object States for a quick overview.


## Rolling Back
ed_user.name = 'Edwardo'

fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
session.add(fake_user)

print session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()

session.rollback()
print ed_user.name
print fake_user in session
print session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()


## Querying
for instance in session.query(User).order_by(User.id):
	print(instance.name, instance.fullname)

for name, fullname in session.query(User.name, User.fullname):
	print(name, fullname)

for row in session.query(User, User.name).all():
	print(row.User, row.name)

for row in session.query(User.name.label('name_label')).all():
	print(row.name_label)

# Basic operations with Query include issuing LIMIT and OFFSET, most conveniently using Python array slices and typically in conjunction with ORDER BY:
for u in session.query(User).order_by(User.id)[1:3]:
	print(u)

# filtering results
for name, in session.query(User.name).\
			filter_by(fullname='Ed Jones'):
	print(name)


for user in session.query(User).\
         filter(User.name=='ed').\
         filter(User.fullname=='Ed Jones'):
	print(user)


## Common Filter Operators

### equals:
# query.filter(User.name == 'ed')

### not equals:
# query.filter(User.name != 'ed')

### LIKE:
# query.filter(User.name.like('%ed%'))

### ILIKE (case-insensitive LIKE):
# query.filter(User.name.ilike('%ed%'))

### IN:
# query.filter(User.name.in_(['ed', 'wendy', 'jack']))
# # works with query objects too:
# query.filter(User.name.in_(
#     session.query(User.name).filter(User.name.like('%ed%'))
# ))

### NOT IN:
# query.filter(~User.name.in_(['ed', 'wendy', 'jack']))

### IS NULL:
# query.filter(User.name == None)
#
# # alternatively, if pep8/linters are a concern
# query.filter(User.name.is_(None))

### IS NOT NULL:
# query.filter(User.name != None)
#
# # alternatively, if pep8/linters are a concern
# query.filter(User.name.isnot(None))

### AND:
# # use and_()
# from sqlalchemy import and_
# query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
#
# # or send multiple expressions to .filter()
# query.filter(User.name == 'ed', User.fullname == 'Ed Jones')
#
# # or chain multiple filter()/filter_by() calls
# query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')

### OR:
# from sqlalchemy import or_
# query.filter(or_(User.name == 'ed', User.name == 'wendy'))

### MATCH:
# query.filter(User.name.match('wendy'))


## Returning Lists and Scalars

### all() returns a list:

# >>> query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
# >>> query.all()
# [<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>,
#       <User(name='fred', fullname='Fred Flinstone', password='blah')>]

### first() applies a limit of one and returns the first result as a scalar:

# >>> query.first()
# <User(name='ed', fullname='Ed Jones', password='f8s7ccs')>

### one() fully fetches all rows, and if not exactly one object identity or composite row is present in the result, raises an error.

# With multiple rows found:
# >>> user = query.one()
# Traceback (most recent call last):
# ...
# MultipleResultsFound: Multiple rows were found for one()

# With no rows found:
# >>> user = query.filter(User.id == 99).one()
# Traceback (most recent call last):
# ...
# NoResultFound: No row was found for one()

### one_or_none() is like one(), except that if no results are found, it doesn't raise an error; it just returns None. Like one(), however, it does raise an error if multiple results are found.

### scalar() invokes the one() method, and upon success returns the first column of the row:


## Using Textual SQL

# bind parameters
# session.query(User).filter(text("id<:value and name=:name")).\
# 					  params(value=224, name='fred').order_by(User.id).one()
# <User(name='fred', fullname='Fred Flinstone', password='blah')>

# entire string-based statement
# session.query(User).from_statement(
#                     text("SELECT * FROM users where name=:name")).\
#                     params(name='ed').all()
# [<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]

# statement
# stmt = text("SELECT name, id, fullname, password "
# 			  "FROM users where name=:name")
# >>> stmt = stmt.columns(User.name, User.id, User.fullname, User.password)
# SQL>>> session.query(User).from_statement(stmt).params(name='ed').all()
# [<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]


## Counting
# Query includes a convenience method for counting called count():
#
# >>> session.query(User).filter(User.name.like('%ed')).count()
# 2


## Building a Relationship

# class Address(Base):
#     __tablename__ = 'addresses'
#     id = Column(Integer, primary_key=True)
#     email_address = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'))
# 
#     user = relationship("User", back_populates="addresses")
# 
# 
#     def __repr__(self):
#         return "<Address(email_address='%s')>" % self.email_address

# User.addresses = relationship(
# 	"Address", order_by=Address.id, back_populates="user")

print repr(User.__table__)
Base.metadata.create_all(engine)


## Working with Related Objects
jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
print jack
print jack.addresses
jack.addresses = [
                Address(email_address='jack@google.com'),
                Address(email_address='j25@yahoo.com')]
print jack.addresses

# >>> jack.addresses[1]
# <Address(email_address='j25@yahoo.com')>
#
# >>> jack.addresses[1].user
# <User(name='jack', fullname='Jack Bean', password='gjffdd')>

session.add(jack)
session.commit()

jack = session.query(User).\
	filter_by(name='jack').one()
print jack
# <User(name='jack', fullname='Jack Bean', password='gjffdd')>
print jack.addresses
# [<Address(email_address='jack@google.com')>, <Address(email_address='j25@yahoo.com')>]


## Querying with Joins
for u, a in session.query(User, Address).\
                    filter(User.id==Address.user_id).\
                    filter(Address.email_address=='jack@google.com').\
                    all():
    print(u)
    print(a)
# <User(name='jack', fullname='Jack Bean', password='gjffdd')>
# <Address(email_address='jack@google.com')>


## Eager Loading
# ...


## Deleting
print session.query(User).filter_by(name='jack').count()
session.delete(jack)
print session.query(User).filter_by(name='jack').count()


print session.query(Address).filter(
    Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])
 ).count()

session.close()
