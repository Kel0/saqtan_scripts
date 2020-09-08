"""initial push

Revision ID: e19c081470ae
Revises: 
Create Date: 2020-09-05 18:25:35.151834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e19c081470ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city_codes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('city_code', sa.Integer(), nullable=True),
    sa.Column('city_name', sa.String(length=100), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crime_codes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('crime_code', sa.Integer(), nullable=True),
    sa.Column('crime_desc', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crimes_count_periods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('period', sa.Integer(), nullable=True),
    sa.Column('crimes_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('count_crimes_by_cities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('city_code', sa.Integer(), nullable=True),
    sa.Column('json_data', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['city_code'], ['city_codes.city_code'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('city_code')
    )
    op.create_table('crime_counts_by_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('crime_code', sa.Integer(), nullable=True),
    sa.Column('crime_type', sa.String(length=255), nullable=True),
    sa.Column('crime_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['crime_code'], ['city_codes.city_code'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('features',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('object_id', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('period', sa.Integer(), nullable=True),
    sa.Column('crime_code', sa.String(length=10), nullable=True),
    sa.Column('time_period', sa.Integer(), nullable=True),
    sa.Column('hard_code', sa.String(length=4), nullable=True),
    sa.Column('ud', sa.String(length=100), nullable=True),
    sa.Column('organ', sa.String(length=255), nullable=True),
    sa.Column('dat_vozb', sa.Integer(), nullable=True),
    sa.Column('dat_sover', sa.String(length=4), nullable=True),
    sa.Column('stat', sa.String(length=255), nullable=True),
    sa.Column('dat_vozb_str', sa.String(length=255), nullable=True),
    sa.Column('dat_sover_str', sa.String(length=255), nullable=True),
    sa.Column('tz1id', sa.String(length=255), nullable=True),
    sa.Column('reg_code', sa.String(length=100), nullable=True),
    sa.Column('city_code', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('org_code', sa.String(length=100), nullable=True),
    sa.Column('entrydate', sa.Integer(), nullable=True),
    sa.Column('fz1r18p5', sa.String(length=255), nullable=True),
    sa.Column('fz1r18p6', sa.String(length=255), nullable=True),
    sa.Column('transgression', sa.String(length=255), nullable=True),
    sa.Column('organ_kz', sa.String(length=255), nullable=True),
    sa.Column('organ_en', sa.String(length=255), nullable=True),
    sa.Column('fe1r29p1_id', sa.String(length=100), nullable=True),
    sa.Column('fe1r32p1', sa.String(length=255), nullable=True),
    sa.Column('x_geo', sa.String(length=255), nullable=True),
    sa.Column('y_geo', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['city_code'], ['city_codes.city_code'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_features_city_code'), 'features', ['city_code'], unique=False)
    op.create_index(op.f('ix_features_crime_code'), 'features', ['crime_code'], unique=False)
    op.create_index(op.f('ix_features_dat_sover'), 'features', ['dat_sover'], unique=False)
    op.create_index(op.f('ix_features_dat_sover_str'), 'features', ['dat_sover_str'], unique=False)
    op.create_index(op.f('ix_features_dat_vozb'), 'features', ['dat_vozb'], unique=False)
    op.create_index(op.f('ix_features_dat_vozb_str'), 'features', ['dat_vozb_str'], unique=False)
    op.create_index(op.f('ix_features_entrydate'), 'features', ['entrydate'], unique=False)
    op.create_index(op.f('ix_features_fe1r29p1_id'), 'features', ['fe1r29p1_id'], unique=False)
    op.create_index(op.f('ix_features_fe1r32p1'), 'features', ['fe1r32p1'], unique=False)
    op.create_index(op.f('ix_features_fz1r18p5'), 'features', ['fz1r18p5'], unique=False)
    op.create_index(op.f('ix_features_fz1r18p6'), 'features', ['fz1r18p6'], unique=False)
    op.create_index(op.f('ix_features_hard_code'), 'features', ['hard_code'], unique=False)
    op.create_index(op.f('ix_features_id'), 'features', ['id'], unique=False)
    op.create_index(op.f('ix_features_object_id'), 'features', ['object_id'], unique=False)
    op.create_index(op.f('ix_features_org_code'), 'features', ['org_code'], unique=False)
    op.create_index(op.f('ix_features_organ'), 'features', ['organ'], unique=False)
    op.create_index(op.f('ix_features_organ_en'), 'features', ['organ_en'], unique=False)
    op.create_index(op.f('ix_features_organ_kz'), 'features', ['organ_kz'], unique=False)
    op.create_index(op.f('ix_features_period'), 'features', ['period'], unique=False)
    op.create_index(op.f('ix_features_reg_code'), 'features', ['reg_code'], unique=False)
    op.create_index(op.f('ix_features_stat'), 'features', ['stat'], unique=False)
    op.create_index(op.f('ix_features_status'), 'features', ['status'], unique=False)
    op.create_index(op.f('ix_features_time_period'), 'features', ['time_period'], unique=False)
    op.create_index(op.f('ix_features_transgression'), 'features', ['transgression'], unique=False)
    op.create_index(op.f('ix_features_tz1id'), 'features', ['tz1id'], unique=False)
    op.create_index(op.f('ix_features_ud'), 'features', ['ud'], unique=False)
    op.create_index(op.f('ix_features_x_geo'), 'features', ['x_geo'], unique=False)
    op.create_index(op.f('ix_features_y_geo'), 'features', ['y_geo'], unique=False)
    op.create_index(op.f('ix_features_year'), 'features', ['year'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_features_year'), table_name='features')
    op.drop_index(op.f('ix_features_y_geo'), table_name='features')
    op.drop_index(op.f('ix_features_x_geo'), table_name='features')
    op.drop_index(op.f('ix_features_ud'), table_name='features')
    op.drop_index(op.f('ix_features_tz1id'), table_name='features')
    op.drop_index(op.f('ix_features_transgression'), table_name='features')
    op.drop_index(op.f('ix_features_time_period'), table_name='features')
    op.drop_index(op.f('ix_features_status'), table_name='features')
    op.drop_index(op.f('ix_features_stat'), table_name='features')
    op.drop_index(op.f('ix_features_reg_code'), table_name='features')
    op.drop_index(op.f('ix_features_period'), table_name='features')
    op.drop_index(op.f('ix_features_organ_kz'), table_name='features')
    op.drop_index(op.f('ix_features_organ_en'), table_name='features')
    op.drop_index(op.f('ix_features_organ'), table_name='features')
    op.drop_index(op.f('ix_features_org_code'), table_name='features')
    op.drop_index(op.f('ix_features_object_id'), table_name='features')
    op.drop_index(op.f('ix_features_id'), table_name='features')
    op.drop_index(op.f('ix_features_hard_code'), table_name='features')
    op.drop_index(op.f('ix_features_fz1r18p6'), table_name='features')
    op.drop_index(op.f('ix_features_fz1r18p5'), table_name='features')
    op.drop_index(op.f('ix_features_fe1r32p1'), table_name='features')
    op.drop_index(op.f('ix_features_fe1r29p1_id'), table_name='features')
    op.drop_index(op.f('ix_features_entrydate'), table_name='features')
    op.drop_index(op.f('ix_features_dat_vozb_str'), table_name='features')
    op.drop_index(op.f('ix_features_dat_vozb'), table_name='features')
    op.drop_index(op.f('ix_features_dat_sover_str'), table_name='features')
    op.drop_index(op.f('ix_features_dat_sover'), table_name='features')
    op.drop_index(op.f('ix_features_crime_code'), table_name='features')
    op.drop_index(op.f('ix_features_city_code'), table_name='features')
    op.drop_table('features')
    op.drop_table('crime_counts_by_types')
    op.drop_table('count_crimes_by_cities')
    op.drop_table('crimes_count_periods')
    op.drop_table('crime_codes')
    op.drop_table('city_codes')
    # ### end Alembic commands ###
