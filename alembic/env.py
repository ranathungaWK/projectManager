from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# import your Base
from app.db.base import Base  # make sure this points to where your Base class is

# this is the Alembic Config object
config = context.config

# Set up Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# set target_metadata to your models’ metadata
target_metadata = Base.metadata

# DATABASE URL (can also be in alembic.ini)
config.set_main_option("sqlalchemy.url", "postgresql://postgres:Kalindu123@localhost:5432/ProjectManager")

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
