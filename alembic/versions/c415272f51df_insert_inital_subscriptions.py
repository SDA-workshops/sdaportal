"""Insert inital subscriptions

Revision ID: c415272f51df
Revises: 40292ce43618
Create Date: 2022-04-09 13:45:40.840360

"""
from alembic import op
# revision identifiers, used by Alembic.
from sqlalchemy.orm import sessionmaker

from db.model import Subscription

revision = 'c415272f51df'
down_revision = '40292ce43618'
branch_labels = None
depends_on = None

Session = sessionmaker(bind=op.get_bind())


def upgrade():
    session = Session()
    session.add_all([
        Subscription(name="Basic", price=0.0),
        Subscription(name="Advanced", price=20.0),
        Subscription(name="Platinum", price=120.0),
    ])
    session.commit()


def downgrade():
    engine = op.get_bind()
    engine.execute("TRUNCATE subscriptions")
