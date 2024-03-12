import csv
import random

# Define the course data
course_data = [
    ["course_name", "course_description", "course_duration", "course_level", "credits_offered", "prerequisites", "class_size", "instructor_information"],
    ["Psychology", "An introductory course covering basic principles of psychology including perception, cognition, learning, and motivation.", "12 weeks", "Undergraduate", "3 credits", "None", "30", "Dr. Emily Adhiambo"],
    ["Analytical Chemistry", "Fundamental principles of Analytical chemistry, including nomenclature, stereochemistry, and reaction mechanisms.", "16 weeks", "Undergraduate", "4 credits", "General Chemistry", "25", "Dr. Michael Kimani"],
    ["Computer Science", "Introduction to programming concepts and problem-solving techniques using a high-level programming language.", "14 weeks", "Undergraduate", "3 credits", "None", "40", "Prof. Sarah Lumumba"],
    ["Economics", "Introduction to economic theory, covering topics such as supply and demand, consumer behavior, and market structures.", "15 weeks", "Undergraduate", "3 credits", "Introductory Economics", "35", "Dr. David Bokelo"],
    ["Literature", "Developing writing skills through the study of various genres and rhetorical strategies.", "13 weeks", "Undergraduate", "3 credits", "Placement Test", "20", "Prof. Laura Muthaka"],
    ["Mathematics", "Introduction to differential calculus, covering limits, continuity, derivatives, and their applications.", "16 weeks", "Undergraduate", "4 credits", "Pre-Calculus", "30", "Dr. James Taiyo"],
    ["Sociology", "Exploration of sociological concepts and theories, including culture, socialization, and social institutions.", "14 weeks", "Undergraduate", "3 credits", "None", "25", "Dr. Jessica Wanjiku"],
    ["Marketing", "Introduction to the principles and practices of marketing, including market analysis, product development, and promotion strategies.", "15 weeks", "Undergraduate", "3 credits", "None", "30", "Prof. Brian Juma"],
    ["Physics", "Introduction to fundamental principles of physics, including mechanics, thermodynamics, and electromagnetism.", "16 weeks", "Undergraduate", "4 credits", "Algebra-based Physics", "25", "Dr. Jennifer Anyango"],
    ["Spanish Language and Culture I", "Introduction to basic Spanish language skills, including speaking, listening, reading, and writing.", "14 weeks", "Undergraduate", "3 credits", "None", "20", "Prof. Maria Raburu"],
    ["Statistics", "Introduction to statistical concepts and methods, including descriptive statistics, probability, and hypothesis testing.", "13 weeks", "Undergraduate", "3 credits", "Algebra", "35", "Dr. William Danda"],
    ["Applied Biology I", "Introduction to biological principles, including cellular structure, genetics, and evolution.", "15 weeks", "Undergraduate", "4 credits", "High School Biology", "30", "Dr. Sarah Telimu"],
    ["Ethics", "Examination of ethical issues in business, including corporate social responsibility, ethical decision-making, and stakeholder management.", "14 weeks", "Undergraduate", "3 credits", "None", "25", "Dr. Robert Hadija"],
    ["World History: Prehistory", "Survey of world history from prehistory to 1500 CE, focusing on major civilizations and historical developments.", "16 weeks", "Undergraduate", "3 credits", "None", "40", "Prof. Elizabeth Tugen"],
    ["Photography and graphic design", "Introduction to digital photography techniques, including composition, exposure, and editing using industry-standard software.", "14 weeks", "Undergraduate", "3 credits", "None", "20", "Prof. Michael Bosire"],
    ["Philosophy", "Introduction to major philosophical questions and theories, including ethics, metaphysics, and epistemology.", "13 weeks", "Undergraduate", "3 credits", "None", "25", "Dr. Thomas Wikanga"],
    ["Art", "Survey of art history from ancient civilizations to the medieval period, covering major artistic movements and styles.", "16 weeks", "Undergraduate", "3 credits", "None", "30", "Prof. Jennifer Lenana"],
    ["Environmental Science", "Introduction to environmental science, covering topics such as ecosystems, biodiversity, and human impacts on the environment.", "15 weeks", "Undergraduate", "3 credits", "None", "25", "Dr. Richard Musinde"],
    ["Political Science", "Introduction to political science, covering topics such as political institutions, ideologies, and international relations.", "14 weeks", "Undergraduate", "3 credits", "None", "35", "Dr. Amanda Kabugwa"],
    ["French", "Introduction to basic French language skills, including speaking, listening, reading, and writing.", "14 weeks", "Undergraduate", "3 credits", "None", "20", "Prof. Philip Mogaka"],
    ["Music", "Introduction to music theory concepts, including notation, scales, intervals, and basic harmony.", "13 weeks", "Undergraduate", "3 credits", "None", "25", "Dr. Katherine Esire"],
    ["Anthropology", "Introduction to the study of human cultures and societies, including cultural anthropology, archaeology, and biological anthropology.", "14 weeks", "Undergraduate", "3 credits", "None", "30", "Dr. Michael Awiti"],
    ["Civic Engineering", "Introduction to engineering principles and problem-solving techniques, including hands-on projects and design challenges.", "15 weeks", "Undergraduate", "3 credits", "Algebra", "35", "Prof. Christopher Jelimu"]
]

search_trends_data = [
    ["most_searched_courses", "frequency_of_searches", "popular_search_terms"],
    ["Computer Science", "1200", "Python programming, Java programming, Web development"],
    ["Data Science", "1000", "Machine learning, Data analysis, Python programming"],
    ["Finance", "900", "Investment, Financial markets, Corporate finance"],
    ["Medicine", "800", "Medical school, Anatomy, Physiology"],
    ["Psychology", "700", "Clinical psychology, Cognitive psychology, Behavioral psychology"],
    ["Business Administration", "600", "MBA programs, Marketing, Entrepreneurship"],
    ["Engineering", "500", "Mechanical engineering, Civil engineering, Electrical engineering"],
    ["Art and Design", "400", "Graphic design, Fine arts, Photography"],
    ["Applied Biology", "300", "Genetics, Ecology, Microbiology"],
    ["Languages", "200", "Spanish language, French language, Mandarin Chinese"],
]

traffic_analysis_data = [
    ["course", "page_views", "time_spent", "bounce_rate"],
    ["Psychology", "1500", "3 minutes", "30%"],
    ["Analytical Chemistry I", "1200", "4 minutes", "25%"],
    ["Computer Science", "1800", "5 minutes", "20%"],
    ["Economics", "1300", "3.5 minutes", "28%"],
    ["Literature", "1600", "4 minutes", "22%"],
    ["Mathematics", "1400", "4.5 minutes", "24%"],
    ["Sociology", "1700", "4 minutes", "21%"],
    ["Principles of Marketing", "1550", "3.8 minutes", "23%"],
    ["Physics", "1350", "4.2 minutes", "26%"],
    ["Spanish Language and Culture I", "1450", "3.7 minutes", "27%"],
    # Add more data rows here...
    ["Art: Ancient to Medieval", "1250", "3.2 minutes", "29%"],
    ["Environmental Science", "1650", "4.3 minutes", "20%"],
    ["Political Science", "1520", "3.9 minutes", "22%"],
    ["Music", "1420", "3.6 minutes", "28%"],
    ["Anthropology", "1480", "4 minutes", "25%"],
    ["Civic Engineering", "1750", "4.5 minutes", "21%"],
    ["Computer Networks", "1320", "3.8 minutes", "26%"],
    ["Philosophy", "1680", "4.2 minutes", "23%"],
    ["Digital Marketing", "1620", "4 minutes", "22%"],
]

user_interactions_data = [
    ["course", "click_through_rates", "conversion_rates", "feedback_and_comments"],
    ["Psychology", "25%", "10%", "Positive feedback on course structure and instructor"],
    ["Organic Chemistry I", "20%", "8%", "Some students found the course challenging but rewarding"],
    ["Computer Science", "30%", "12%", "Many students appreciated the hands-on coding exercises"],
    ["Principles of Microeconomics", "18%", "7%", "Some students requested more real-world examples"],
    ["Literature", "35%", "15%", "Students found the instructor's feedback helpful for improving writing skills"],
    ["Mathematics", "22%", "9%", "Positive feedback on instructor's teaching style"],
    ["Sociology", "28%", "11%", "Students enjoyed the interactive discussions in class"],
    ["Principles of Marketing", "31%", "13%", "Some students suggested more guest lectures from industry professionals"],
    ["Physics", "19%", "8%", "Positive feedback on the clarity of course materials"],
    ["Spanish Language and Culture I", "26%", "10%", "Students appreciated the cultural immersion activities"],
    # Add more data rows here...
    ["Art and Design", "29%", "12%", "Students found the course material fascinating but dense"],
    ["Environmental Science", "24%", "10%", "Positive feedback on the relevance of course content to current environmental issues"],
    ["Political Science", "27%", "11%", "Some students suggested more interactive activities during lectures"],
    ["French", "23%", "9%", "Students found the pronunciation drills helpful for improving speaking skills"],
    ["Music", "21%", "8%", "Positive feedback on the instructor's passion for music"],
    ["Anthropology", "28%", "12%", "Students enjoyed the fieldwork assignments and guest lectures"],
    ["Engineering", "32%", "13%", "Some students suggested more hands-on experiments in the lab sessions"],
    ["Computer Networks", "34%", "14%", "Positive feedback on the relevance of course material to industry certifications"],
    ["Philosophy", "26%", "11%", "Students appreciated the depth of philosophical discussions in class"],
    ["Digital Marketing", "33%", "15%", "Some students suggested more case studies from real-world marketing campaigns"],
]

engagement_metrics_data = [
    ["course", "requests_for_more_information", "course_related_downloads", "related_webinars_events"],
    ["Psychology", "15", "20", "2"],
    ["Organic Chemistry I", "12", "18", "3"],
    ["Computer Science", "18", "22", "4"],
    ["Principles of Microeconomics", "10", "15", "1"],
    ["English Composition I", "20", "25", "3"],
    ["Mathematics", "14", "20", "2"],
    ["Sociology", "16", "18", "2"],
    ["Principles of Marketing", "18", "20", "3"],
    ["Physics", "10", "15", "1"],
    ["Spanish Language and Culture I", "12", "18", "2"],
    # Add more data rows here...
    ["Art and Design", "14", "20", "2"],
    ["Environmental Science", "16", "18", "2"],
    ["Political Science", "18", "20", "3"],
    ["French", "10", "15", "1"],
    ["Music", "12", "18", "2"],
    ["Anthropology", "15", "20", "2"],
    ["Engineering", "18", "22", "4"],
    ["Computer Networks", "20", "25", "3"],
    ["Philosophy", "14", "20", "2"],
    ["Digital Marketing", "16", "18", "2"],
]

time_trends_data = [
    ["course", "change_in_popularity_over_time", "seasonal_variation_in_interest"],
    ["Psychology", "Steady increase", "Higher interest during fall and spring semesters"],
    ["Organic Chemistry I", "Fluctuating", "Higher interest during spring semester"],
    ["Computer Science", "Consistent high demand", "Constant interest throughout the year"],
    ["Principles of Microeconomics", "Decreasing", "Higher interest during fall semester"],
    ["English Composition I", "Steady increase", "Stable interest throughout the year"],
    ["Mathematics", "Fluctuating", "Higher interest during fall and spring semesters"],
    ["Sociology", "Increasing", "Stable interest throughout the year"],
    ["Principles of Marketing", "Stable", "Constant interest throughout the year"],
    ["Physics", "Decreasing", "Higher interest during spring semester"],
    ["Spanish Language and Culture I", "Fluctuating", "Higher interest during fall semester"],
    # Add more data rows here...
    ["Art and Design", "Increasing", "Stable interest throughout the year"],
    ["Environmental Science", "Steady increase", "Higher interest during fall and spring semesters"],
    ["Political Science", "Decreasing", "Higher interest during fall semester"],
    ["French", "Fluctuating", "Higher interest during spring semester"],
    ["Music", "Stable", "Constant interest throughout the year"],
    ["Anthropology", "Increasing", "Stable interest throughout the year"],
    ["Engineering", "Steady increase", "Higher interest during fall and spring semesters"],
    ["Computer Networks", "Decreasing", "Higher interest during fall semester"],
    ["Philosophy", "Fluctuating", "Higher interest during spring semester"],
    ["Digital Marketing", "Stable", "Constant interest throughout the year"],
]

referral_sources_data = [
    ["course", "where_visitors_are_coming_from", "marketing_channels_effectiveness"],
    ["Psychology", "Search engines", "High"],
    ["Organic Chemistry I", "Social media", "Moderate"],
    ["Computer Science", "Direct traffic", "High"],
    ["Principles of Microeconomics", "Referral websites", "Low"],
    ["English Composition I", "Email campaigns", "Moderate"],
    ["Mathematics", "Search engines", "High"],
    ["Sociology", "Social media", "Moderate"],
    ["Principles of Marketing", "Direct traffic", "High"],
    ["Physics", "Referral websites", "Low"],
    ["Spanish Language and Culture I", "Search engines", "High"],
    # Add more data rows here...
    ["Art and Design", "Email campaigns", "Moderate"],
    ["Environmental Science", "Direct traffic", "High"],
    ["Political Science", "Referral websites", "Low"],
    ["French", "Social media", "Moderate"],
    ["Music", "Search engines", "High"],
    ["Anthropology", "Direct traffic", "High"],
    ["Engineering", "Social media", "Moderate"],
    ["Computer Networks", "Referral websites", "Low"],
    ["Philosophy", "Email campaigns", "Moderate"],
    ["Digital Marketing", "Search engines", "High"],
]

device_usage_data = [
    ["type_of_device", "conversion_rates"],
    ["Desktop", "12%"],
    ["Mobile", "15%"],
    ["Tablet", "10%"],
    ["Desktop", "14%"],
    ["Mobile", "16%"],
    ["Tablet", "11%"],
    ["Desktop", "13%"],
    ["Mobile", "17%"],
    ["Tablet", "12%"],
    ["Desktop", "15%"],
    # Add more data rows here...
    ["Mobile", "18%"],
    ["Tablet", "13%"],
    ["Desktop", "16%"],
    ["Mobile", "19%"],
    ["Tablet", "14%"],
    ["Desktop", "17%"],
    ["Mobile", "20%"],
    ["Tablet", "15%"],
    ["Desktop", "18%"],
    ["Mobile", "21%"],
    ["Tablet", "16%"],
    ]

competitor_analysis_data = [
    ["curse", "comparison_with_competitors", "benchmarking_against_similar_courses"],
    ["Psychology", "Similar content, competitive pricing", "Average enrollment rate compared to similar courses"],
    ["Organic Chemistry I", "Advanced curriculum, higher tuition", "Higher completion rates compared to similar courses"],
    ["Computer Science", "Cutting-edge technology focus, renowned faculty", "Higher job placement rates compared to similar courses"],
    ["Principles of Microeconomics", "Comprehensive coverage, diverse faculty", "Similar average grades compared to similar courses"],
    ["English Composition I", "Strong emphasis on writing skills, innovative teaching methods", "Higher student satisfaction compared to similar courses"],
    ["Mathematics", "Rigorous curriculum, challenging assignments", "Similar dropout rates compared to similar courses"],
    ["Sociology", "Interactive learning environment, diverse perspectives", "Higher retention rates compared to similar courses"],
    ["Principles of Marketing", "Practical applications, industry connections", "Higher average salaries post-graduation compared to similar courses"],
    ["Physics", "Emphasis on problem-solving, research opportunities", "Similar student engagement levels compared to similar courses"],
    ["Spanish Language and Culture I", "Immersive learning experiences, study abroad opportunities", "Higher language proficiency outcomes compared to similar courses"],
    # Add more data rows here...
    ["Art and Design", "Extensive course material, renowned faculty", "Similar completion rates compared to similar courses"],
    ["Environmental Science", "Hands-on fieldwork opportunities, sustainability focus", "Higher student engagement levels compared to similar courses"],
    ["Political Science", "In-depth analysis, guest lectures", "Similar participation rates in extracurricular activities compared to similar courses"],
    ["French", "Interactive language labs, cultural immersion activities", "Higher average grades compared to similar courses"],
    ["Music", "Comprehensive music curriculum, performance opportunities", "Similar satisfaction rates among music majors compared to similar courses"],
    ["Anthropology", "Anthropological fieldwork, global perspective", "Higher employment rates in anthropology-related fields compared to similar courses"],
    ["Engineering", "Hands-on projects, industry partnerships", "Similar research output compared to similar courses"],
    ["Computer Networks", "Cutting-edge technology focus, networking opportunities", "Higher certification rates compared to similar courses"],
    ["Philosophy", "Critical thinking emphasis, philosophical debates", "Similar enrollment rates in advanced philosophy courses compared to similar courses"],
    ["Digital Marketing", "Industry-relevant curriculum, case study analysis", "Higher digital marketing campaign success rates compared to similar courses"],
]

prospective_student_demographics_data = [
    ["geographic_location", "age_range", "gender_distribution", "educational_background"]
]
# Generating 1000 rows of data for students
for _ in range(1000):
    geographic_location = random.choice(["Nairobi", "Mombasa", "Kisumu", "Eldoret", "Nakuru", "Malindi", "Kakamega", "Meru", "Thika", "Kitale"])
    age_range = random.choice(["18-20", "21-25", "26-30", "31-35", "36-40", "41-45", "46-50", "51-55", "56-60"])
    gender_distribution = random.choice(["Male", "Female"])
    educational_background = random.choice(["High School", "College", "University"])
    prospective_student_demographics_data.append([geographic_location, age_range, gender_distribution, educational_background])

    

# Write data to CSV file
#
# replace the data file & data array to write
file_data = [
        ('course_data', course_data),
        ('search_trends_data', search_trends_data),
        ('traffic_analysis_data', traffic_analysis_data),
        ('user_interactions_data', user_interactions_data),
        ('engagement_metrics_data', engagement_metrics_data),
        ('time_trends_data', time_trends_data),
        ('referral_sources_data', referral_sources_data),
        ('device_usage_data', device_usage_data),
        ('competitor_analysis_data', competitor_analysis_data),
        ('prospective_student_demographics_data', prospective_student_demographics_data)
        ]
#
for file_name, data in file_data:
    with open(f"data/{file_name}.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    print(f"Data has been exported to the {file_name} sucessfully")
