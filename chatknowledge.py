import os
from flask import Flask, request, jsonify, render_template
from google import genai
from flask_cors import CORS
from google.genai import types
import re
from dotenv import load_dotenv

load_dotenv()

# Initialize Flask app
app = Flask(__name__)

        # Initialize the GenAI client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
model = "gemini-2.0-flash"

# Enable CORS
CORS(app)  # Allow cross-origin requests

# # Route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')  # Serving index.html

# Route for the chatbot page (chatbot.html)
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')  # Serving chatbot.html

# Endpoint to interact with the chatbot
@app.route('/questions', methods=['POST'])
def generate_message():
    try:
        # Extract the user input from the JSON body
        user_input = request.form['user_input']
        print("Received user input:", user_input)  # Debug: print the received user input
        if not user_input:
         return jsonify({'error': 'Message not provided'}), 400

        if not user_input:
            return jsonify({'error': 'Message not provided'}), 400

        # Use the generate function to get the bot's response
        full_response = generate(user_input)
        print(f"Generated Response: {full_response}")  # Debugging line

        # Return the bot's response as JSON
        return jsonify({'response': full_response})
    except Exception as e:
        # Handle any exceptions and send an error response
        print(f"Error: {str(e)}")  # Debugging line
        return jsonify({'error': str(e)}), 500


def generate(user_input):
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is the name of the school?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The name of the school is Holy Rosary Academy of Las Pinas City (HRA).
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""where is the school located?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Holy Rosary Academy of Las Pinas City is located at ST. JOSEPH AVE. CORNER NAGA ROAD, PULANGLUPA DOS, LAS PIÑAS CITY, 1740.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""is the school public or private?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""I don't know, I only answer HRA quiries
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""is the school public or private?

answer: private"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that Holy Rosary Academy of Las Pinas City is a **private** school.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""do they have website?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Yes, the website of Holy Rosary Academy of Las Pinas City is hra.edu.ph.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what are the school operating hours?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Holy Rosary Academy of Las Pinas City's operating hours are:

*   **Monday - Friday: 09:00 AM - 5:00 PM**
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what are the contact details of the school?

answer: 
Telephone: (632) 820-8019 / 825-2027
Facsimile: (632) 820-2723

OFFICE OF STUDENT AFFAIRS / GUIDANCE OFFICE
(632) 881-6708

REGISTRAR’S OFFICE
(632) 881-6806

PRINCIPAL’S OFFICE
(632) 881-3667

Email: holyrosaryacademylpc@yahoo.com"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember the contact details of Holy Rosary Academy of Las Pinas City:

*   **Telephone:** (632) 820-8019 / 825-2027
*   **Facsimile:** (632) 820-2723
*   **OFFICE OF STUDENT AFFAIRS / GUIDANCE OFFICE:** (632) 881-6708
*   **REGISTRAR’S OFFICE:** (632) 881-6806
*   **PRINCIPAL’S OFFICE:** (632) 881-3667
*   **Email:** holyrosaryacademylpc@yahoo.com
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""does the school have an official website or social media pages?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Yes, Holy Rosary Academy of Las Pinas City has both an official website and a Facebook page:

*   **Website:** hra.edu.ph
*   **Facebook Page:** Holy Rosary Academy of Las Pinas City (Hra) [https://www.facebook.com/profile.php?id=61557922658937&\\_rdc=3&\\_rdr](https://www.facebook.com/profile.php?id=61557922658937&_rdc=3&_rdr)
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is the school mission and vision?

answer:
Vision
A School for Virtue Centered Leadership.
Mission
Developing lifelong learners and leaders with character and competence.


Slogan
At HRA, every learner is a leader."""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember the school's vision, mission and slogan:

*   **Vision:** A School for Virtue Centered Leadership.
*   **Mission:** Developing lifelong learners and leaders with character and competence.
*   **Slogan:** At HRA, every learner is a leader.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what are the core values of the school?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""I don't have access to the core values of the school. Please check the school website hra.edu.ph or contact the school directly through the contact details I have provided.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is the history of the school?

answer:
School History
School History
Education founded on a love and respect of the Supreme Being superimposes on the learner the values that predicate academic excellence. In our pursuit for excellence, our entire school community dedicates itself to God, country, and the Filipino people.

At Holy Rosary Academy, Education is life and not just a preparation for life.

Humble Beginnings
HRA set sail in 1999 with only four (4) classrooms designed to accommodate seventy five (75) students on the corner of Naga Road and St. Joseph Subdivision, Las Piñas City. What started as a small school born out of its founder Ms. Theresa Galang’s love for children, grew into an institution dedicated to providing students with the skills necessary to tackle the competitive world head on.

Onward Always Onward
Spurred by the requests and support of its parentis, HRA continually grew and expanded.

In 2002, HRA constructed a two floor building to accommodate its first batch of elementary students. Today, the building houses its preschool department.

The following year, in 2003, it put up a five floor building complete with a Multi-Purpose Hall to house an ever growing student population.

At the end of 2005, HRA celebrated its pioneer batch’s elementary graduation with its first Elementary Commencement Exercise.

Immediately after its first elementary graduation, HRA began its Entrepreneurial High School Program designed to provide an advance career guide and instruction for college related subjects in addition to the basic educational requirements. HRA assembled, shortly thereafter, two additionally buildings to house its high school population, a HELE area, and a two floor canteen in order to provide its students a brighter tomorrow.

In 2009, HRA honored its pioneer batch with its First High School Commencement Exercise.

Almost 11 years later, HRA still is committed to provide top quality education as it blazes it way forward.

Preparing for the Future
From humble beginnings, HRA has become an institution committed to preparing and molding students to become the leaders of tomorrow. Through, the collaborative efforts of the entire school community, Rosarians are launched at graduation from HRA armed with the proper ideals, virtues, and knowledge to create a better future for both themselves and the Filipino People."""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember the history of the school as follows:

*   **Founded:** 1999 by Ms. Theresa Galang.
*   **Initial Size:** Started with four classrooms and 75 students at the corner of Naga Road and St. Joseph Subdivision, Las Piñas City.
*   **Growth:** Expanded due to parental requests and support.
*   **2002:** Constructed a two-floor building for elementary students (now houses the preschool department).
*   **2003:** Built a five-floor building with a Multi-Purpose Hall.
*   **2005:** Celebrated its first Elementary Commencement Exercise.
*   **Entrepreneurial High School Program:** Introduced to provide career guidance and advanced instruction.
*   **2009:** Held its First High School Commencement Exercise.
*   **Commitment:** Continues to provide quality education and prepare students to be future leaders.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""is the school?

answer: 
yes, DepEd"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""I'm sorry, I don't understand. Are you asking if Holy Rosary Academy of Las Pinas City is accredited by the Department of Education (DepEd)? If so, the answer is yes.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""who is the school president or principal?

answer: Ma. Theresa M. Galang"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school president or principal is Ma. Theresa M. Galang.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Who are the vice-principals or assistant principals?

answer: none"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that Holy Rosary Academy of Las Pinas City has no vice-principals or assistant principals.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""who is the school director or superintendent? 

answer: Armando Galang"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school director or superintendent is Armando Galang.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""who are the members of the school board? 

answer: 
Armando B. Galang - Director
Ma. Theresa M. Galang - Directress/Principal
Atty. Arman Jason M. Galang - Legal
Dr. John Christian M. Galang - Medical Consultant"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember the members of the school board are:

*   Armando B. Galang - Director
*   Ma. Theresa M. Galang - Directress/Principal
*   Atty. Arman Jason M. Galang - Legal
*   Dr. John Christian M. Galang - Medical Consultant
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""who is in charge of academic affairs?

answer: Celsa Santos"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that Celsa Santos is in charge of academic affairs.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""who is the head of student affairs or student services?

answer: Dorothy Quinico"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that Dorothy Quinico is the head of student affairs or student services.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""who is the school registrar?

answer: Nanette V. Canlas"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that Nanette V. Canlas is the school registrar.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Who is the guidance counselor?

answer: Hannah Grace E. Sayas - grade 11
Kimberly O. Marcos - grade 12"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the guidance counselors are:

*   Hannah Grace E. Sayas - Grade 11
*   Kimberly O. Marcos - Grade 12
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""who handles discipline and student conduct?

answer: Guidance Office"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the Guidance Office handles discipline and student conduct.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""who is responsible for school security?

answer: Administration"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the Administration is responsible for school security.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what are the requirements for enrollment?

answer: ID 1x1, Report Card, Birth Certificate"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the requirements for enrollment are:

*   ID 1x1
*   Report Card
*   Birth Certificate
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""when is the enrollment period?

answer: october to august"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the enrollment period is from October to August.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""is there an entrance exam?

answer: none
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there is no entrance exam.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there scholarships or financial assistance programs?

answer: voucher from government"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the only scholarship or financial assistance program available is a voucher from the government.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""does the school accept transferees? 

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that Holy Rosary Academy of Las Pinas City accepts transferees.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""can students transfer during the 2nd semester? 

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that students can transfer during the 2nd semester.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what are the requirements for transferring in the 2nd semester?

answer: ID 1x1. Report Card, Birth Cert"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the requirements for transferring in the 2nd semester are:

*   ID 1x1
*   Report Card
*   Birth Certificate
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""can students shift to a different strand after enrolling?

answer: No"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that students cannot shift to a different strand after enrolling.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what academic tracs and strands are available? 

answer: ABM, HUMSS, STEM, GAS, """),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the available academic tracks and strands are:

*   ABM (Accountancy, Business, and Management)
*   HUMSS (Humanities and Social Sciences)
*   STEM (Science, Technology, Engineering, and Mathematics)
*   GAS (General Academic Strand)
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""how are students assessed?

answer:  formative, quarterly, exams, Unit test, Quizzes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that students are assessed through:

*   Formative assessments
*   Quarterly exams
*   Unit tests
*   Quizzes
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is the school's policy on failing grades?

answer: if 4 failed subjects, repeat the level"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school's policy on failing grades is: if a student fails 4 subjects, they must repeat the level.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Does the school have partnerships with universities and industries?

answer: yes
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school has partnerships with universities and industries.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What clubs and organizations can students join?

answer: Glee, Art, Taekwondo, Dance, Basketball, Volleyball, etc."""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the clubs and organizations students can join include:

*   Glee
*   Art
*   Taekwondo
*   Dance
*   Basketball
*   Volleyball
*   etc.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there sports teams or athletic program?

answer: yes, volleyball, basketball, chess, badminton, etc."""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school has sports teams or athletic programs for:

*   Volleyball
*   Basketball
*   Chess
*   Badminton
*   etc.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""does the school have a student government?

answer: yes, SSG"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school has a student government called SSG (Supreme Student Government).
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there school events like fairs, intramurals, or talent shows? 

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school holds school events like fairs, intramurals, or talent shows.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""does the school offer advanced placement or honors classes?

answer: no"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school does not offer advanced placement or honors classes.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""does the school offer arts, music, or drama programs?

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school offers arts, music, or drama programs.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what leadership programs are available for students?

answer: THE LEADER IN ME PROGRAM"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school offers \"The Leader In Me\" Program as a leadership program for students.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there school publications or journalism programs? 

answer: yes, The Tribune"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school has a school publication called \"The Tribune,\" indicating a journalism program.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are field trips or educational tours part of the curriculum?

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that field trips or educational tours are part of the curriculum.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""how can students start their own club or organization?

answer: school handles this program"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school handles the program for starting a club or organization. Students should inquire with the appropriate school personnel (likely student affairs or a similar department) to initiate the process.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""does the school have library and media center?

answer: yes
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school has a library and media center.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there transportation services available?

answer: no, own serivice"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school does not provide transportation services; students must arrange their own transportation.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there dormitories or housing options for students? 

answer: none"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there are no dormitories or housing options for students.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is the policy in bringing outside food?

answer: no such policy"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there is no specific policy against bringing outside food.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""is there a parent-teacher association(PTA)?

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there is a Parent-Teacher Association (PTA).
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""how does the school communicate with parents?

answer: conference, notice"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school communicates with parents through conferences and notices.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""can parents volunteer in school activities?

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that parents can volunteer in school activities.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is the process for raising concerns or complaints?

answer: set for appointment"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the process for raising concerns or complaints is to set an appointment.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there parenting seminars or workshops?

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there are parenting seminars or workshops.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there school programs where parents can participate?

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there are school programs where parents can participate.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""can parents request special assistance for their child's learning need?

answer: yes, remediation"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that parents can request special assistance for their child's learning needs, such as remediation.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there intership or work immersion opportunities?

answer: yes
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there are internship or work immersion opportunities available.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""how does the school help students apply for college?

answer: career talk"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school helps students apply for college through career talks. For further information please contact the Guidance Office at (632) 881-6708 or the Registrar's Office at (632) 881-6806, or visiting the school website at hra.edu.ph to find this information
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""does the school assist in university scholarships application?

answer: yes
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school assists in university scholarship applications. For further information please contact the Guidance Office at (632) 881-6708 or the Registrar's Office at (632) 881-6806, or visiting the school website at hra.edu.ph to find this information
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""how can students request transcripts for diplomas?

answer: write a letter of request via email"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that students can request transcripts or diplomas by writing a letter of request via email to holyrosaryacademylpc@yahoo.com
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there alumni support programs?

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there are alumni support programs. For further information please contact the Registrar's Office at (632) 881-6806, or visiting the school website at hra.edu.ph to find this information
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""does the school offer training for entrance exams like UPCAT, ACET, and others?

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the school offers training for entrance exams like UPCAT, ACET, and others.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what documents are required for the application?

answer: none"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""I think there might be a misunderstanding. You asked what documents are required for the application, and I have been instructed to answer as a Registrar from HRA.

If you are asking about college entrance exam training, I do not have that information.

If you meant enrollment in HRA, then I would need:

*   ID 1x1
*   Report Card
*   Birth Certificate
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""is there an application fee? if so, how much? 

answer: none
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there is no application fee.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is the deadline for submitting applications?

answer: a year ahead"""),
            ],
        ),  
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the deadline for submitting applications is a year ahead.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""how will I know if my application is accepted?

answer: receiving notice"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that you will know if your application is accepted by receiving a notice.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""is there an orientation program for new students?

answer: yes"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there is an orientation program for new students.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is the procedure for students with special needs to apply?

answer: via interview"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that the procedure for students with special needs to apply is via an interview. For further information please contact the Guidance Office at (632) 881-6708
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""is there an age limit for enrolling in senior high school?

answer: none"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there is no age limit for enrolling in senior high school.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""can I transfer my credits from another school? what is the process?

answer: REPORT CARD"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that to transfer credits from another school, you need to present your Report Card. You may want to contact the Registrar’s Office at (632) 881-6806 for the complete steps.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""is there waiting list for incoming students?

answer: none"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there is no waiting list for incoming students.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what should i do if I miss the application deadline?

answer: definitely no acceptance"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that if you miss the application deadline, there will definitely be no acceptance.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""are there additional support services for new students adjusting to school life?

answer: none
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that there are no additional support services for new students adjusting to school life.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""can I apply for early admission or advance registration?

answer: yes
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I understand. I will remember that you can apply for early admission or advance registration.
"""),
            ],
        ),   
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)],  # Dynamic user input
        )
        
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""Act as a registrar at Holy Rosary Academy of Las Pinas CIty (HRA).

            The School exact location at ST. JOSEPH AVE. CORNER NAGA ROAD, PULANGLUPA DOS, LAS PIÑAS CITY, 1740.

            The school open hours: 
            OPEN TIME 09:00 - 17:00
            MONDAY - FRIDAYwhat

            If the query is not related to Holy Rosary Academy of Las Pinas (HRA) say "I" don't know, I only answer HRA queries" but have some personality like you're really a human.
                                 
            if they continue asking you questions that is not related to HRA, say "Oh I am tired na sa ganyang mga tanong, nandito ako bes para sumagot ng tanong related sa HRA paalala ko lang." and use emoji accordingly.
                                 
            there is a tuition fee, but there is a government support or voucher to cover the tuition fee of the students. 
            the tuition without utilizing the voucher is 22,500 pesos.
            there will be a 500 cost to cover the deficit since voucher only cover 22,000 pesos.
                                 
            don't mention or give information that is not being asked, analyze what the user saying, and reply accordingly while adhering to the other instruction.
                                 
            use emoticons or emoji accordingly.
            
            try to use tagalog and english when you are joking with the user or when you are answering about something that is not HRA related.                     

            website of the HRA : hra.edu.ph
            facebook page: Holy Rosary Academy of Las Pinas City  (Hra) https://www.facebook.com/profile.php?id=61557922658937&_rdc=3&_rdr#
            //hra.edu.ph/"""),
        ],
    )

      # Initialize the response variable to accumulate chunks
    full_response = ""

    # Request content from the trained model
    for chunk in client.models.generate_content_stream(
    model=model,
    contents=contents,
    config=generate_content_config,
    ):
        if chunk.candidates and chunk.candidates[0].content:
            # Process the chunk's text content
            if chunk.candidates[0].content.parts:
                response_text = chunk.candidates[0].content.parts[0].text
                full_response += response_text
    # Return the full response after all chunks have been processed
    return full_response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Run the app
    