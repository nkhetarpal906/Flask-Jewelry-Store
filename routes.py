import os
from flask import render_template, redirect, url_for, flash, request, current_app
from app import app, db, login_manager
from models import User, Product, Order
from forms import RegistrationForm, LoginForm, ProductForm
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from email_service import send_order_confirmation, send_order_notification_to_admin
from functools import wraps

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    # Retrieve a few products for the animated gallery (e.g., best-sellers)
    products = Product.query.limit(5).all()
    return render_template('index.html', products=products)

@app.route('/shop')
def shop():
    category = request.args.get('category')
    sort_by = request.args.get('sort_by')
    query = Product.query
    if category:
        query = query.filter_by(category=category)
    if sort_by == 'price_asc':
        query = query.order_by(Product.price.asc())
    elif sort_by == 'price_desc':
        query = query.order_by(Product.price.desc())
    elif sort_by == 'new':
        query = query.order_by(Product.id.desc())  # Assuming higher ID = new product
    products = query.all()
    return render_template('shop.html', products=products)

@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        if not current_user.is_authenticated:
            flash('Please login to place an order', 'warning')
            return redirect(url_for('login'))
        quantity = int(request.form.get('quantity', 1))
        if product.stock < quantity:
            flash('Not enough stock available', 'danger')
            return redirect(url_for('product_detail', product_id=product.id))
        # Deduct stock and create order
        product.stock -= quantity
        order = Order(user_id=current_user.id, product_id=product.id, quantity=quantity)
        db.session.add(order)
        db.session.commit()
        # Send emails
        send_order_confirmation(current_user, order)
        send_order_notification_to_admin(app.config.get('ADMIN_EMAIL'), current_user, order)
        flash('Order placed successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('product_detail.html', product=product)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check for existing user by username or email
        existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
        if existing_user:
            flash('User with that username or email already exists', 'danger')
            return redirect(url_for('register'))
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', orders=orders)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# --- Admin Routes ---

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('Admin access required', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/admin')
@admin_required
def admin_dashboard():
    products = Product.query.all()
    orders = Order.query.all()
    return render_template('admin_dashboard.html', products=products, orders=orders)

@app.route('/admin/add_product', methods=['GET', 'POST'])
@admin_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        # Process the uploaded image file
        image_file = form.image.data
        filename = secure_filename(image_file.filename)
        # Save the file to the UPLOAD_FOLDER configured in app.config
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Build relative path for database (relative to static folder)
        relative_path = "images/" + filename

        new_product = Product(
            name=form.name.data,
            price=form.price.data,
            description=form.description.data,
            category=form.category.data,
            stock=form.stock.data,
            image=relative_path
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('add_product.html', form=form)

@app.route('/admin/edit_product/<int:product_id>', methods=['GET', 'POST'])
@admin_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.description = form.description.data
        product.category = form.category.data
        product.stock = form.stock.data
        # If a new image is uploaded, update the file
        if form.image.data:
            image_file = form.image.data
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            product.image = "images/" + filename
        db.session.commit()
        flash('Product updated successfully', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('edit_product.html', form=form, product=product)

@app.route('/admin/delete_product/<int:product_id>', methods=['POST'])
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/mark_delivered/<int:order_id>', methods=['POST'])
@admin_required
def mark_delivered(order_id):
    order = Order.query.get_or_404(order_id)
    order.order_status = "Delivered"
    db.session.commit()
    flash("Order marked as delivered", "success")
    return redirect(url_for('admin_dashboard'))
