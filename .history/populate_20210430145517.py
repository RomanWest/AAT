from aat import db
from aat.models import Multiple
from datetime import datetime
db.session.add(Multiple(question="What colour is a banana?", correct="yellow", module_code="Fruit123", 
    incorrect_1="blue", incorrect_2="red", incorrect_3="purple", difficulty="easy", is_formative=True, feedback="Refer to Fruit123 module"))
db.session.commit()