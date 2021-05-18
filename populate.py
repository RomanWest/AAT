from aat import db
from aat.models import Assessment, Multiple, Fill, User
from datetime import datetime

Multiple.query.delete()
db.session.commit()
# Multiple Fruit Easy Formative
# Multiple Fruit Med Formatvie
# Multiple Fruit Hard Formative
# Multiple Fruit Easy Summative
db.session.add(Multiple(question="What colour is a banana?", correct="yellow", module_code="Fruit123", incorrect_1="blue",
               incorrect_2="red", incorrect_3="purple", difficulty="easy", is_summative=True, feedback="Refer to Fruit123 module!"))
db.session.commit()
db.session.add(Multiple(question="Which of the following is a citric fruit?", correct="orange", module_code="Fruit123", incorrect_1="apple",
               incorrect_2="pear", incorrect_3="kiwi", difficulty="easy", is_summative=True, feedback="Refer to Fruit123 module!"))
db.session.commit()
db.session.add(Multiple(question="Where do bananas grow?", correct="a tree", module_code="Fruit123", incorrect_1="underground",
               incorrect_2="in caves", incorrect_3="in a lab", difficulty="easy", is_summative=True, feedback="Refer to Fruit123 module!"))
db.session.commit()
# Multiple Fruit Medium Summative
db.session.add(Multiple(question="apples are what colour?", correct="red", module_code="Fruit123", incorrect_1="black",
               incorrect_2="blue", incorrect_3="purple", difficulty="medium", is_summative=True, feedback="Refer to Fruit123 module!"))
db.session.commit()
db.session.add(Multiple(question="Which of the following is not a fruit?", correct="potato", module_code="Fruit123", incorrect_1="apple",
               incorrect_2="grape", incorrect_3="lemon", difficulty="medium", is_summative=True, feedback="Refer to Fruit123 module!"))
db.session.commit()
db.session.add(Multiple(question="What fruit is similar to a lemon?", correct="lime", module_code="Fruit123", incorrect_1="banana",
               incorrect_2="apple", incorrect_3="aubergine", difficulty="medium", is_summative=True, feedback="Refer to Fruit123 module!"))
db.session.commit()
# Multiple Fruit Hard Summative
db.session.add(Multiple(question="What fruit has a similar texture to potato?", correct="apple", module_code="Fruit123", incorrect_1="mango",
               incorrect_2="avocado", incorrect_3="orange", difficulty="hard", is_summative=True, feedback="Refer to Fruit123 module!"))
db.session.commit()
db.session.add(Multiple(question="what is an apple?", correct="fruit", module_code="Fruit123", incorrect_1="vegetable",
               incorrect_2="herb", incorrect_3="cushion", difficulty="hard", is_summative=True, feedback="Refer to Fruit123 module!"))
db.session.commit()
db.session.add(Multiple(question="Where do apples grow?", correct="everywhere", module_code="Fruit123", incorrect_1="Europe",
               incorrect_2="Africa", incorrect_3="Asia", difficulty="hard", is_summative=True, feedback="Refer to Fruit123 module!"))

db.session.commit()
# Multiple Biology Easy Formative
db.session.add(Multiple(question="How many eyes do humans have?", correct="Two", module_code="Biology123",
                        incorrect_1="One", incorrect_2="Three", incorrect_3="Four", difficulty="easy", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="How many feet do elephants have?", correct="Four", module_code="Biology123",
                        incorrect_1="One", incorrect_2="Three", incorrect_3="Two", difficulty="easy", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="What colour is a giraffe?", correct="Yellow", module_code="Biology123",
                        incorrect_1="Green", incorrect_2="Blue", incorrect_3="Grey", difficulty="easy", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
# Multiple Biology Medium Formative
db.session.add(Multiple(question="How many legs do spiders have?", correct="Eight", module_code="Biology123",
                        incorrect_1="Two", incorrect_2="Six", incorrect_3="Four", difficulty="medium", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="Tigers are related to what animal?", correct="Cat", module_code="Biology123",
                        incorrect_1="Dog", incorrect_2="Fish", incorrect_3="Humans", difficulty="medium", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="What do humans eat with?", correct="Their mouths", module_code="Biology123",
                        incorrect_1="Their eyes", incorrect_2="Their ears", incorrect_3="Their feet", difficulty="medium", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
# Multiple Biology Hard Formative
db.session.add(Multiple(question="What diet do cats have?", correct="Omnivorous", module_code="Biology123",
                        incorrect_1="Vegetarian", incorrect_2="Pescatarian", incorrect_3="Canivorous", difficulty="hard", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="What spectrum can bees see in?", correct="Ultraviolet", module_code="Biology123",
                        incorrect_1="X-ray", incorrect_2="Gamma", incorrect_3="Infrared", difficulty="hard", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="how many toes do dogs have?", correct="Eighteen", module_code="Biology123",
                        incorrect_1="Ten", incorrect_2="Four", incorrect_3="Twenty", difficulty="hard", is_summative=False, feedback="Refer to Biology123 module!"))
db.session.commit()
# Multiple Biology Easy Summative
db.session.add(Multiple(question="What is the name for your finger closest to your thumb?", correct="Index finger", module_code="Biology123",
                        incorrect_1="Ring finger", incorrect_2="Middle finger", incorrect_3="Pinky finger", difficulty="easy", is_summative=True, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="What do humans walk on?", correct="Their feet", module_code="Biology123",
                        incorrect_1="Their hands", incorrect_2="Their knees", incorrect_3="Their elbows", difficulty="easy", is_summative=True, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="Which of the following animals does not have a tail?", correct="Chimpanze", module_code="Biology123",
                        incorrect_1="Cat", incorrect_2="Dog", incorrect_3="Sheep", difficulty="easy", is_summative=True, feedback="Refer to Biology123 module!"))
db.session.commit()
# Multiple Biology Med Summative
db.session.add(Multiple(question="How many bones are in the human body?", correct="Two Hundred and Six", module_code="Biology123",
                        incorrect_1="One hundred and Ninety Four", incorrect_2="Twnety Six", incorrect_3="Two Hundred and Eighty Five", difficulty="medium", is_summative=True, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="Which of the following is not commonly a domestic pet?", correct="Hippopotamus", module_code="Biology123",
                        incorrect_1="Cat", incorrect_2="Dog", incorrect_3="Rat", difficulty="medium", is_summative=True, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="Which of the following animals does not have a tail?", correct="Chimpanze", module_code="Biology123",
                        incorrect_1="Cat", incorrect_2="Dog", incorrect_3="Sheep", difficulty="medium", is_summative=True, feedback="Refer to Biology123 module!"))
db.session.commit()
# Multiple Biology Hard Summative
db.session.add(Multiple(question="Which of the following animals does not have a tail?", correct="Chimpanze", module_code="Biology123",
                        incorrect_1="Cat", incorrect_2="Dog", incorrect_3="Sheep", difficulty="hard", is_summative=True, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="What animal spawns tadpoles?", correct="Frogs", module_code="Biology123",
                        incorrect_1="Donkeys", incorrect_2="Mice", incorrect_3="Elephants", difficulty="hard", is_summative=True, feedback="Refer to Biology123 module!"))
db.session.commit()
db.session.add(Multiple(question="Which domestic animal is the best?", correct="Cat", module_code="Biology123",
                        incorrect_1="Dog", incorrect_2="Donkey", incorrect_3="Lizard", difficulty="hard", is_summative=True, feedback="Refer to Biology123 module!"))
db.session.commit()

# Multiple Maths Easy Formative
db.session.add(Multiple(question="How many sides does a square have?", correct="Four", module_code="Maths123",
                        incorrect_1="Three", incorrect_2="Two", incorrect_3="One", difficulty="easy", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
db.session.add(Multiple(question="How many faces are on a sphere?", correct="One", module_code="Maths123",
                        incorrect_1="Six", incorrect_2="Four", incorrect_3="Two", difficulty="easy", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
db.session.add(Multiple(question="How many corners does a triangle have?", correct="Three", module_code="Maths123",
                        incorrect_1="Two", incorrect_2="Four", incorrect_3="One", difficulty="easy", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
# Multiple Maths Medium Formative
db.session.add(Multiple(question="How many sides does a rhombus have?", correct="Four", module_code="Maths123",
                        incorrect_1="Two", incorrect_2="One", incorrect_3="Three", difficulty="medium", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
db.session.add(Multiple(question="How many edges does a dodecahedron have?", correct="Twelve", module_code="Maths123",
                        incorrect_1="Two", incorrect_2="Four", incorrect_3="Ten", difficulty="medium", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
db.session.add(Multiple(question="How many faces does a square have?", correct="One", module_code="Maths123",
                        incorrect_1="Six", incorrect_2="Four", incorrect_3="Two", difficulty="medium", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
# Multiple Maths Hard Formative
db.session.add(Multiple(question="How many degrees do all of the angles in a square add up to?", correct="Three Hundred and Sixty", module_code="Maths123",
                        incorrect_1="One Hundred and Eighty", incorrect_2="Ninety", incorrect_3="Thirty", difficulty="hard", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
db.session.add(Multiple(question="What is pythagoras's theorum?", correct="a^2 + b^2 = c^2", module_code="Maths123",
                        incorrect_1="a + b = c", incorrect_2="a + b = 2c", incorrect_3="e = m c^2", difficulty="hard", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
db.session.add(Multiple(question="What maths topic revolves around right handed triangles?", correct="Trigonometry", module_code="Maths123",
                        incorrect_1="Statistics", incorrect_2="Simultaneous Equations", incorrect_3="Differentiation", difficulty="hard", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
# Multiple Maths Easy Summative
db.session.add(Multiple(question="x * 2 =", correct="2x", module_code="Maths123",
                        incorrect_1="x", incorrect_2="y", incorrect_3="x^2", difficulty="easy", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
db.session.add(Multiple(question="100 + 50 =", correct="150", module_code="Maths123",
                        incorrect_1="100", incorrect_2="50", incorrect_3="500", difficulty="easy", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
db.session.add(Multiple(question="5 * 2 =", correct="10", module_code="Maths123",
                        incorrect_1="5", incorrect_2="100", incorrect_3="20", difficulty="easy", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
# Multiple Maths Med Summative
db.session.add(Multiple(question="500 - - 20 =", correct="520", module_code="Maths123",
                        incorrect_1="480", incorrect_2="500", incorrect_3="50", difficulty="medium", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
db.session.add(Multiple(question="3 * 5 + 2 =", correct="17", module_code="Maths123",
                        incorrect_1="21", incorrect_2="7", incorrect_3="15", difficulty="medium", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
db.session.add(Multiple(question="What category does trigonometry belong to?", correct="Calculus", module_code="Maths123",
                        incorrect_1="Statistics", incorrect_2="Mechanics", incorrect_3="Differentiation", difficulty="medium", is_summative=False, feedback="Refer to Maths123 module!"))
db.session.commit()
# Multiple Maths Hard Summative

Fill.query.delete()
db.session.commit()
db.session.add(Fill(question="A tree is made from wood", module_code="Fruit123", correct="wood", difficulty="easy",
    is_summative=False, feedback="Refer to Fruit123 module!"))
db.session.commit()
db.session.add(Fill(question="1 + 299 = 300", module_code="Maths123", correct="300", difficulty="hard",
                    is_summative=True, feedback="Refer to Maths123 notes, Chapter 2"))
db.session.commit()
db.session.add(Fill(question="The colour of grass is green", module_code="Fruit123", correct="green", difficulty="easy",
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
db.session.add(Assessment(assessment_name="Test",is_summative=True, module_code="Fruit123", admin_created=True, 
    q1_type="Multiple", q1_id=1, q2_type="Fill", q2_id="1", q3_type="Fill", q3_id="3", feedback_date=datetime(2021,5,19)))
db.session.commit()

db.session.commit()
db.session.add(Assessment(assessment_name="Test2",is_summative=False, module_code="Maths123", admin_created=True, 
    q1_type="Multiple", q1_id="1", q2_type="Multiple", q2_id="2", q3_type="Multiple", q3_id="3", feedback_date=datetime(2021,5,18)))
db.session.commit()
db.session.add(Assessment(assessment_name="Assessment 3",is_summative=False, module_code="Biology123", admin_created=True, 
    q1_type="Multiple", q1_id="5", q2_type="Multiple", q2_id="10", q3_type="Fill", q3_id="4"))
db.session.commit()

