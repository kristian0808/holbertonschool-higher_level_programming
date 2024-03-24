#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and establish connection
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True,
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects that contain the letter 'a'
    states = (
        session.query(State).filter(
            State.name.like("%a%")).order_by(State.id).all()
    )

    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
