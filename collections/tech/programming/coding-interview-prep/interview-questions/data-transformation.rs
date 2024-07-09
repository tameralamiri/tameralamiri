use chrono::NaiveDate;
use serde::{Serialize, Deserialize};
use std::collections::HashMap;


#[derive(Debug, Serialize, Deserialize)]
struct Customer {
    id: u32,
    name: String,
    created_at: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct User {
    username: String,
    customer_id: u32,
    active: bool,
    created_at: String,
}

#[derive(Debug, Serialize)]
struct OutputData {
    customer_name: String,
    active_user_count: usize,
    inactive_user_count: usize,
    active_users: Vec<String>,
    inactive_users: Vec<String>,
    newest_user: String,
    created_at: String,
}

// Simulating the API responses
fn get_all_customers() -> Vec<(u32, String, String)> {
    vec![
        (1, "Custom Inks Inc".to_string(), "2023-01-01".to_string()),
        (2, "Hog Heaven Oinc".to_string(), "2023-02-01".to_string()),
        (3, "LL Beam LLC".to_string(), "2023-03-01".to_string()),
        (4, "Weesnaw's Paddywagons".to_string(), "2024-01-01".to_string()),
    ]
}

fn get_all_users() -> Vec<(String, u32, bool, String)> {
    vec![
        ("dan@custominc.com".to_string(), 1, true, "2023-01-02".to_string()),
        ("john@custominc.com".to_string(), 1, false, "2023-01-03".to_string()),
        ("hog.roger@hoghevvin.com".to_string(), 2, true, "2023-02-01".to_string()),
        ("hog.mike@hoghevvin.com".to_string(), 2, true, "2023-02-05".to_string()),
        ("hog.june@hoghevvin.com".to_string(), 2, true, "2023-02-21".to_string()),
        ("hog.melissa@hoghevvin.com".to_string(), 2, true, "2023-02-25".to_string()),
        ("donald@llbeam.org".to_string(), 3, false, "2023-03-16".to_string()),
        ("jen@llbeam.org".to_string(), 3, false, "2023-03-17".to_string()),
        ("tami@llbeam.org".to_string(), 3, false, "2023-03-19".to_string()),
        ("rufus@weesnawz.gov".to_string(), 4, true, "2023-01-17".to_string()),
        ("stumpy@weesnawz.gov".to_string(), 4, false, "2023-01-16".to_string()),
    ]
}

// Convert tuple to Customer struct
fn parse_customers(customer_tuples: Vec<(u32, String, String)>) -> Vec<Customer> {
    customer_tuples.into_iter().map(|(id, name, created_at)| Customer {
        id,
        name,
        created_at,
    }).collect()
}

// Convert tuple to User struct
fn parse_users(user_tuples: Vec<(String, u32, bool, String)>) -> Vec<User> {
    user_tuples.into_iter().map(|(username, customer_id, active, created_at)| User {
        username,
        customer_id,
        active,
        created_at,
    }).collect()
}

fn initialize_customer_data(customers: Vec<Customer>) -> HashMap<u32, (String, String, Vec<String>, Vec<String>, Option<String>, Option<NaiveDate>)> {
    let mut customer_dict = HashMap::new();
    for customer in customers {
        customer_dict.insert(
            customer.id,
            (
                customer.name,
                customer.created_at,
                vec![],
                vec![],
                None,
                None,
            ),
        );
    }
    customer_dict
}

fn process_users(users: Vec<User>, customer_dict: &mut HashMap<u32, (String, String, Vec<String>, Vec<String>, Option<String>, Option<NaiveDate>)>) {
    for user in users {
        let user_created_at = NaiveDate::parse_from_str(&user.created_at, "%Y-%m-%d").unwrap();
        let customer_data = customer_dict.get_mut(&user.customer_id).unwrap();
        if user.active {
            customer_data.2.push(user.username.clone());
        } else {
            customer_data.3.push(user.username.clone());
        }

        if customer_data.5.is_none() || user_created_at > customer_data.5.unwrap() {
            customer_data.4 = Some(user.username);
            customer_data.5 = Some(user_created_at);
        }
    }
}

fn create_output_data(customer_dict: HashMap<u32, (String, String, Vec<String>, Vec<String>, Option<String>, Option<NaiveDate>)>) -> Vec<OutputData> {
    let mut output_data = vec![];
    for (_customer_id, customer_data) in customer_dict {
        output_data.push(OutputData {
            customer_name: customer_data.0,
            active_user_count: customer_data.2.len(),
            inactive_user_count: customer_data.3.len(),
            active_users: customer_data.2,
            inactive_users: customer_data.3,
            newest_user: customer_data.4.unwrap(),
            created_at: customer_data.1,
        });
    }
    output_data
}

fn main() {
    // Simulate fetching data from API
    let customer_tuples = get_all_customers();
    let user_tuples = get_all_users();

    // Parse tuples into structs
    let customers = parse_customers(customer_tuples);
    let users = parse_users(user_tuples);

    // Transform data
    let mut customer_dict = initialize_customer_data(customers);
    process_users(users, &mut customer_dict);
    let output_data = create_output_data(customer_dict);

    // Print output as JSON
    println!("{}", serde_json::to_string_pretty(&output_data).unwrap());
}
