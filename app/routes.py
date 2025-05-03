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

@main.route('/like/<int:deal_id>', methods=['POST'])
@login_required
def toggle_like(deal_id):
    deal = Deal.query.get_or_404(deal_id)
    if current_user.has_liked(deal):
        current_user.unlike_deal(deal)
    else:
        current_user.like_deal(deal)
    return redirect(request.referrer or url_for('main.index'))

@main.route('/profile')
@login_required
def profile():
    posted_deals = Deal.query.filter_by(user_id=current_user.user_id).order_by(Deal.deal_entered.desc()).all()
    liked_deals = [like.deal for like in current_user.liked_deals]

    return render_template('profile.html', posted_deals=posted_deals, liked_deals=liked_deals)

@main.route('/deals/<int:deal_id>/update', methods=['GET', 'POST'])
@login_required
def update_deal(deal_id):
    deal = Deal.query.get_or_404(deal_id)
    if deal.author != current_user:
        abort(403)

    form = DealForm()
    form.category_id.choices = [(c.category_id, c.category_name) for c in Category.query.all()]
    if form.validate_on_submit():
        store = Store.query.filter_by(store_name=form.store_name.data.strip()).first()
        if not store:
            store = Store(store_name=form.store_name.data.strip())
            db.session.add(store)
            db.session.commit()

        deal.store_id = store.store_id
        deal.category_id = form.category_id.data
        deal.deal_desc = form.deal_desc.data
        deal.deal_amount = form.deal_amount.data
        deal.deal_validity = form.deal_validity.data
        db.session.commit()
        flash('Deal updated successfully!', 'success')
        return redirect(url_for('main.profile'))

    elif request.method == 'GET':
        form.store_name.data = deal.store.store_name
        form.category_id.data = deal.category_id
        form.deal_desc.data = deal.deal_desc
        form.deal_amount.data = deal.deal_amount
        form.deal_validity.data = deal.deal_validity

    return render_template('create_deal.html', title='Update Deal', form=form, legend='Update Deal')


@main.route('/deals/<int:deal_id>/delete', methods=['POST'])
@login_required
def delete_deal(deal_id):
    deal = Deal.query.get_or_404(deal_id)
    if deal.author != current_user:
        abort(403)
    db.session.delete(deal)
    db.session.commit()
    flash('Deal deleted successfully!', 'info')
    return redirect(url_for('main.profile'))

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from . import db
from .models import User, Deal, Store, Category
from .forms import RegistrationForm, LoginForm, DealForm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify
from io import BytesIO
import base64
import numpy as np



@main.route("/visualizations")
@login_required
def visualizations():
    sns.set_theme(style="whitegrid", palette="YlGnBu")
    plt.rcParams.update({'font.size': 12})

    deals = db.session.query(Deal, User, Store, Category).\
        join(User, Deal.user_id == User.user_id).\
        join(Store, Deal.store_id == Store.store_id).\
        join(Category, Deal.category_id == Category.category_id).all()

    df = pd.DataFrame([{
        'category': c.category_name,
        'store': s.store_name,
        'user': u.username,
        'amount': d.deal_amount,
        'likes': len(d.likes),
        'desc': d.deal_desc,
        'date': d.deal_entered
    } for d, u, s, c in deals])
    df.dropna(inplace=True)

    plots = []

    def fig_to_base64(fig):
        buf = BytesIO()
        fig.tight_layout()
        fig.savefig(buf, format="png")
        buf.seek(0)
        return base64.b64encode(buf.read()).decode()

    # Define a consistent palette
    palette = sns.color_palette("YlGnBu", as_cmap=False)

    # 1. Pie Chart: Deals per Category
    fig1, ax1 = plt.subplots(figsize=(6, 6))
    category_counts = df['category'].value_counts()
    explode = [0.05] * len(category_counts)
    ax1.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%',
            startangle=140, explode=explode, colors=palette[:len(category_counts)], shadow=False)
    ax1.axis('equal')
    plt.title("Deals per Category")
    plots.append(fig_to_base64(fig1))

    # 2. Line Plot: Deals Over Time
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    df['date'] = pd.to_datetime(df['date'])
    daily_counts = df.groupby(df['date'].dt.date).size()
    ax2.plot(daily_counts.index, daily_counts.values, marker='o', color=palette[3])
    ax2.set_title("Deals Over Time")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Number of Deals")
    ax2.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(rotation=30)
    plots.append(fig_to_base64(fig2))

    # 3. Bar Plot: Top Users by Deal Posts
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    user_counts = df['user'].value_counts().head(5)
    bars = sns.barplot(x=user_counts.values, y=user_counts.index, ax=ax3, palette=palette[:len(user_counts)])
    for i, v in enumerate(user_counts.values):
        ax3.text(v + 0.5, i, str(v), color='black', va='center')
    ax3.set_title("Top Users by Deal Posts")
    plots.append(fig_to_base64(fig3))

    # 4. Treemap: Top Stores by Deal Count
    store_counts = df['store'].value_counts().head(5)
    fig4 = plt.figure(figsize=(8, 4))
    squarify.plot(sizes=store_counts.values, label=store_counts.index, alpha=0.9, color=palette[:len(store_counts)])
    plt.title("Top Stores by Deal Count")
    plt.axis('off')
    plots.append(fig_to_base64(fig4))

    # 5. Bar Plot: Top 3 Most Liked Deals
    top_liked = df.sort_values(by='likes', ascending=False).head(3)
    fig5, ax5 = plt.subplots(figsize=(8, 4))
    sns.barplot(x=top_liked['likes'], y=top_liked['desc'].str[:30] + '...', ax=ax5, palette=palette[:len(top_liked)])
    for i, v in enumerate(top_liked['likes']):
        ax5.text(v + 0.5, i, str(v), color='black', va='center')
    ax5.set_title("Top 3 Most Liked Deals")
    plots.append(fig_to_base64(fig5))

    return render_template("visualizations.html", plots=plots)
