import sqlalchemy as sa

metadata = sa.MetaData()

vote_results = sa.Table(
    'voting',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.Text),
    sa.Column('votes', sa.Integer)
)
