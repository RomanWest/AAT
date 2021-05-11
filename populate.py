from aat import db
from aat.models import Assessment, Multiple, Fill, User
from datetime import datetime

Multiple.query.delete()
db.session.commit()
db.session.add(Multiple(question="What colour is a banana?", correct="yellow", module_code="Fruit123",
    incorrect_1="blue", incorrect_2="red", incorrect_3="purple", difficulty="easy", is_summative=True, feedback="Refer to Fruit123 module!"))
db.session.commit()
db.session.add(Multiple(question="How many eyes do humans have?", correct="Two", module_code="Biology123",
    incorrect_1="One", incorrect_2="Three", incorrect_3="Four", difficulty="easy", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="How many sides does a square have?", correct="Four", module_code="Maths123",
    incorrect_1="Three ", incorrect_2="Two", incorrect_3="One", difficulty="hard", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()

Fill.query.delete()
db.session.commit()
db.session.add(Fill(question="A tree is made from", module_code="Fruit123", correct="wood", difficulty="easy",
    is_summative=False, feedback="Refer to Fruit123 module!"))
db.session.commit()
db.session.add(Fill(question="1 + 299 = 300", module_code="Maths123", correct="300", difficulty="hard",
    is_summative=True, feedback="Refer to Maths123 notes, Chapter 2"))
db.session.commit()
db.session.add(Fill(question="The colour of grass is?", module_code="Fruit123", correct="green", difficulty="easy",
    is_summative=True, feedback="Refer to Fruit123 notes, Chapter 10"))
db.session.commit()
db.session.add(Fill(question="75 - -1", module_code="Maths123", correct="76", difficulty="hard",
    is_summative=True, feedback="Refer to Maths123 notes, Chapter 15"))
db.session.commit()

User.query.delete()
db.session.commit()
db.session.add(User(username="Admin", first_name="Ad", last_name="min", email="admin@admin.com", password="123456", is_admin=True,
    module_1="Fruit123", module_2="Biology123", module_3="Maths123"))
db.session.commit()

Assessment.query.delete()
db.session.commit()
db.session.add(Assessment(assessment_name="Test", module_code="Fruit123", admin_created=True, 
    q1_type="Multiple", q1_id=1, q2_type="Fill", q2_id="1", q3_type="Fill", q3_id="3"))
db.session.commit()
