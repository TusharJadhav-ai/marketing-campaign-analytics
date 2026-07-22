"""
Marketing Performance Rules
---------------------------
Defines realistic digital marketing performance metrics
for each marketing channel.
Version: 1.0
"""

CHANNEL_METRICS = {

    "Google Search": {
        "CTR": (4.0, 7.0),
        "CPC": (20, 60)
    },

    "Facebook": {
        "CTR": (1.5, 3.0),
        "CPC": (8, 25)
    },

    "Instagram": {
        "CTR": (1.2, 2.8),
        "CPC": (10, 30)
    },

    "YouTube": {
        "CTR": (0.8, 2.0),
        "CPC": (4, 15)
    },

    "LinkedIn": {
        "CTR": (2.0, 5.0),
        "CPC": (60, 150)
    },

    "Email": {
        "CTR": (5.0, 12.0),
        "CPC": (1, 5)
    }

}

CAMPAIGN_BUDGET_RANGES = {

    "Seasonal": (30000, 70000),

    "Promotional": (20000, 50000),

    "Festival": (60000, 150000),

    "Clearance": (10000, 30000)

}