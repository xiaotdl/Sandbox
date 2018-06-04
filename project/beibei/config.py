# -*- coding: utf-8 -*-
import os
import sys


class Config(object):
    # == app server ==
    # HOST='0.0.0.0'
    HOST='10.192.10.147'
    PORT=5000

    # Flask and some of its extensions use this secret key as a cryptographic key to generate signatures or tokens.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


    # == db ==
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:default@localhost:3306/product_mgmt'
    # Disable signaling to application every time a change is about to be made in the database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
