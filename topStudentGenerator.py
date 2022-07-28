import os

student_template = '''
            <!-- Single Card Element -->
            <div class="col-12 col-md-6 col-lg-3">
              <div class="card">
                <img
                  src="./images/student/{sp}"
                  class="card-img-top"
                />
                <div class="card-body">
                  <h5 class="card-title">{sn}</h5>
                  <p class="card-text">{sw}</p>
                </div>
              </div>
            </div>
            <!-- END of Single Card Element -->

'''

students = os.listdir('./images/student/')
student_names = ["Awlad Hossain"," Jannatul Islam", "Imran Hossain", "Nishi Akter"]
student_works = ["UI/UX Designer", "Motion Design", "Graphic Designer", "Web Developer"]

with open("output.txt", "w") as file:
    for i in range(4):
        file.write(student_template.format(sp=students[i], sn=student_names[i], sw=student_works[i]) + "\n")
