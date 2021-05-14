from aat import db
from aat.models import Assessment, Multiple, Fill, User
from datetime import datetime


Multiple.query.delete()
db.session.commit()
db.session.add(Multiple(question="What colour is a banana?", correct="yellow", module_code="Fruit123",incorrect_1="blue", incorrect_2="red", incorrect_3="purple", difficulty="easy", is_summative=True, feedback="Refer to Fruit123 module!"))
db.session.add(Multiple(question="What colour is an orange?", correct="orange", module_code="Fruit123", incorrect_1="blue", incorrect_2="red", incorrect_3="purple", difficulty="easy", is_summative=False, feedback="Refer to Fruit123 module!"))
db.session.add(Multiple(question="What colour is a lemon?", correct="yellow", module_code="Fruit123", incorrect_1="blue", incorrect_2="red", incorrect_3="purple", difficulty="easy", is_summative=False, feedback="Refer to Fruit123 module!"))
db.session.add(Multiple(question="What colour is an apple?", correct="red", module_code="Fruit123", incorrect_1="blue", incorrect_2="black", incorrect_3="purple", difficulty="easy", is_summative=False, feedback="Refer to Fruit123 module!"))

db.session.commit()
db.session.add(Multiple(question="How many eyes do humans have?", correct="Two", module_code="Biology123",incorrect_1="One", incorrect_2="Three", incorrect_3="Four", difficulty="easy", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.add(Multiple(question="How many ears do humans have?", correct="two", module_code="Biology123", incorrect_1="one", incorrect_2="three", incorrect_3="four", difficulty="easy", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.add(Multiple(question="How many hands do humans have?", correct="two", module_code="Biology123", incorrect_1="one", incorrect_2="three", incorrect_3="four", difficulty="easy", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="How many sides does a square have?", correct="Four", module_code="Maths123",incorrect_1="Three ", incorrect_2="Two", incorrect_3="One",difficulty="hard", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.add(Multiple(question="How many sides does a pentagon have?", correct="five", module_code="Maths123",incorrect_1="Three ", incorrect_2="Two", incorrect_3="One", difficulty="easy", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.add(Multiple(question="How many sides does a triangle have?", correct="three", module_code="Maths123", incorrect_1="one", incorrect_2="two", incorrect_3="four", difficulty="easy", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.add(Multiple(question="How many sides does a rectangle have?", correct="four", module_code="Maths123", incorrect_1="one", incorrect_2="three", incorrect_3="two",  difficulty="easy", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()

Fill.query.delete()
db.session.commit()
db.session.add(Fill(question="A tree is made from", module_code="Fruit123", correct="wood", difficulty="easy",is_summative=False, feedback="Refer to Fruit123 module!"))
db.session.add(Fill(question="The colour of an orage is ", module_code="Fruit123", correct="orange", difficulty="easy",is_summative=False, feedback="Refer to Fruit123 module!"))
db.session.add(Fill(question="The colour of a banana is ", module_code="Fruit123", correct="yellow", difficulty="easy",is_summative=False, feedback="Refer to Fruit123 module!"))
db.session.add(Fill(question="1 + 9 = ", module_code="Maths123", correct="10", difficulty="easy",is_summative=False, feedback="Refer to Maths123 notes, Chapter 2"))
db.session.add(Fill(question="1 + 10 = ", module_code="Maths123", correct="11", difficulty="easy",is_summative=False, feedback="Refer to Maths123 notes, Chapter 2"))
db.session.add(Fill(question="1 + 11 = ", module_code="Maths123", correct="12", difficulty="easy",is_summative=False, feedback="Refer to Maths123 notes, Chapter 2"))
db.session.add(Fill(question="The colour of blood is ", module_code="Biology123", correct="red", difficulty="easy",is_summative=False, feedback="Refer to Biology123 module!"))
db.session.add(Fill(question="a group of lions is called a ", module_code="Biology123", correct="pride", difficulty="easy",is_summative=False, feedback="Refer to Biology123 module!"))
db.session.add(Fill(question="ice is made from ", module_code="Biology123", correct="water", difficulty="easy",is_summative=False, feedback="Refer to Biology123 module!"))

db.session.commit()
db.session.add(Fill(question="1 + 299 = 300", module_code="Maths123", correct="300", difficulty="hard",is_summative=True, feedback="Refer to Maths123 notes, Chapter 2"))
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
db.session.add(User(username="bob", first_name="bob", last_name="bob", email="bob@bob.com", password="123456", is_admin=False,module_1="Fruit123", module_2="Biology123", module_3="Maths123"))
db.session.commit()

Assessment.query.delete()
db.session.commit()
db.session.add(Assessment(assessment_name="Test",is_summative=True, module_code="Fruit123", admin_created=True,
    q1_type="Multiple", q1_id=1, q2_type="Fill", q2_id="1", q3_type="Fill", q3_id="3"))
db.session.commit()



db.session.commit()
