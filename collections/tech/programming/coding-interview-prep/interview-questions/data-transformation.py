# Transform the user and customer data into the format specified output data format.

# **Input Data Formats**

#     Customers
#       - id: int           -- The customer's ID
#       - name: str         -- The customer's name
#       - created_at: str   -- The date on which the customer entry was created, an ISO string

#     Users
#       - username: str      -- The user's username
#       - customer_id: int   -- The ID of the customer to which the user belongs
#       - active: bool       -- Whether or not the user is active
#       - created_at: str    -- The date on which the user entry was created, an ISO string

# **Output Data Format**

# ```
# [
#     {
#         "customer_name": str,        # The name of the customer
#         "active_user_count": int,    # The number of active users
#         "inactive_user_count": int,  # The number of inactive users
#         "active_users": list[str],   # A list of usernames for active users
#         "inactive_users": list[str], # A list of usernames for inactive users
#         "newest_user": str,          # The username of the most recently created user
#         "created_at": str,           # The date on which the customer entry was created
#     }, ...
# ]
# ```

# Your results should be dumped as raw JSON to the console!
import json
from datetime import datetime

def get_all_customers():
    return [
        (1, "Custom Inks Inc", "2023-01-01"),
        (2, "Hog Heaven Oinc", "2023-02-01"),
        (3, "LL Beam LLC", "2023-03-01"),
        (4, "Weesnaw's Paddywagons", "2024-01-01"),
    ]

def get_all_users():
    return [
        ("dan@custominc.com", 1, True, "2023-01-02"),
        ("john@custominc.com", 1, False, "2023-01-03"),
        ("hog.roger@hoghevvin.com", 2, True, "2023-02-01"),
        ("hog.mike@hoghevvin.com", 2, True, "2023-02-05"),
        ("hog.june@hoghevvin.com", 2, True, "2023-02-21"),
        ("hog.melissa@hoghevvin.com", 2, True, "2023-02-25"),
        ("donald@llbeam.org", 3, False, "2023-03-16"),
        ("jen@llbeam.org", 3, False, "2023-03-17"),
        ("tami@llbeam.org", 3, False, "2023-03-19"),
        ("rufus@weesnawz.gov", 4, True, "2023-01-17"),
        ("stumpy@weesnawz.gov", 4, False, "2023-01-16"),
    ]

def initialize_customer_dict(customers: list[tuple]):
    return {
        cust[0] : {
            "name": cust[1],
            "created_at": cust[2], 
            "active_users": [], 
            "inactive_users": [], 
            "newest_user": None, 
            "newest_user_date": None
        }
    for cust in customers}

def process_users(users: list[tuple], customer_dict: dict):
    for username, customer_id, active, created_at in users:
        user_data = (username, created_at)
        if active:
            customer_dict[customer_id]["active_users"].append(username)
        else:
            customer_dict[customer_id]["inactive_users"].append(username)

        # Update the newest user if this user is newer
        if (customer_dict[customer_id]["newest_user_date"] is None or 
            datetime.fromisoformat(created_at) > customer_dict[customer_id]["newest_user_date"]):
            customer_dict[customer_id]["newest_user"] = username
            customer_dict[customer_id]["newest_user_date"] = datetime.fromisoformat(created_at)

def create_output_data(customer_dict):
    output_data = []
    for customer_id, customer_data in customer_dict.items():
        output_data.append({
            "customer_name": customer_data["name"],
            "active_user_count": len(customer_data["active_users"]),
            "inactive_user_count": len(customer_data["inactive_users"]),
            "active_users": customer_data["active_users"],
            "inactive_users": customer_data["inactive_users"],
            "newest_user": customer_data["newest_user"],
            "created_at": customer_data["created_at"]
        })
    return output_data

def transform_data(customers, users):
    customer_dict = initialize_customer_dict(customers)
    process_users(users, customer_dict)
    return create_output_data(customer_dict)

if __name__ == "__main__":
    customers = get_all_customers()
    users = get_all_users()
    transformed_data = transform_data(customers, users)
    print(json.dumps(transformed_data, indent=4))