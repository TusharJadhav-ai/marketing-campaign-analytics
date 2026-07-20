"""
Business Rules
--------------
Defines all business assumptions used to generate
realistic marketing campaign data.

Project:
Marketing Campaign Analytics
"""

# ==========================================================
# Campaign Types
# ==========================================================

CAMPAIGN_TYPES = {

    "Summer Sale": "Seasonal",
    "Winter Sale": "Seasonal",
    "Back to School": "Seasonal",

    "Black Friday": "Promotional",
    "Flash Sale": "Promotional",
    "Weekend Special": "Promotional",

    "Diwali Bonanza": "Festival",
    "New Year Blast": "Festival",
    "Festive Combo": "Festival",

    "Mega Clearance": "Clearance"
}

# ==========================================================
# Channel Weights
# ==========================================================

CHANNEL_WEIGHTS = {

    "Summer Sale": {
        "Instagram": 30,
        "Facebook": 25,
        "Google Search": 20,
        "YouTube": 15,
        "Email": 5,
        "LinkedIn": 5
    },

    "Winter Sale": {
        "Instagram": 25,
        "Facebook": 25,
        "Google Search": 25,
        "YouTube": 15,
        "Email": 5,
        "LinkedIn": 5
    },

    "Black Friday": {
        "Google Search": 30,
        "Facebook": 25,
        "Instagram": 20,
        "Email": 15,
        "YouTube": 7,
        "LinkedIn": 3
    },

    "Flash Sale": {
        "Google Search": 30,
        "Facebook": 25,
        "Instagram": 20,
        "Email": 10,
        "YouTube": 10,
        "LinkedIn": 5
    },

    "Weekend Special": {
        "Facebook": 30,
        "Instagram": 30,
        "Google Search": 20,
        "YouTube": 10,
        "Email": 5,
        "LinkedIn": 5
    },

    "Diwali Bonanza": {
        "Facebook": 30,
        "Instagram": 25,
        "Google Search": 20,
        "YouTube": 15,
        "Email": 5,
        "LinkedIn": 5
    },

    "New Year Blast": {
        "Facebook": 25,
        "Instagram": 25,
        "Google Search": 20,
        "YouTube": 15,
        "Email": 10,
        "LinkedIn": 5
    },

    "Festive Combo": {
        "Facebook": 30,
        "Instagram": 25,
        "Google Search": 20,
        "YouTube": 15,
        "Email": 5,
        "LinkedIn": 5
    },

    "Back to School": {
        "Facebook": 30,
        "Instagram": 25,
        "Google Search": 20,
        "YouTube": 15,
        "Email": 5,
        "LinkedIn": 5
    },

    "Mega Clearance": {
        "Google Search": 35,
        "Facebook": 25,
        "Instagram": 15,
        "Email": 15,
        "YouTube": 5,
        "LinkedIn": 5
    }

}

# ==========================================================
# Device Distribution
# ==========================================================

DEVICE_WEIGHTS = {

    "Instagram": {
        "Mobile": 85,
        "Desktop": 15
    },

    "Facebook": {
        "Mobile": 80,
        "Desktop": 20
    },

    "YouTube": {
        "Mobile": 75,
        "Desktop": 25
    },

    "Google Search": {
        "Mobile": 60,
        "Desktop": 40
    },

    "LinkedIn": {
        "Mobile": 45,
        "Desktop": 55
    },

    "Email": {
        "Mobile": 35,
        "Desktop": 65
    }

}

# ==========================================================
# Customer Segment Distribution
# ==========================================================

CUSTOMER_SEGMENT_WEIGHTS = {

    "Facebook": {
        "New": 40,
        "Returning": 30,
        "Premium": 20,
        "Loyal": 10
    },

    "Instagram": {
        "New": 45,
        "Premium": 25,
        "Returning": 20,
        "Loyal": 10
    },

    "Google Search": {
        "New": 35,
        "Returning": 35,
        "Premium": 20,
        "Loyal": 10
    },

    "LinkedIn": {
        "Premium": 45,
        "Loyal": 35,
        "Returning": 15,
        "New": 5
    },

    "Email": {
        "Loyal": 50,
        "Returning": 30,
        "Premium": 15,
        "New": 5
    },

    "YouTube": {
        "New": 40,
        "Returning": 30,
        "Premium": 20,
        "Loyal": 10
    }

}