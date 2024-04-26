#!/usr/bin/python3

""" Prints the State object with the name passed as argument from the database hbtn_0e_0_usa database """
import sys
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session object 
    session = Session()

    # Search for the specified state in the database
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break

        # Print a message if the state is not found
        if found is False:
            print("Not found")