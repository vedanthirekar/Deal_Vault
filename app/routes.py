from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from . import db
from .models import User, Deal
from .forms import RegistrationForm, LoginForm, DealForm

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        from .models import UserProfile

        # Create user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        # Create corresponding user profile
        profile = UserProfile(
            user_id=user.user_id,
            dob=form.dob.data,
            gender=form.gender.data
        )
        db.session.add(profile)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', title='Register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/')
@main.route('/home')
def index():
    deals = Deal.query.order_by(Deal.deal_entered.desc()).all()
    return render_template('index.html', deals=deals)

from .models import Store, Category  # add this import

from .models import Store, Category, Deal

@main.route('/deals/new', methods=['GET', 'POST'])
@login_required
def new_deal():
    form = DealForm()
    form.category_id.choices = [(c.category_id, c.category_name) for c in Category.query.all()]

    if form.validate_on_submit():
        # Check if store already exists
        store = Store.query.filter_by(store_name=form.store_name.data.strip()).first()
        if not store:
            store = Store(store_name=form.store_name.data.strip())
            db.session.add(store)
            db.session.commit()

        deal = Deal(
            store_id=store.store_id,
            category_id=form.category_id.data,
            deal_desc=form.deal_desc.data,
            deal_amount=form.deal_amount.data,
            deal_validity=form.deal_validity.data,
            user_id=current_user.user_id
        )
        db.session.add(deal)
        db.session.commit()
        flash('Your deal has been posted!', 'success')
        return redirect(url_for('main.index'))

    return render_template('create_deal.html', title='New Deal', form=form, legend='New Deal')


@main.route('/deals')
def all_deals():
    store_query = request.args.get('store')
    category_query = request.args.get('category', type=int)
    desc_query = request.args.get('desc')
    sort = request.args.get('sort', 'latest')

    query = Deal.query

    if store_query:
        query = query.join(Store).filter(Store.store_name.ilike(f"%{store_query}%"))
    if category_query:
        query = query.filter_by(category_id=category_query)
    if desc_query:
        query = query.filter(Deal.deal_desc.ilike(f"%{desc_query}%"))

    if sort == 'popular':
        query = query.order_by(Deal.deal_likes.desc())
    else:
        query = query.order_by(Deal.deal_entered.desc())

    deals = query.all()
    categories = Category.query.all()
    return render_template('deals.html', deals=deals, categories=categories, store_query=store_query, category_query=category_query, desc_query=desc_query, sort=sort)


@main.route('/deals/<int:deal_id>')
def deal(deal_id):
    deal = Deal.query.get_or_404(deal_id)
    return render_template('deal.html', title=deal.deal_desc, deal=deal)
