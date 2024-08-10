import random

diet_tips = [
    "Eat a healthy diet rich in fruits, vegetables, whole grains, and lean proteins.",
    "Exercise regularly to maintain a healthy weight and improve cardiovascular health.",
    "Eat more vegetables, since old age is associated with risk of heart failure",
    "Limit alcohol consumption to moderate levels.",
    "Manage stress through relaxation techniques such as meditation or yoga.",
    "Monitor and control high blood pressure, cholesterol levels, and diabetes.",
    "Get regular check-ups and screenings for heart health.",
    "Maintain a healthy weight and avoid obesity.",
    "Limit intake of saturated fats, trans fats, cholesterol, and sodium.",
    "Stay hydrated by drinking plenty of water throughout the day.",
]

exercise_tips = [
    "Take a 30-minute brisk walk every day to improve cardiovascular health.",
    "Engage in strength training exercises like push-ups and squats to build muscle mass and bone density.",
    "Join a fitness class or sports team to make exercise more enjoyable and social.",
    "Incorporate activities like cycling, swimming, or dancing into your weekly routine for variety.",
    "Use stairs instead of elevators whenever possible to increase daily physical activity.",
    "Set achievable fitness goals and track your progress to stay motivated and accountable.",
    "Take breaks from sitting every hour to stretch or walk around to reduce sedentary behavior.",
    "Include balance and flexibility exercises like yoga or tai chi to improve agility and prevent injuries.",
    "Find outdoor activities you enjoy, such as hiking or gardening, to stay active while enjoying nature.",
    "Stay consistent with your exercise routine by scheduling workouts at the same time each day.",
]


stress_management_tips = [
    "Practice deep breathing exercises to calm your mind and body.",
    "Meditate for a few minutes each day to reduce stress and promote relaxation.",
    "Engage in regular physical activity, such as walking, yoga, or swimming, to release tension and improve mood.",
    "Connect with nature by spending time outdoors or bringing plants into your living space.",
    "Maintain a healthy sleep routine by going to bed and waking up at consistent times each day.",
    "Spend time with loved ones and engage in meaningful social activities to foster a sense of connection and support.",
    "Limit exposure to stressful situations and learn to say no when necessary to protect your mental health.",
    "Practice mindfulness by focusing on the present moment and accepting thoughts and feelings without judgment.",
    "Engage in hobbies and activities that bring you joy and relaxation, such as reading, gardening, or listening to music.",
    "Seek professional help from a therapist or counselor if you're struggling to manage stress on your own.",
]


def diet_recommendations():
    return 

def exercise_recommendations(): 
    return random.choice(exercise_tips)

def stress_management_recommendations():
    return random.choice(stress_management_tips)    


def get_recommendation(form_values):
    # Check if blood pressure is at critical levels
    if int(form_values.get("trestbps")) > 125:
        return "Your blood pressure is beyond critical levels and you need to visit a healthcare facility as soon as possible."

    # Determine personalized recommendations based on form entries
    recommendations = []

    # Age-specific diet recommendation
    age = int(form_values.get("age"))
    if age > 12:
        diet_recommendation = f"For your age {age}, {diet_tips[2]}"
    else:
        diet_recommendation = random.choice(diet_tips)
    recommendations.append(diet_recommendation)

    # Randomly select exercise recommendation
    exercise_recommendation = exercise_recommendations()  # Corrected function call
    recommendations.append(exercise_recommendation)

    # Randomly select stress management recommendation
    stress_management_recommendation = random.choice(stress_management_tips)
    recommendations.append(stress_management_recommendation)

    # Convert recommendations list to a string separated by colons
    recommendations_str = ":".join(recommendations)
    
    return recommendations_str
