from datetime import datetime

# In-memory storage for demonstration. Replace with a database in production.
plans = {
    "hourly_3mbps": {
        "name": "3Mbps Hourly",
        "speed_mbps": 3,
        "duration_hours": 1,
        "price": 20,
        "unlimited": False
    },
    "unlimited_24hr_5mbps": {
        "name": "5Mbps Unlimited 24hrs",
        "speed_mbps": 5,
        "duration_hours": 24,
        "price": 30,
        "unlimited": True
    },
    "unlimited_12hr_5mbps": {
        "name": "5Mbps Unlimited 12hrs",
        "speed_mbps": 5,
        "duration_hours": 12,
        "price": 40,
        "unlimited": True
    }
}

customers = {}

def add_plan(plan_id, plan_data):
    plans[plan_id] = plan_data

def delete_plan(plan_id):
    if plan_id in plans:
        del plans[plan_id]

def add_customer(customer_id, plan_id):
    if plan_id in plans:
        customers[customer_id] = {
            "plan_id": plan_id,
            "start_time": datetime.now(),
            "paid": False
        }

def get_customer(customer_id):
    return customers.get(customer_id)

def get_plan(plan_id):
    return plans.get(plan_id)

def get_all_plans():
    return plans

def get_all_customers():
    return customers