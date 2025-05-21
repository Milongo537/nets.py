from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Plan, Customer
from . import db

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('base.html')

@routes.route('/add_plan', methods=['GET', 'POST'])
def add_plan():
    if request.method == 'POST':
        plan_name = request.form['plan_name']
        speed = request.form['speed']
        rate = request.form['rate']
        
        new_plan = Plan(name=plan_name, speed=speed, rate=rate)
        db.session.add(new_plan)
        db.session.commit()
        flash('Plan added successfully!', 'success')
        return redirect(url_for('routes.home'))
    
    return render_template('add_plan.html')

@routes.route('/delete_plan/<int:plan_id>', methods=['POST'])
def delete_plan(plan_id):
    plan = Plan.query.get(plan_id)
    if plan:
        db.session.delete(plan)
        db.session.commit()
        flash('Plan deleted successfully!', 'success')
    else:
        flash('Plan not found!', 'danger')
    return redirect(url_for('routes.home'))

@routes.route('/customer_dashboard')
def customer_dashboard():
    customers = Customer.query.all()
    return render_template('customer_dashboard.html', customers=customers)

@routes.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        # Handle payment processing logic here
        pass
    return render_template('payment.html')