from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import (
    plans, customers, add_plan, delete_plan, add_customer,
    get_customer, get_plan, get_all_plans, get_all_customers
)

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('customer_dashboard.html', plans=get_all_plans(), customers=get_all_customers())

# Admin: Add a new plan
@main.route('/admin/add_plan', methods=['GET', 'POST'])
def admin_add_plan():
    if request.method == 'POST':
        plan_id = request.form['plan_id']
        name = request.form['name']
        speed_mbps = int(request.form['speed_mbps'])
        duration_hours = int(request.form['duration_hours'])
        price = int(request.form['price'])
        unlimited = 'unlimited' in request.form

        add_plan(plan_id, {
            "name": name,
            "speed_mbps": speed_mbps,
            "duration_hours": duration_hours,
            "price": price,
            "unlimited": unlimited
        })
        flash('Plan added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_plan.html')

# Admin: Delete a plan
@main.route('/admin/delete_plan/<plan_id>', methods=['POST'])
def admin_delete_plan(plan_id):
    delete_plan(plan_id)
    flash('Plan deleted successfully!', 'success')
    return redirect(url_for('main.index'))

# Customer: Select a plan
@main.route('/customer/select_plan', methods=['POST'])
def customer_select_plan():
    customer_id = request.form['customer_id']
    plan_id = request.form['plan_id']
    add_customer(customer_id, plan_id)
    flash('Plan selected! Please proceed to payment.', 'info')
    return redirect(url_for('main.customer_payment', customer_id=customer_id))

# Customer: Payment page (dummy, integrate with mpesa.py)
@main.route('/customer/payment/<customer_id>', methods=['GET', 'POST'])
def customer_payment(customer_id):
    customer = get_customer(customer_id)
    if not customer:
        flash('Customer not found.', 'danger')
        return redirect(url_for('main.index'))
    plan = get_plan(customer['plan_id'])
    if request.method == 'POST':
        # Here, integrate with mpesa.py for real payment
        customer['paid'] = True
        flash('Payment successful! Enjoy your internet.', 'success')
        return redirect(url_for('main.index'))
    return render_template('payment.html', customer=customer, plan=plan)