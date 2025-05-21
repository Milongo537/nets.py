from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    speed_mbps = db.Column(db.Float, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    duration_hours = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Plan {self.id}: {self.speed_mbps} Mbps, {self.rate} Shillings, {self.duration_hours} hours>'


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)
    total_bill = db.Column(db.Float, default=0.0)

    plan = db.relationship('Plan', backref='customers')

    def __repr__(self):
        return f'<Customer {self.id}: {self.name}, Plan ID: {self.plan_id}, Total Bill: {self.total_bill}>'