import os

course_pic = os.listdir('./images/course/')
course_template = '''

				<!-- Single Course  -->
				<div class="course border rounded p-0 col-12 col-lg-6">
					<div class="course-elements d-flex flex-column flex-md-row">
						<div class="course-thumbnail">
							<img src="images/course/{cp}" class="w-100 img-fluid" alt="" />
						</div>
						<div
							class="course-info px-3 mt-3 mt-md-0  ms-md-5 d-md-flex flex-column justify-content-center">
							<h5>{cn}</h5>
							<p>{cd}</p>
							<h2><span class="price">$20</span></h2>
						</div>
					</div>
				</div>
				<!-- END of Single Course  -->
'''

#Populating course
with open("output.txt","w") as file:
    for course in course_pic:
        file.write(course_template.format(cp = course, cn = course.split(".")[0], cd= "Learn " + course.split(".")[0]+ " at your own pace") + "\n")
