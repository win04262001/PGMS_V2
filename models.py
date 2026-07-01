import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bid(db.Model):
    __tablename__ = 'bids'

    id = db.Column(db.Integer, primary_key=True)
    date_monitored = db.Column(db.Date, nullable=True)
    reference_number = db.Column(db.String(64), unique=True, nullable=False)
    system_type = db.Column(db.String(64), nullable=False, default='Philgeps')
    control_number = db.Column(db.String(128), nullable=True)
    delivery_location = db.Column(db.String(255), nullable=True)
    contact_person = db.Column(db.String(128), nullable=True)
    procurement_mode = db.Column(db.String(128), nullable=True)
    date_created = db.Column(db.DateTime, nullable=True)
    procuring_entity = db.Column(db.String(255), nullable=True)
    project_title = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(128), nullable=True)
    region = db.Column(db.String(128), nullable=True)
    province = db.Column(db.String(128), nullable=True)
    abc_value = db.Column(db.Float, nullable=True)
    closing_date = db.Column(db.Date, nullable=True)
    closing_time = db.Column(db.String(16), nullable=True)
    days_remaining = db.Column(db.Integer, nullable=True)
    priority_level = db.Column(db.String(64), nullable=True)
    status = db.Column(db.String(128), nullable=True)
    canvassing_status = db.Column(db.String(128), nullable=True)
    remarks = db.Column(db.Text, nullable=True)
    date_submitted = db.Column(db.Date, nullable=True)
    date_added = db.Column(db.Date, default=datetime.date.today, nullable=False)
    bid_amount = db.Column(db.Float, nullable=True)
    result = db.Column(db.String(128), nullable=True)
    opportunity_score = db.Column(db.Integer, nullable=True)
    abc_flag = db.Column(db.String(64), nullable=True)
    recommendation = db.Column(db.String(128), nullable=True)
    attachments = db.Column(db.String(2048), nullable=True)
    rfq_source = db.Column(db.String(32), nullable=True, default='online')  # 'online' or 'walk-in'
    pr_number = db.Column(db.String(64), nullable=True)  # For walk-in RFQs
    office_department = db.Column(db.String(255), nullable=True)
    supplier_name = db.Column(db.String(255), nullable=True)
    company_address = db.Column(db.Text, nullable=True)
    contact_email = db.Column(db.String(255), nullable=True)
    contact_phone = db.Column(db.String(32), nullable=True)

    def __repr__(self):
        return f'<Bid {self.reference_number}>'


class BidAttachment(db.Model):
    __tablename__ = 'bid_attachments'

    id = db.Column(db.Integer, primary_key=True)
    bid_id = db.Column(db.Integer, db.ForeignKey('bids.id'), nullable=False)
    filename = db.Column(db.String(1024), nullable=False)
    original_filename = db.Column(db.String(1024), nullable=False)
    attachment_type = db.Column(db.String(64), nullable=True)  # 'scanned_rfq', 'quotation', etc.
    upload_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    file_size = db.Column(db.Integer, nullable=True)
    file_path = db.Column(db.String(2048), nullable=True)

    def __repr__(self):
        return f'<BidAttachment {self.original_filename}>'


class RequirementDocument(db.Model):
    __tablename__ = 'requirements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    filename = db.Column(db.String(1024), nullable=False, unique=True)
    original_filename = db.Column(db.String(1024), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<RequirementDocument {self.title}>'


class PreDocument(db.Model):
    __tablename__ = 'pre_documents'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    supplier_name = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    filename = db.Column(db.String(1024), nullable=False, unique=True)
    original_filename = db.Column(db.String(1024), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<PreDocument {self.title}>'


class LoginLog(db.Model):
    __tablename__ = 'login_logs'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    action = db.Column(db.String(32), nullable=False)
    ip_address = db.Column(db.String(64), nullable=True)
    user_agent = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<LoginLog {self.username} {self.action} {self.timestamp}>'
