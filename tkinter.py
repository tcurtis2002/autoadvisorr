import tkinter as tk
import requests
from bs4 import BeautifulSoup
import json

# Function to scrape banner data
def scrape_banner():
    url = "http://example.com/banner"  # Replace with actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    courses = []  # List to hold course dictionaries
    # Extract course data (this will depend on the HTML structure)
    for course in soup.find_all('div', class_='course'):
        course_id = course.find('span', class_='course-id').text
        grade = course.find('span', class_='grade').text
        semester = course.find('span', class_='semester').text
        course_number = course.find('span', class_='course-number').text
        courses.append({
            "course_id": course_id,
            "grade": grade,
            "semester": semester,
            "course_number": course_number
        })
    
    return courses

# Function to process courses with advisor info
def process_courses(courses):
    advisor_info = {
        "name": "Advisor Name",
        "email": "advisor@example.com"
    }
    
    course_matrix = {
        "CS101": {
            "course_name": "Introduction to Computer Science",
            "credits": 3
        },
        "MATH201": {
            "course_name": "Calculus II",
            "credits": 4
        }
    }
    
    # Create JSON structure
    data = {
        "advisor": advisor_info,
        "courses": courses,
        "course_matrix": course_matrix
    }

    return json.dumps(data, indent=4)

# Main function to run Tkinter app
def main():
    root = tk.Tk()
    root.title("Course Advisor")

    def on_scrape():
        courses = scrape_banner()
        json_data = process_courses(courses)
        print(json_data)  # or save it to a file

    tk.Button(root, text="Scrape Courses", command=on_scrape).pack()
    root.mainloop()

if __name__ == "__main__":
    main()