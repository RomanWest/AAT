from aat.models import Attempts
from flask import request

print(Attempts.query.all())

print(Attempts.query.filter_by(Attempts.user_id==1))