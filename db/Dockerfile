# Use PostgreSQL 17.2 image as the base (replace with actual version if available)
FROM postgres:17.2-alpine

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=django
ENV POSTGRES_PASSWORD=django_password
ENV POSTGRES_DB=django_db

# Copy custom initialisation scripts
COPY ./scripts/ /docker-entrypoint-initdb.d/

# Expose the PostgreSQL default port
EXPOSE 5432