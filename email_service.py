from flask_mail import Message
from flask import current_app

def send_order_confirmation(user, order):
    mail = current_app.extensions.get('mail')
    msg = Message(
        'Order Confirmation - Pearl Box',
        recipients=[user.email],
        body=f'''Dear {user.username},

Thank you for your order!

Order ID: {order.id}
Product: {order.product.name}
Quantity: {order.quantity}
Order Date: {order.order_date.strftime("%Y-%m-%d %H:%M:%S")}

We will notify you once your order is shipped.

Best regards,
Pearl Box Team
'''
    )
    mail.send(msg)

def send_order_notification_to_admin(admin_email, user, order):
    mail = current_app.extensions.get('mail')
    msg = Message(
        'New Order Received - Pearl Box',
        recipients=[admin_email],
        body=f'''Hello Admin,

A new order has been placed.

Order ID: {order.id}
User: {user.username} ({user.email})
Product: {order.product.name}
Quantity: {order.quantity}
Order Date: {order.order_date.strftime("%Y-%m-%d %H:%M:%S")}

Please process this order accordingly.

Best regards,
Pearl Box Website
'''
    )
    mail.send(msg)
