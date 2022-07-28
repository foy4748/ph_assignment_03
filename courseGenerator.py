import os

course_pic = os.listdir('./images/course/')
course_template = '''
          <!-- Single Course  -->
          <div class="course outline rounded p-0 col-12 col-lg-6">
            <div class="course-elements d-flex flex-column flex-md-row">
              <div class="course-thumbnail">
                <img
                  src="images/course/{cp}"
                  class="w-100 img-fluid"
                  alt=""
                />
              </div>
              <div
                class="container px-2 mt-3 mt-md-0 ms-md-3 d-md-flex flex-column justify-content-center"
              >
                <h1 class="fs-4">{cn}</h1>
                <p>{cd}</p>
                <h2 class="fs-4"><span class="price">Price: $20</span></h2>
              </div>
            </div>
          </div>
          <!-- END of Single Course  -->
'''

course_names = ["Fundamental Of UI/UX Design", "Javascript Basic to advanced", "Fullstack Web Development", "Digital Marketing", "Photography Basic Rules", "Motion Graphics"]
#Populating course
with open("output.txt","w") as file:
    for i in range(len(course_pic)):
        file.write(course_template.format(cp = course_pic[i], cn = course_names[i], cd= "Learn " + course_names[i] + " at your own pace") + "\n")
