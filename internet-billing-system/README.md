# Internet Billing System

This project is an Internet Billing System built with Flask that allows users to manage internet plans and customers, and integrates with M-Pesa for payment processing.

## Features

- Add and delete internet plans
- Customer dashboard to view current plans and billing information
- Payment processing through M-Pesa
- User-friendly interface for managing plans and payments

## Project Structure

```
internet-billing-system
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── mpesa.py
│   ├── templates
│   │   ├── base.html
│   │   ├── add_plan.html
│   │   ├── delete_plan.html
│   │   ├── customer_dashboard.html
│   │   └── payment.html
│   └── static
│       └── style.css
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd internet-billing-system
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Configure the application:
   - Update the `config.py` file with your database settings and M-Pesa credentials.

## Usage

1. Run the application:
   ```
   python run.py
   ```

2. Access the application in your web browser at `http://127.0.0.1:5000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.