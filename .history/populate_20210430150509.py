from aat import db
from aat.models import Multiple
from datetime import datetime
db.session.delete(Multiple)
db.session.commit()
db.session.add(Multiple(question="What colour is a banana?", correct="yellow", module_code="Fruit123", 
    incorrect_1="blue", incorrect_2="red", incorrect_3="purple", difficulty="easy", is_formative=True, feedback="Refer to Fruit123 module!"))    
db.session.commit()
db.session.add(Multiple(question="How many eyes do humans have?", correct="Two", module_code="Biology123", 
    incorrect_1="One", incorrect_2="Three", incorrect_3="Four", difficulty="easy", is_formative=False, feedback="Refer to Biology123 module!"))    
db.session.commit()