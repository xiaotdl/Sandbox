from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime

from Models import Candidate
from Models import Recruiter
from Models import Client
from Models import Position
from Models import Interview
from Models import init_database



class DataProviderService:
    def __init__(self, engine):
        """
        :param engine: The engine route and login details
        :return: a new instance of DAL class
        :type engine: string
        """
        if not engine:
            raise ValueError('The values specified in engine parameter has to be supported by SQLAlchemy')
        self.engine = engine
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()

    def init_database(self):
        """
        Initializes the database tables and relationships
        :return: None
        """
        init_database(self.engine)

    def add_candidate(self, first_name, last_name, email, birthday=None, phone=None, languages="", skills=""):
        """
        Creates and saves a new candidate to the database.

        :param first_name: First Name of the candidate
        :param last_name: Last Name of the candidate
        :param email: Email address of the candidate
        :param birthday: Birthday of the candidate
        :param phone: Telephone number of the candidate
        :param languages: Language skills of the candidate
        :param skills: Skills which the candidate has
        :return: The id of the new Candidate
        """

        new_candidate = Candidate(first_name=first_name,
                                  last_name=last_name,
                                  email=email,
                                  birthday=birthday,
                                  phone=phone,
                                  languages=languages,
                                  skills=skills)

        self.session.add(new_candidate)
        self.session.commit()

        return new_candidate.id

    def get_candidate(self, id=None, serialize=False):
        """
        If the id parameter is  defined then it looks up the candidate with the given id,
        otherwise it loads all the candidates

        :param id: The id of the candidate which needs to be loaded (default value is None)
        :return: The candidate or candidates.
        """

        all_candidates = []

        if id is None:
            all_candidates = self.session.query(Candidate).order_by(Candidate.last_name).all()
        else:
            all_candidates = self.session.query(Candidate).filter(Candidate.id == id).all()

        if serialize:
            return [cand.serialize() for cand in all_candidates]
        else:
            return all_candidates

    def update_candidate(self, id, new_candidate):
        updated_candidate = None
        candidate = self.get_candidate(id)[0]

        if candidate:
            candidate.email = new_candidate["email"]
            candidate.phone = new_candidate["phone"]
            candidate.first_name = new_candidate["first_name"]
            candidate.last_name = new_candidate["last_name"]
            self.session.add(candidate)
            self.session.commit()
            updated_candidate = self.get_candidate(id)[0]

        return updated_candidate


def fill_database(self):
        #
        # Candidates
        #
        cand1 = Candidate(first_name="John",
                          last_name="Doe",
                          email="john@example.com",
                          birthday=datetime.date(1979, 3, 4),
                          phone="1-233-332",
                          languages='{ "English": "mother tongue", '
                                    '  "French" : "beginner" }',
                          skills=".NET JavaScript Python Node.js MySQL")
        cand2 = Candidate(first_name="Jane",
                          last_name="Doe",
                          email="jane@example.com",
                          birthday=datetime.date(1984, 7, 9),
                          phone="1-737-372",
                          languages='{ "English": "mother tongue", '
                                    '  "French" : "beginner",'
                                    '  "German" : "intermediate" }',
                          skills="Ruby Java PHP CakePHP")
        cand3 = Candidate(first_name="Bob",
                          last_name="Coder",
                          email="bc@bobthecoder.com",
                          birthday=datetime.date(1988, 11, 3),
                          phone="1-113-333",
                          languages='{ "English": "mother tongue", '
                                    '  "Japanese" : "beginner",'
                                    '  "Swedish" : "intermediate" }',
                          skills="Electrical Engineering High Voltage Ruby Java JavaScript MongoDB Oracle PHP")

        self.session.add(cand1)
        self.session.add(cand2)
        self.session.add(cand3)
        self.session.commit()


        #
        # Recruiters
        #
        recr1 = Recruiter(first_name="Bill",
                          last_name="Oak",
                          phone="1-454-998")
        recr2 = Recruiter(first_name="Vanessa",
                          last_name="Albright",
                          phone="1-119-238")
        recr3 = Recruiter(first_name="Kate",
                          last_name="Mingley",
                          phone="2-542-977")
        self.session.add(recr1)
        self.session.add(recr2)
        self.session.add(recr3)
        self.session.commit()


        #
        # Clients
        #
        client1 = Client(name="Capital Inc.",
                         phone="326-554-975",
                         email="admin@capital.inc")
        client2 = Client(name="Red Black Tree Inc",
                         phone="121-554-775",
                         email="info@redblacktreeinc.com")
        client3 = Client(name="My House Builder Company",
                         phone="663-514-075",
                         email="hr@myhouseb.com")
        self.session.add(client1)
        self.session.add(client2)
        self.session.add(client3)
        self.session.commit()

        #
        # Positions
        #
        cl1_pos1 = Position(name="Python developer",
                            description="Our company needs a highly experienced senior Python developer with "
                                        "skills in large Python code handling.",
                            tech_skills="Python SQLAlchemy GIT SVN OOP",
                            years_of_experience=7,
                            salary=65000,
                            client=client1.id,
                            recruiter=recr1.id)

        cl1_pos2 = Position(name="Ruby developer",
                            description="Our company needs an experienced Ruby web developer with "
                                        "skills in CSS and JavaScript.",
                            tech_skills="Ruby CSS JavaScript",
                            years_of_experience=3,
                            salary=58000,
                            client=client1.id,
                            recruiter=recr1.id)
        # Client 2
        cl2_pos1 = Position(name="Electrical Engineer",
                            description="Our company needs an expert on Electrical Engineering.",
                            tech_skills="Physics Electricity Engineering Planning ",
                            years_of_experience=10,
                            salary=85000,
                            client=client2.id,
                            recruiter=recr2.id)
        cl2_pos2 = Position(name="Carpenter",
                            description="We are looking for a carpenter with experience in Alaska.",
                            tech_skills="Carpenter Wood-Structure Scaffold Shelving",
                            years_of_experience=6,
                            salary=61000,
                            client=client2.id,
                            recruiter=recr2.id)

        # Client 3
        cl3_pos1 = Position(name="Txi driver",
                            description="Our company needs Taxi Drivers in Boston.",
                            tech_skills="Taxi-license Car Driver-license",
                            years_of_experience=2,
                            salary=45000,
                            client=client3.id,
                            recruiter=recr3.id)
        cl3_pos2 = Position(name="Mason",
                            description="We are looking for a mason who has experience working with clay",
                            tech_skills="Masonary Clay Building Planning",
                            years_of_experience=3,
                            salary=43000,
                            client=client3.id,
                            recruiter=recr3.id)
        self.session.add(cl1_pos1)
        self.session.add(cl1_pos2)
        self.session.add(cl2_pos1)
        self.session.add(cl2_pos2)
        self.session.add(cl3_pos1)
        self.session.add(cl3_pos2)
        self.session.commit()



        #
        # Interviews
        #
        int1 = Interview(date=datetime.date(2015, 4, 3),
                         feedback="The candidate is perfect fit for the position.",
                         position=cl1_pos1.id,
                         recruiter_id=recr1.id,
                         candidate=cand1.id)
        int2 = Interview(date=datetime.date(2015, 6, 13),
                         feedback="The candidate is not good for the position.",
                         position=cl1_pos2.id,
                         recruiter_id=recr1.id,
                         candidate=cand2.id)
        int3 = Interview(date=datetime.date(2015, 7, 22),
                         feedback="The candidate is good for the position.",
                         position=cl2_pos1.id,
                         recruiter_id=recr2.id,
                         candidate=cand3.id)
        self.session.add(int1)
        self.session.add(int2)
        self.session.add(int3)

        self.session.commit()
