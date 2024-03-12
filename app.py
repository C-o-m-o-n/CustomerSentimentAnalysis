# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import csv

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

app = Flask(__name__)

# isLoggedIn = False
# List of valid credentials (username, password)
valid_credentials = [
    ("wesley", "K4nB%w"),
    ("collins", "Zb*4U&"),
    ("maurice", "M<!6by"),
    ("kevin", "NT:x6K"),
    ("hezbon", "bXE9*r")
]

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")  

@app.route("/")
def login_page():
    return render_template("login.html")
    
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if (username, password) in valid_credentials:
        # Redirect to home page after successful login
        return redirect(url_for("dashboard"))
    else:
        # Display error message for invalid credentials
        return render_template("login.html", error="Invalid username or password")
        
@app.route("/home")
def home():
    return render_template("home.html")  



course_data = []
with open('data/course_data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        course_data.append(row)

# Define route for course data page
@app.route('/course-data')
def function_course_data():
    return render_template('course_data.html', course_data=course_data)
    
@app.route('/search-trends')
def function_search_trends():
    # Read data from CSV file
    df = pd.read_csv('data/search_trends_data.csv')

    # Convert frequency_of_searches column to numeric
    df['frequency_of_searches'] = pd.to_numeric(df['frequency_of_searches'])

    # Create Horizontal Bar Chart
    plt.figure(figsize=(10, 6))
    plt.barh(df['most_searched_courses'], df['frequency_of_searches'], color='skyblue')
    plt.xlabel('Frequency of Searches')
    plt.ylabel('Course')
    plt.title('Frequency of Searches for Each Course')
    plt.tight_layout()
    plt.savefig('static/horizontal_bar_chart.png')

    # Create Word Cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['popular_search_terms']))
    wordcloud.to_file('static/wordcloud.png')

    return render_template('search_trends.html')    
    
@app.route('/traffic-analysis')
def function_traffic_analysis():
    # Read data from CSV file
    df = pd.read_csv('data/traffic_analysis_data.csv')

    # Extract data for charts
    courses = df['course']
    page_views = df['page_views']
    time_spent = df['time_spent'].apply(lambda x: float(x.split()[0]))
    bounce_rate = df['bounce_rate'].apply(lambda x: float(x.strip('%')))

    # Create Bar Chart for Page Views
    plt.figure(figsize=(10, 6))
    plt.bar(courses, page_views, color='skyblue')
    plt.xlabel('Course')
    plt.ylabel('Page Views')
    plt.title('Number of Page Views for Each Course')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('static/page_views_bar_chart.png')

    # Create Line Chart for Time Spent
    plt.figure(figsize=(10, 6))
    plt.plot(courses, time_spent, marker='o', color='green')
    plt.xlabel('Course')
    plt.ylabel('Time Spent (minutes)')
    plt.title('Time Spent on Each Course')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('static/time_spent_line_chart.png')

    # Create Pie Chart for Bounce Rate
    plt.figure(figsize=(10, 6))
    plt.pie(bounce_rate, labels=courses, autopct='%1.1f%%', startangle=140)
    plt.title('Bounce Rate for Each Course')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.savefig('static/bounce_rate_pie_chart.png')

    return render_template('traffic_analysis.html')
    
@app.route('/user-interactions')
def function_user_interactions():
    # Read data from CSV file
    df = pd.read_csv('data/user_interactions_data.csv')

    # Extract data for visualizations
    courses = df['course']
    click_through_rates = df['click_through_rates'].apply(lambda x: float(x.strip('%')))
    conversion_rates = df['conversion_rates'].apply(lambda x: float(x.strip('%')))
    feedback_and_comments = df['feedback_and_comments']

    # Create Horizontal Bar Chart for Click-through Rates and Conversion Rates
    plt.figure(figsize=(10, 6))
    plt.barh(courses, click_through_rates, color='skyblue', label='Click-through Rate')
    plt.barh(courses, conversion_rates, color='orange', left=click_through_rates, label='Conversion Rate')
    plt.xlabel('Rate (%)')
    plt.ylabel('Course')
    plt.title('Click-through Rates and Conversion Rates for Each Course')
    plt.legend()
    plt.tight_layout()
    plt.savefig('static/click_conversion_rates_bar_chart.png')

    # Create Word Cloud for Feedback and Comments
    wordcloud_text = ' '.join(feedback_and_comments)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(wordcloud_text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Feedback and Comments')
    plt.tight_layout()
    plt.savefig('static/feedback_comments_wordcloud.png')
    
    # Extract data for display
    course_feedback = df[['course', 'feedback_and_comments']].values.tolist()

    return render_template('user_interactions.html', course_feedback=course_feedback)

@app.route('/engagement-metrics')
def function_engagement_metrics():
    # Read data from CSV file
    df = pd.read_csv('data/engagement_metrics_data.csv')

    # Extract necessary columns for visualization
    courses = df['course']
    requests_for_more_info = df['requests_for_more_information'].astype(int)
    course_related_downloads = df['course_related_downloads'].astype(int)
    related_webinars_events = df['related_webinars_events'].astype(int)

    # Create Bar Chart for each engagement metric
    plt.figure(figsize=(10, 6))
    plt.bar(courses, requests_for_more_info, color='skyblue', label='Requests for More Information')
    plt.bar(courses, course_related_downloads, color='orange', label='Course-related Downloads', bottom=requests_for_more_info)
    plt.bar(courses, related_webinars_events, color='green', label='Related Webinars/Events', bottom=requests_for_more_info + course_related_downloads)
    plt.xlabel('Course')
    plt.ylabel('Count')
    plt.title('Engagement Metrics for Each Course')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig('static/engagement_metrics_bar_chart.png')

    # Create Stacked Bar Chart for total engagement breakdown by course
    plt.figure(figsize=(10, 6))
    plt.bar(courses, requests_for_more_info, color='skyblue', label='Requests for More Information')
    plt.bar(courses, course_related_downloads, color='orange', label='Course-related Downloads', bottom=requests_for_more_info)
    plt.bar(courses, related_webinars_events, color='green', label='Related Webinars/Events', bottom=requests_for_more_info + course_related_downloads)
    plt.xlabel('Course')
    plt.ylabel('Count')
    plt.title('Total Engagement Breakdown by Course')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig('static/total_engagement_stacked_bar_chart.png')

    return render_template('engagement_metrics.html')  

@app.route('/time-trends')
def function_time_trends():
    # Read data from CSV file
    df = pd.read_csv('data/time_trends_data.csv')

    # Extract necessary columns for visualization
    courses = df['course']
    change_in_popularity = df['change_in_popularity_over_time']
    seasonal_variation = df['seasonal_variation_in_interest']

    # Create Line Chart for change in popularity over time
    plt.figure(figsize=(10, 6))
    plt.plot(courses, change_in_popularity, marker='o', color='blue', linestyle='-', linewidth=2, label='Change in Popularity')
    plt.xlabel('Course')
    plt.ylabel('Popularity Trend')
    plt.title('Change in Popularity Over Time')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig('static/change_in_popularity_line_chart.png')

    # Create Step Chart for seasonal variation in interest
    plt.figure(figsize=(10, 6))
    plt.step(courses, seasonal_variation, where='mid', color='green', linestyle='-', linewidth=2, label='Seasonal Variation')
    plt.xlabel('Course')
    plt.ylabel('Interest Level')
    plt.title('Seasonal Variation in Interest')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig('static/seasonal_variation_step_chart.png')

    return render_template('time_trends.html')
    
@app.route('/referral-sources')
def function_referral_sources():
    # Read data from CSV file
    df = pd.read_csv('data/referral_sources_data.csv')

    # Extract necessary columns for visualization
    courses = df['course']
    where_visitors_are_coming_from = df['where_visitors_are_coming_from']
    marketing_channels_effectiveness = df['marketing_channels_effectiveness']

    # Create Vertical Bar Chart for where visitors are coming from
    plt.figure(figsize=(10, 6))
    plt.barh(courses, where_visitors_are_coming_from, color='skyblue')
    plt.xlabel('Referral Source')
    plt.ylabel('Course')
    plt.title('Where Visitors Are Coming From')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('static/where_visitors_bar_chart.png')

    # Create Grouped Bar Chart for marketing channels effectiveness
    plt.figure(figsize=(10, 6))
    index = range(len(courses))
    bar_width = 0.35
    plt.bar(index, marketing_channels_effectiveness, bar_width, label='High', color='skyblue')
    plt.bar([i + bar_width for i in index], marketing_channels_effectiveness, bar_width, label='Moderate', color='orange')
    plt.bar([i + 2*bar_width for i in index], marketing_channels_effectiveness, bar_width, label='Low', color='salmon')
    plt.xlabel('Course')
    plt.ylabel('Effectiveness')
    plt.title('Marketing Channels Effectiveness')
    plt.xticks([i + bar_width for i in index], courses, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig('static/marketing_channels_grouped_bar_chart.png')

    return render_template('referral_sources.html')
    
@app.route('/device-usage')
def function_device_usage():
    # Read data from CSV file
    df = pd.read_csv('data/device_usage_data.csv')

    # Extract necessary columns for visualization
    device_types = df['type_of_device']
    conversion_rates = df['conversion_rates'].str.rstrip('%').astype(float)

    # Create Horizontal Bar Chart
    plt.figure(figsize=(10, 6))
    plt.barh(device_types, conversion_rates, color='skyblue')
    plt.xlabel('Conversion Rates (%)')
    plt.ylabel('Device Types')
    plt.title('Device Usage Conversion Rates')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('static/device_usage_horizontal_bar_chart.png')

    return render_template('device_usage.html')    
    
@app.route('/competitor-analysis')
def function_competitor_analysis():
    # Read data from CSV file
    df = pd.read_csv('data/competitor_analysis_data.csv')

    # Extract necessary information for visualization
    courses = df['course']
    comparison_with_competitors = df['comparison_with_competitors']
    benchmarking_against_similar_courses = df['benchmarking_against_similar_courses']

    return render_template('competitor_analysis.html', 
                           courses=courses, 
                           comparison_with_competitors=comparison_with_competitors, 
                           benchmarking_against_similar_courses=benchmarking_against_similar_courses)
                           

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  
