from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Mapping Configuration
# Ref: http://docs.sqlalchemy.org/en/latest/orm/mapping_styles.html

## Types of Mappings

### Declarative Mapping
# Making use of the Declarative system,
# 1) the components of the user-defined class,
# 2) the Table metadata to which the class is mapped
# are defined at once.

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    addresses = relationship("Address", backref="user", order_by="Address.id")

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'))
    email_address = Column(String)


### Classical Mappings
# from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import mapper
#
# metadata = MetaData()
#
# user = Table('user', metadata,
#             Column('id', Integer, primary_key=True),
#             Column('name', String(50)),
#             Column('fullname', String(50)),
#             Column('password', String(12))
#         )
#
# class User(object):
#     def __init__(self, name, fullname, password):
#         self.name = name
#         self.fullname = fullname
#         self.password = password
#
# mapper(User, user)
#
# ---
#
# address = Table('address', metadata,
#             Column('id', Integer, primary_key=True),
#             Column('user_id', Integer, ForeignKey('user.id')),
#             Column('email_address', String(50))
#             )
#
# mapper(User, user, properties={
#     'addresses' : relationship(Address, backref='user', order_by=address.c.id)
# })
#
# mapper(Address, address)


### Runtime Introspection of Mappings, Objects
from sqlalchemy import inspect
insp = inspect(User)
print type(insp)
print insp
print insp.columns
print list(insp.columns)
print insp.columns.name
print insp.all_orm_descriptors.keys()
print list(insp.column_attrs)
print insp.column_attrs.name.expression


## Mapping Columns and Expressions

### Naming Columns Distinctly from Attribute Names
# 1)
# class User(Base):
#     __tablename__ = 'user'
#     id = Column('user_id', Integer, primary_key=True)
#     name = Column('user_name', String(50))

# 2)
# When mapping to an existing table, the Column object can be referenced directly:
# class User(Base):
#     __table__ = user_table
#     id = user_table.c.user_id
#     name = user_table.c.user_name
# Or in a classical mapping, placed in the properties dictionary with the desired key:

# 3)
# mapper(User, user_table, properties={
#    'id': user_table.c.user_id,
#    'name': user_table.c.user_name,
# })


### Automating Column Naming Schemes from Reflected Tables

# @event.listens_for(Table, "column_reflect")
# def column_reflect(inspector, table, column_info):
#     # set column.key = "attr_<lower_case_name>"
#     column_info['key'] = "attr_%s" % column_info['name'].lower()


### Naming All Columns with a Prefix

# class User(Base):
#     __table__ = user_table
#     __mapper_args__ = {'column_prefix':'_'}

# The above will place attribute names such as _user_id, _user_name, _password etc.
# on the mapped User class.


### Using column_property for column level options

# sqlalchemy.orm.column_property(*columns, **kwargs)

# from sqlalchemy.orm import column_property
#
# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(Integer, primary_key=True)
#     name = column_property(Column(String(50)), active_history=True)

# column_property() is also used to map a single attribute to multiple columns. This use case arises when mapping to a join() which has attributes which are equated to each other:

# Another place where column_property() is needed is to specify SQL expressions as mapped attributes, such as below where we create an attribute fullname that is the string concatenation of the firstname and lastname columns:

# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     firstname = Column(String(50))
#     lastname = Column(String(50))
#     fullname = column_property(firstname + " " + lastname)


### Mapping a Subset of Table Columns

# include e.g.:
# class User(Base):
#     __table__ = user_table
#     __mapper_args__ = {
#         'include_properties' :['user_id', 'user_name']
#     }

# exclude e.g.:
# class Address(Base):
#     __table__ = address_table
#     __mapper_args__ = {
#         'exclude_properties' : ['street', 'city', 'state', 'zip']
#     }

# join table
# class UserAddress(Base):
#     __table__ = user_table.join(addresses_table)
#     __mapper_args__ = {
#         'exclude_properties' :[address_table.c.id],
#         'primary_key' : [user_table.c.id]
#     }




### Mapping Class Inheritance Hierarchies

# SQLAlchemy supports three forms of inheritance:
# 1) single table inheritance, where several types of classes are represented by a single table,
# 2) concrete table inheritance, where each type of class is represented by independent tables,
# 3) joined table inheritance, where the class hierarchy is broken up among dependent tables, each class represented by its own table that only includes those attributes local to that class.

# The most common forms of inheritance are 1) single and 3) joined table.


#### Joined Table Inheritance

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'employee',
        'polymorphic_on':type
    }

# Above, an additional column type is established to act as the discriminator, configured as such using the mapper.polymorphic_on parameter. This column will store a value which indicates the type of object represented within the row. The column may be of any datatype, though string and integer are the most common.


class Engineer(Employee):
    __tablename__ = 'engineer'
    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    engineer_name = Column(String(30))

    __mapper_args__ = {
        'polymorphic_identity':'engineer',
    }

class Manager(Employee):
    __tablename__ = 'manager'
    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    manager_name = Column(String(30))

    __mapper_args__ = {
        'polymorphic_identity':'manager',
    }

# It is most common that the foreign key constraint is established on the same column or columns as the primary key itself, however this is not required.


##### Relationships with Joined Inheritance

# class Company(Base):
#     __tablename__ = 'company'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     employees = relationship("Employee", back_populates="company")
#
# class Employee(Base):
#     __tablename__ = 'employee'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     type = Column(String(50))
#
#     company_id = Column(ForeignKey('company.id'))
#     company = relationship("Company", back_populates="employees")
#
#     __mapper_args__ = {
#         'polymorphic_identity':'employee',
#         'polymorphic_on':type
#     }
#
# class Manager(Employee):
#     # ...
#
# class Engineer(Employee):
#     # ...


##### Loading Joined Inheritance Mappings

# See the sections Loading Inheritance Hierarchies and Loading objects with joined table inheritance for background on inheritnce loading techniques, including configuration of tables to be queried both at mapper configuration time as well as query time.


#### Single Table Inheritance

# class Employee(Base):
#     __tablename__ = 'employee'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     type = Column(String(20))
#
#     __mapper_args__ = {
#         'polymorphic_on':type,
#         'polymorphic_identity':'employee'
#     }
#
# class Manager(Employee):
#     manager_data = Column(String(50))
#
#     __mapper_args__ = {
#         'polymorphic_identity':'manager'
#     }
#
# class Engineer(Employee):
#     engineer_info = Column(String(50))
#
#     __mapper_args__ = {
#         'polymorphic_identity':'engineer'
#     }

# Note that the mappers for the derived classes Manager and Engineer omit the __tablename__, indicating they do not have a mapped table of their own.

##### Relationships with Single Table Inheritance
# ...


#### Concrete Table Inheritance
# ...









































































